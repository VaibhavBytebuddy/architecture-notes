# Company-by-Company Technical Interview Intelligence (2026)
**Target Profile:** Software Engineer / Java Full-Stack (Java 17/21, Spring Boot, Kafka, MongoDB, Gemini AI, Angular)  
**Locations:** Remote (1st Priority), Pune / Mumbai, Delhi-NCR (Gurgaon/Noida) — *Excluding South India*

---

## 🏢 Tier 1: Remote-First & Developer Platform Startups

### 1. BrowserStack (Remote-First / Mumbai)
* **Engineering Culture:** High-concurrency systems, developer tools, distributed test runners.
* **Hiring Pipeline (4 Rounds):**
  * **Round 1: Machine Coding / Live Coding (90 mins)**
    * *Task:* Implement a functional, thread-safe module from scratch in Java with working JUnit tests.
    * *Frequent Problems:* 
      1. Design an In-Memory Cache with eviction policies (LRU/LFU) and TTL expiration.
      2. Design a Thread-Safe In-Memory Message Queue (Publish/Subscribe pattern).
      3. Design a Distributed Rate Limiter (Token Bucket or Sliding Window).
    * *Evaluation Rubric:* Clean Object-Oriented Principles (SOLID), thread safety (`ConcurrentHashMap`, `ReentrantLock`, `AtomicInteger`), handling race conditions, and unit test coverage.
  * **Round 2: Data Structures & Concurrency Deep-Dive (60 mins)**
    * *Focus:* Multithreading internals, JVM memory model, deadlock detection, producer-consumer pattern.
    * *Questions Asked:* How `ConcurrentHashMap` avoids full locks; differences between `synchronized`, `ReentrantLock`, and `StampedLock`; Java thread pool executor queue overflow strategies.
  * **Round 3: System Architecture & Past Production Experience (60 mins)**
    * *Focus:* Deep-dive into your Talenlio architecture.
    * *Questions Asked:* How you architected the Gmail Tracker pipeline; Kafka partition key selection; handling Google Pub/Sub webhook failures; why you chose Firestore over MongoDB for real-time Kanban sync.
  * **Round 4: Engineering Director / Culture Round (45 mins)**
    * *Focus:* Autonomy, asynchronous communication, handling production outages, engineering philosophy.

---

### 2. Wingify / VWO & HackerRank (Remote / Delhi-NCR)
* **Engineering Culture:** High-throughput event ingestion, A/B testing statistical engines, developer assessments.
* **Hiring Pipeline (3–4 Rounds):**
  * **Round 1: Take-Home or Live Pair Programming (60–90 mins)**
    * Build a Spring Boot REST service with clean DTO validation, service layer separation, and global exception handling.
  * **Round 2: Low-Level Design (LLD) & Algorithms (60 mins)**
    * Design a URL Shortener or Feature Flag evaluation engine in Java.
  * **Round 3: Distributed Systems & Kafka Flow (60 mins)**
    * Deep-dive into event brokers, message ordering guarantees, consumer group rebalancing, and database read/write decoupling.
  * **Round 4: Culture & Hiring Manager (30 mins)**

---

## 🏢 Tier 2: Pune & Mumbai GCCs & Fintech Titans

### 3. Mastercard (Pune Tech Hub)
* **Engineering Culture:** Resilient payment gateways, microservice compliance, strict transaction boundaries, Decency Quotient (DQ).
* **Hiring Pipeline (4–5 Rounds):**
  * **Round 1: HR & Screening (30 mins)**
    * Communication check, experience breakdown, current/expected compensation, notice period.
  * **Round 2: Online Assessment / Karat Technical Screen (60 mins)**
    * 2–3 algorithmic problems on HackerRank/Codility focusing on Arrays, Strings, Two Pointers, and Trees.
  * **Round 3: Technical SME Round — Java & Spring Boot Deep-Dive (60 mins)**
    * *Java 17/21:* `HashMap` internal node bucketing, hash computation `(n - 1) & hash`, Red-Black tree conversion threshold (8), Garbage Collection generations (Eden, Survivor, Tenured), G1 GC vs ZGC.
    * *Spring Boot:* Bean lifecycle from instantiation to `@PostConstruct` and `@PreDestroy`; constructor injection vs field injection; `@Transactional` rollback rules on unchecked vs checked exceptions; Spring Security filter chain with JWT.
  * **Round 4: Bar Raiser & Debugging Round (60 mins)**
    * *Live Debugging:* Interviewer provides a buggy piece of Java code with concurrency race conditions or memory leaks and asks you to diagnose and fix it.
    * *Database Tuning:* Explain plans, eliminating full collection scans (COLLSCAN) in MongoDB, indexing strategies (ESR rule).
  * **Round 5: Hiring Manager & Decency Quotient (DQ) (45 mins)**
    * Behavioral evaluation, past project architecture at Talenlio, conflict resolution, handling technical debt.

