# Master Project Context & Interview Knowledge Vault

This document compiles the complete technical architecture, projects, problem-solving accomplishments, and interview preparation strategies across your work on **Talenlio / HireOS / Standout**.

---

## 1. High-Level System Architecture & Ecosystem

You worked as a **Full-Stack & Mobile Software Engineer** on a distributed talent and recruitment platform serving two distinct audiences:
- **Standout (`switzerland`)**: Talent-facing web portal (job tracking, resume building, AI mock interviews, assessments).
- **HireOS (`saudi-arabia`)**: Employer/recruiter-facing enterprise portal (candidate management, job postings, talent pools, assessment assigning, analytics).
- **Mobile App (`turkey`)**: Flutter mobile application for talents (job tracking, applications, chat, profile management).

```
                      +-----------------------------+
                      |       Client Layer          |
                      +--------------+--------------+
                                     |
         +---------------------------+---------------------------+
         |                           |                           |
  [ Angular Web ]             [ Angular Web ]             [ Flutter Mobile ]
   Standout (Talent)          HireOS (Employer)              Turkey (Talent)
   (repo: switzerland)       (repo: saudi-arabia)            (repo: turkey)
         |                           |                           |
         +---------------------------+---------------------------+
                                     |
                            [ API Gateway / JWT ]
                                     |
         +---------------------------+---------------------------+
         |                           |                           |
  [ Spring Boot Backend ]     [ Node.js Chat / Sync ]     [ Sandbox Execution ]
    Core Logic, MongoDB,        Real-time messaging,        Code challenge eval
    Kafka, Gemini AI            WebSockets, Push            (vietnam / JadugarGoGo)
    (repo: germany)             (repo: argentina)
         |                           |
         +-------------+-------------+
                       |
     +-----------------+-----------------+
     |                 |                 |
[ MongoDB Atlas ]  [ Firestore ]   [ Apache Kafka ]   [ Google Cloud Pub/Sub ]
```

### Microservices & Repositories Map
| Repository | Technology | Purpose & Responsibility |
|---|---|---|
| **germany** | Spring Boot (Java 17/21), MongoDB, Kafka | Core backend business logic, authentication, candidate & job management, payments, AI services |
| **switzerland** | Angular, RxJS, Tailwind, Material | Standout web platform (Talent UI): job search, application tracking, resume builder, assessments |
| **saudi-arabia** | Angular, RxJS, Tailwind | HireOS web platform (Employer UI): candidate pipeline, job posting, custom forms, organization management |
| **turkey** | Flutter (Dart), BLoC / State, Firebase | Cross-platform mobile app for iOS & Android (talent job tracker, alerts, chat, payments) |
| **argentina** | Node.js, Express, WebSocket | Real-time messaging service, sequence-ordered chat delivery, push notification triggers |
| **brazil** | Node.js, Streams | High-volume analytics, reporting, and asynchronous CSV exports |
| **vietnam / JadugarGoGo** | Go / Python / Sandbox | Secure sandbox code execution engine for candidate technical assessments |
| **norway / mexico** | Node.js / Puppeteer | Headless resume PDF generation and layout rendering engine |

---

## 2. Key Flagship Projects Owned & Delivered (STAR Method)

When interviewing, use the **STAR method** (Situation, Task, Action, Result).

### Project 1: Gmail Email Tracker with Gemini AI Classification
- **Situation**: Job seekers had to manually track application statuses by toggling between external email accounts and the Talenlio Kanban board. Application statuses frequently went stale.
- **Task**: Architect an end-to-end automated email tracking system that connects to Gmail via OAuth2, listens for incoming job updates in real time, classifies emails into recruitment stages using Generative AI, and updates the talent's Kanban board seamlessly.
- **Action**:
  - **Auth & Integration**: Implemented OAuth2 authorization code flow with automatic token refresh in Spring Boot (`GmailOAuthService`), storing credentials securely.
  - **Webhook & Event Streaming**: Configured Google Pub/Sub watch subscriptions on the user's Gmail mailbox renewing every 6 hours. When Google sends a push notification, the Spring Boot webhook controller ingests it and publishes a `GmailSyncEventDpo` to an Apache Kafka `EMAIL_TOPIC`.
  - **AI Classification**: Built `JobEmailDetectionService` utilizing the **Google Gen-AI SDK (Gemini)** with structured JSON output prompts to classify emails into distinct recruitment lifecycle stages (`APPLIED`, `SCREENING`, `INTERVIEW`, `OFFER`, `REJECTED`, `WISHLIST`) with confidence scores (`EXACT`, `HIGH`, `MEDIUM`, `LOW`, `AUTO_DETECTED`).
  - **Real-Time Storage & Sync**: Stored thread and message metadata in Google Cloud Firestore under `talent__talent/{talentId}/emails/{threadId}`. In Angular (`switzerland`), set up real-time Firestore snapshot listeners to instantly update the Kanban board without manual page refreshes.