---

### 4. Barclays & BNY Mellon (Pune Tech Hubs)
* **Engineering Culture:** Core banking transactions, fault tolerance, Spring Boot microservices, high security.
* **Hiring Pipeline (3–4 Rounds):**
  * **Round 1: Online Coding Test (HackerRank)** — 2 DSA questions + Core Java MCQs.
  * **Round 2: Core Java & Concurrency (60 mins)** — Thread safety, Java Streams API lazy evaluation, `CompletableFuture` chaining, JVM profiling.
  * **Round 3: Microservices & Database Design (60 mins)** — API Gateway, circuit breakers (Resilience4j), distributed transactions (Saga pattern), ACID properties in MongoDB/PostgreSQL.
  * **Round 4: Techno-Managerial Round (45 mins)** — System scalability, production war stories, team collaboration.

---

## 🏢 Tier 3: Delhi-NCR High-Growth Tech & Unicorns

### 5. Zomato & Blinkit (Gurgaon HQ)
* **Engineering Culture:** Rapid shipping, extreme scale, real-time logistics, high-stress problem solving.
* **Hiring Pipeline (3–4 Rounds):**
  * **Round 1: Online Assessment (OA)** — 2–3 Medium/Hard algorithmic challenges (Sliding Window, Heaps, Graphs).
  * **Round 2: Live Problem Solving & Concurrency (60 mins)**
    * Write clean, runnable code in collaborative editor (handling all edge cases).
    * Thread-safety problems: producer-consumer, rate limiting, task scheduling.
  * **Round 3: Low-Level Design (LLD) & Production Deep-Dive (60 mins)**
    * *Machine/Object Design:* Design a Restaurant Menu Service, Food Delivery Tracking, or Notification Engine.
    * *Project Defense:* Defend your Talenlio architecture: Why Kafka over RabbitMQ? How did you resolve the 100MB `$facet` aggregation crash in MongoDB? How do you prevent Gemini AI API rate limiting from blocking user requests?
  * **Round 4: Engineering Director / Culture & Ownership (45 mins)**
    * Evaluates high ownership, bias for action, dealing with production outages under pressure.

---

### 6. MakeMyTrip (Gurgaon)
* **Engineering Culture:** High-throughput booking engines, caching architectures, distributed search.
* **Hiring Pipeline (3–4 Rounds):**
  * **Round 1:** Coding Assessment (Array manipulation, dynamic programming, strings).
  * **Round 2:** Data Structures & Java Internals (Java Collections, Multithreading, Spring Boot REST).
  * **Round 3:** System Architecture & Caching (Redis Cache-Aside pattern, Kafka event pipelines, database indexing).
  * **Round 4:** Engineering Manager Round.

---

## 📋 Comprehensive Topic-to-Company Matrix

| Core Topic | Tested By | Exact Question Pattern |
|---|---|---|
| **HashMap & ConcurrentHashMap Internals** | Mastercard, Barclays, Zomato | Bucket array structure, hash calculation, treeify threshold 8, CAS + bucket lock. |
| **Java Concurrency & ThreadPoolExecutor** | BrowserStack, Zomato, BNY Mellon | ThreadPool parameters, rejection execution handlers, Virtual Threads vs Platform Threads. |
| **Spring Boot `@Transactional` & AOP** | Mastercard, Barclays, MakeMyTrip | Proxy mechanism, rollback on `RuntimeException`, self-invocation proxy bypass bug. |
| **Apache Kafka & Event Streaming** | Zomato, BrowserStack, Mastercard | Partition key distribution, consumer group rebalancing, offset commits, idempotency. |
| **MongoDB Optimization & Explain Plans** | Zomato, BrowserStack, Wingify | Resolving 100MB `$facet` crash, COLLSCAN vs IXSCAN, compound indexing rules. |
| **Machine Coding: In-Memory Cache / Rate Limiter** | BrowserStack, Zomato, HackerRank | 60–90 min runnable Java code with thread safety and clean JUnit 5 tests. |