- **Result**: Completely automated status tracking for talents, eliminating manual data entry and providing instant email context directly within application cards.

### Project 2: High-Volume MongoDB Optimization & Crash Mitigation
- **Situation**: In production, candidate and job searches began throwing catastrophic `UNHANDLED_ERROR 99999` and out-of-memory errors. The MongoDB cluster was experiencing CPU spikes due to severe COLLSCANs (collection scans) and memory allocation failures.
- **Task**: Identify root causes of slow queries and memory crashes across production databases and implement long-term structural fixes.
- **Action**:
  - **Fixed `$facet` 100MB Memory Overflow**: In applicant search queries, MongoDB was running unbounded `$facet` aggregations combining count and pagination into one pipeline, hitting the 100MB in-memory aggregation limit. Split the pipeline into separate count and targeted page queries.
  - **Eliminated Case-Insensitive COLLSCANs**: Discovered user lookup queries using `$toLower` inside query filters on 60,000+ documents, bypassing B-Tree indexes and triggering full table scans. Migrated to indexed normalized lowercase fields.
  - **Handled Zero-Division & Edge Cases**: Identified divide-by-zero crashes when `pageSize: 0` was passed into `FacetSearchMapper.getTotalPages()`, adding defensive boundary checks.
- **Result**: Reduced search latency from over 30 seconds to under 120ms, eliminated memory crashes, and brought query targeting back to optimal 1:1 index efficiency.

### Project 3: Flutter Mobile App (Turkey) Performance & Frame Budget Optimization
- **Situation**: The mobile app experienced noticeable scroll jank, visual stuttering, and startup crashes on newer mobile OS versions (e.g., iOS UIScene lifecycle changes and Android Google Credential Manager updates).
- **Task**: Optimize rendering performance to achieve a smooth 60–120 FPS, resolve startup crashes, and modernize auth flows.
- **Action**:
  - **Eliminated Scroll Jank**: Analyzed frame budgets using `addTimingsCallback` targeting the 8.33ms (120Hz) frame threshold. Found expensive dynamic backdrop frost blurs (`BackdropFilter`) causing 500+ over-budget frames during list scrolls. Refactored layout to use lightweight pre-rendered gradients, bringing dropped frames to zero.
  - **Resolved Crashlytics & OS Breakages**: Migrated legacy Google Sign-In to the Android `Credential Manager` API, preventing `SignInHubActivity` NPEs. Updated iOS `UIScene` lifecycle configs in `Info.plist` to prevent launch termination.
  - **Widget Tree Hygiene**: Addressed red-screen assertion failures in collapsing headers and scoped dependencies by validating constraints before layout computation.
- **Result**: Reached consistent 120 FPS scrolling across feed and application boards, resolved critical launch crashes, and stabilized mobile releases.

### Project 4: Reliable Distributed Chat & Notification Pipeline
- **Situation**: Under high concurrency or poor network conditions, candidate-employer chat messages arrived out of order, and push notifications were clearing entire notification trays on tap.
- **Action**:
  - Implemented sequence-based message ordering (`seq` counter per conversation) in Node.js (`argentina`) to guarantee strictly ordered, idempotent delivery.
  - Configured notification group IDs and specific intent payload routing in Flutter so tapping a single message dismisses only that specific notification rather than wiping the user's notification group.
- **Result**: Rock-solid real-time messaging parity between mobile and web applications with reliable offline catch-up.

---

## 3. How to Present "Working with AI" in Interviews

### The Common Trap
❌ *"AI wrote most of my code, and I don't remember the details."* (This immediately kills senior/mid-level interviews).

### The Winning Senior Framing
✅ **Frame AI as your Developer Tool & Productivity Multiplier:**
1. **"I owned the architecture, data models, and trade-offs."**
   > *"I used AI assistants like Gemini and Claude as pair-programming accelerators for drafting repetitive boilerplate, creating mock test fixtures, and stress-testing edge cases. However, all domain architecture, database index strategy, Kafka topic partitioning, and API contracts were engineered and validated by me."*
2. **"AI helped me explore edge cases faster."**
   > *"For instance, when designing the Gmail Sync pipeline, I used AI to brainstorm failure modes in Pub/Sub renewal tokens, but I wrote the actual scheduler, retry policies, and error boundaries."*
3. **"I engineered the prompts and integration pipelines."**
   > *"In the Email Tracker feature, I integrated Gemini AI into production using the official Google Gen-AI SDK. I engineered prompts with structured output validation, enforced schema sanitization, and implemented fallback handling for non-standard email structures."*

---

## 4. Technical Concepts to Master for Your Interviews

### Backend (Spring Boot & Distributed Systems)
- **Spring Boot Ecosystem**: Dependency injection, `@Transactional` boundaries, Spring Data MongoDB, interceptors, filters, JWT authentication.
- **Event-Driven Architecture**:
  - Why use **Kafka** vs **Pub/Sub**? Pub/Sub was used as the external Google webhook ingestion buffer; Kafka was used as the internal distributed event backbone with consumer groups.
  - Consumer offset management, idempotency, dead-letter queues (DLQ).
- **Database Engineering (MongoDB & Firestore)**:
  - B-Tree compound indexing, prefix rules, index selectivity (`nReturned` vs `totalKeysExamined`).
  - Unbounded arrays vs fan-out document models (why embedding infinite subdocuments is an anti-pattern in Mongo).
  - Firestore document hierarchies (`collection -> doc -> subcollection`) and real-time WebSocket listener cost models.

### Frontend (Angular & TypeScript)
- **Change Detection**: Default vs `OnPush` strategy, NgZone, `markForCheck()`.
- **RxJS Patterns**: `switchMap` (cancelling previous calls like auto-complete), `mergeMap` (concurrent executions), `exhaustMap` (ignoring clicks while in-flight), `catchError`.
- **State Management**: Reactive state, behavioral subjects, route resolvers, CDK overlays, and responsive breakpoints.

### Mobile (Flutter & Dart)
- **Rendering Pipeline**: Widget tree -> Element tree -> RenderObject tree.
- **Frame Budgeting**: 16.6ms (60Hz) vs 8.33ms (120Hz), raster thread vs UI thread bottlenecks, avoiding `BackdropFilter` and unbounded repaints in list views.
- **Native Bridges & Lifecycle**: Method channels, Android Foreground Services, iOS SceneDelegate.

---

## 5. Strategy for Your New Dedicated Chat Sessions

Instead of one giant, cluttered conversation where you try to learn everything at once, break your interview preparation into **5 laser-focused sessions**:

1. **Session 1: Backend Architecture & Spring Boot Deep Dive**
   - Goal: Walk through the exact request lifecycle of `germany` from Controller -> Service -> Repository -> MongoDB.
   - Practice: "Tell me about a time you optimized a slow database query."
2. **Session 2: Event-Driven Systems & Kafka / Pub/Sub**
   - Goal: Deep-dive into the Gmail Email Tracker event stream and how you handled token renewals, webhook idempotency, and failures.
   - Practice: System design interview on building a real-time event pipeline.
3. **Session 3: Generative AI in Production (Gemini SDK)**
   - Goal: Master structured output prompting, token budget management, JSON parsing hygiene, and error recovery.
   - Practice: "How have you used LLMs in a production system beyond simple chat?"
4. **Session 4: Angular & State Management (Standout & HireOS)**
   - Goal: Deep-dive into component lifecycle, RxJS operators, form validation patterns, and responsiveness.
   - Practice: Frontend architecture & performance optimization questions.
5. **Session 5: Mock Interview & Behavioral Drills (STAR)**
   - Goal: Run a full 45-minute simulated technical interview where the AI grills you on architectural trade-offs, debugging stories, and leadership questions.
