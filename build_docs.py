import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        # Running header (pages > 1)
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(colors.HexColor("#475569"))
            self.drawString(54, 752, "JAVA FULL-STACK & SYSTEM ENGINEERING ROADMAP (2026)")
            self.setFont("Helvetica", 8)
            self.setFillColor(colors.HexColor("#94A3B8"))
            self.drawRightString(558, 752, "Vaibhav Bhadane | Production Engineering")
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.75)
            self.line(54, 744, 558, 744)

        # Running footer (all pages)
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.75)
        self.line(54, 46, 558, 46)
        
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        self.drawString(54, 34, "Talenlio / HireOS / Standout Architecture & Interview Preparation Master Guide")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 34, page_str)
        self.restoreState()

def build_pdf():
    pdf_filename = "/Users/vaibhav/.gemini/antigravity/scratch/Java_FullStack_Interview_Roadmap.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#475569'),
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#1E3A8A'),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#334155'),
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#334155'),
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=3
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#1E293B')
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#0F172A')
    )

    code_card_style = ParagraphStyle(
        'CodeCard',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=10.5,
        textColor=colors.HexColor('#0F172A')
    )

    banner_title = ParagraphStyle(
        'BannerTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.white
    )

    banner_sub = ParagraphStyle(
        'BannerSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#93C5FD')
    )

    story = []

    # 1. HEADER BANNER BLOCK
    header_data = [
        [
            Paragraph("<b>JAVA FULL-STACK & SYSTEM ENGINEERING ROADMAP</b>", banner_title),
        ],
        [
            Paragraph("<b>Production-Grade Interview Mastery Guide (Java 8 to 21, Spring Boot, Kafka, Gemini AI, MongoDB & Angular)</b><br/>"
                      "Candidate: <b>Vaibhav Bhadane</b> | Experience: <b>1+ Years Production Full-Stack</b> | Target: <b>Remote / Global / Pune / NCR</b>", banner_sub)
        ]
    ]
    header_table = Table(header_data, colWidths=[504])
    header_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0F172A')),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('CORNERPAD', (0,0), (-1,-1), 6),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 10))

    # 2. THE 3-STAGE BLUEPRINT TABLE
    story.append(Paragraph("1. The 3-Stage Blueprint: How to Stand Out & Get Hired", h1_style))
    story.append(Paragraph("Most 1–2 YOE candidates fail because they only present basic tutorial CRUD projects. Your preparation is engineered around three distinct leverage tiers:", body_style))

    stage_table_data = [
        [
            Paragraph("Stage", table_header_style),
            Paragraph("Technical Focus & Key Tools", table_header_style),
            Paragraph("Strategic Purpose in the Interview", table_header_style),
            Paragraph("Interview Impact", table_header_style),
        ],
        [
            Paragraph("<b>STAGE 1<br/>The Gatekeepers</b>", table_cell_bold),
            Paragraph("<b>Java 17/21 Core</b> (OOP, Collections internals, Streams, Multithreading, JMM)<br/>"
                      "<b>Spring Boot</b> (IoC/DI, Bean Lifecycle, @Transactional, REST, Exceptions)", table_cell_style),
            Paragraph("Ensures you pass the <b>screening calls, online coding assessments, and Round 1 technical filters</b>. Without these, you never reach round 2.", table_cell_style),
            Paragraph("<b>Passes the Filter</b><br/>(Baseline requirement)", table_cell_bold),
        ],
        [
            Paragraph("<b>STAGE 2<br/>The Standout Weapons</b>", table_cell_bold),
            Paragraph("<b>Apache Kafka & Pub/Sub</b> (Event streaming, consumer groups, offsets)<br/>"
                      "<b>MongoDB Optimization</b> (Explain plans, COLLSCAN fix, $facet 100MB fix)<br/>"
                      "<b>Production Gemini AI</b> (Google Gen-AI SDK, JSON schema, prompt hygiene)", table_cell_style),
            Paragraph("<b>Sets you in the top 5% of candidates.</b> Juniors almost never have production message broker or query tuning experience. This justifies high-band compensation.", table_cell_style),
            Paragraph("<b>Wins the Offer</b><br/>(INR 10–16+ LPA Band)", table_cell_bold),
        ],
        [
            Paragraph("<b>STAGE 3<br/>Full-Stack Polish</b>", table_cell_bold),
            Paragraph("<b>Angular & RxJS</b> (switchMap, observables, component architecture)<br/>"
                      "<b>System Design Basics</b> (Rate limiting, Redis caching, DB replication)", table_cell_style),
            Paragraph("Proves you are an autonomous, versatile engineer who can deliver features end-to-end across backend and frontend.", table_cell_style),
            Paragraph("<b>Closes the Deal</b><br/>(Dependable engineer)", table_cell_bold),
        ]
    ]

    stage_table = Table(stage_table_data, colWidths=[90, 170, 164, 80])
    stage_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#FFFFFF'), colors.HexColor('#F8FAFC')]),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(stage_table)
    story.append(Spacer(1, 10))

    # 3. STAGE 1: JAVA CORE EVOLUTION
    story.append(Paragraph("2. Stage 1: Java Core Deep-Dive (Java 8 to Java 21 LTS)", h1_style))
    story.append(Paragraph("Interviewers test language evolution to verify if you write modern, performant code or outdated legacy syntax:", body_style))

    story.append(Paragraph("<b>A. Java 8 Essentials (The Functional Revolution):</b>", h2_style))
    story.append(Paragraph("&bull; <b>Lambda Expressions:</b> Concise implementation of Single Abstract Method (SAM) interfaces.", bullet_style))
    story.append(Paragraph("&bull; <b>Functional Interfaces:</b> <code>Predicate&lt;T&gt;</code> (boolean test), <code>Function&lt;T,R&gt;</code> (transformation), <code>Consumer&lt;T&gt;</code> (accepts arg, returns void), <code>Supplier&lt;T&gt;</code> (produces value).", bullet_style))
    story.append(Paragraph("&bull; <b>Streams API:</b> Declarative data processing pipeline. Difference between <i>Intermediate operations</i> (lazy: <code>filter()</code>, <code>map()</code>, <code>flatMap()</code>, <code>sorted()</code>) and <i>Terminal operations</i> (eager: <code>collect()</code>, <code>forEach()</code>, <code>reduce()</code>, <code>count()</code>).", bullet_style))
    story.append(Paragraph("&bull; <b>Optional&lt;T&gt;:</b> Container object used to prevent <code>NullPointerException</code>. Correct methods: <code>map()</code>, <code>orElse()</code>, <code>orElseGet()</code>, <code>orElseThrow()</code>. Never call <code>.get()</code> without <code>.isPresent()</code>.", bullet_style))
    story.append(Paragraph("&bull; <b>Default & Static Methods in Interfaces:</b> Enabled backwards compatibility for Java collection streams without breaking existing implementations.", bullet_style))

    story.append(Paragraph("<b>B. Java 11 to 17 LTS (Modern Enterprise Java):</b>", h2_style))
    story.append(Paragraph("&bull; <b>Local-Variable Type Inference (<code>var</code>):</b> Compile-time type inference for cleaner code readability (Java 10/11).", bullet_style))
    story.append(Paragraph("&bull; <b>Records (Java 14/16/17):</b> Immutable data carriers. Automatically generates constructor, getters, <code>equals()</code>, <code>hashCode()</code>, and <code>toString()</code>. Perfect for Spring Boot DTOs and Kafka payloads.", bullet_style))
    story.append(Paragraph("&bull; <b>Sealed Classes & Interfaces (Java 17):</b> Restricts which classes can extend or implement them using <code>sealed ... permits ...</code>. Provides domain-driven compile-time exhaustiveness.", bullet_style))
    story.append(Paragraph("&bull; <b>Pattern Matching for <code>instanceof</code> and <code>switch</code>:</b> Eliminates manual casting: <code>if (obj instanceof String s) { s.length(); }</code>.", bullet_style))
    story.append(Paragraph("&bull; <b>Text Blocks (<code>\"\"\"</code>):</b> Multiline strings preserving formatting without escaping quotes, ideal for JSON schemas and SQL queries.", bullet_style))

    story.append(Paragraph("<b>C. Java 21 LTS (The Future of Concurrency):</b>", h2_style))
    story.append(Paragraph("&bull; <b>Virtual Threads (Project Loom):</b> Lightweight JVM-managed threads (millions can run concurrently). Solves thread-per-request blocking I/O overhead without complex reactive programming.", bullet_style))
    story.append(Paragraph("&bull; <b>Sequenced Collections:</b> Unified interface for collections with defined encounter order (<code>getFirst()</code>, <code>getLast()</code>, <code>reversed()</code>).", bullet_style))

    story.append(Paragraph("<b>D. Critical Java Internals (Top 5 Interview Questions):</b>", h2_style))
    story.append(Paragraph("1. <b>HashMap Internal Architecture:</b> Backed by an array of Nodes/Buckets. Hash index computed via <code>(n - 1) & hash(key)</code>. Collisions are handled via linked list until bucket length reaches <b>8 (TREEIFY_THRESHOLD)</b>, where it transforms into a <b>Red-Black Tree</b> (O(log n) lookup).", bullet_style))
    story.append(Paragraph("2. <b>HashMap vs ConcurrentHashMap:</b> <code>HashMap</code> is non-thread-safe. <code>Hashtable</code> synchronizes whole methods (poor throughput). <code>ConcurrentHashMap</code> uses <b>fine-grained bucket-level synchronization and CAS (Compare-And-Swap)</b>, allowing concurrent reads without locking.", bullet_style))
    story.append(Paragraph("3. <b>Java Memory Model (Heap vs Stack):</b> Stack stores primitive values and method invocation stack frames (thread-isolated). Heap stores all objects and arrays (shared across threads). Managed by Garbage Collectors (G1 GC, ZGC).", bullet_style))
    story.append(Paragraph("4. <b>Garbage Collection Generations:</b> Young Generation (Eden + Survivor S0/S1 spaces) where objects are born; Old/Tenured Generation for objects surviving multiple minor GC cycles.", bullet_style))
    story.append(Paragraph("5. <b>ThreadPoolExecutor Architecture:</b> Core pool size, maximum pool size, keep-alive time, work queue (e.g. <code>LinkedBlockingQueue</code>), and rejection execution handlers (<code>AbortPolicy</code>, <code>CallerRunsPolicy</code>).", bullet_style))

    story.append(PageBreak())

    # 4. SPRING BOOT ARCHITECTURE
    story.append(Paragraph("3. Stage 1 (Part B): Spring Boot Microservices Mastery", h1_style))
    story.append(Paragraph("Spring Boot is the backbone of your backend profile. Interviewers expect you to explain its core lifecycle, annotations, and transaction boundaries:", body_style))

    spring_table_data = [
        [
            Paragraph("Core Concept", table_header_style),
            Paragraph("Technical Mechanism & Best Practices", table_header_style),
            Paragraph("Production Interview Answer", table_header_style)
        ],
        [
            Paragraph("<b>IoC Container & Dependency Injection</b>", table_cell_bold),
            Paragraph("Inversion of Control transfers object creation and lifecycle management to Spring's <code>ApplicationContext</code>. Always prefer <b>Constructor Injection</b> over Field Injection (<code>@Autowired</code> on private fields) because constructor injection ensures immutability, avoids reflection overhead, and makes unit testing trivial.", table_cell_style),
            Paragraph("\"In our Germany backend, we use constructor injection across all services (e.g. <code>GmailOAuthService</code>) to guarantee dependencies are non-null and simplify Mockito testing.\"", table_cell_style)
        ],
        [
            Paragraph("<b>Spring Bean Lifecycle</b>", table_cell_bold),
            Paragraph("1. Bean definition loaded ➔ 2. Instance created ➔ 3. Properties injected ➔ 4. Aware interfaces called ➔ 5. <code>@PostConstruct</code> invoked ➔ 6. <code>InitializingBean.afterPropertiesSet()</code> ➔ 7. Bean is ready for use ➔ 8. Container shutdown triggers <code>@PreDestroy</code>.", table_cell_style),
            Paragraph("\"We use <code>@PostConstruct</code> in scheduler and connection services to initialize OAuth credentials and warm up connection pools on startup.\"", table_cell_style)
        ],
        [
            Paragraph("<b>Transaction Management (<code>@Transactional</code>)</b>", table_cell_bold),
            Paragraph("Spring uses AOP proxies around methods. Default rollback occurs on <b>unchecked exceptions (RuntimeException and Error)</b>, NOT on checked exceptions. Use <code>@Transactional(rollbackFor = Exception.class)</code>. Propagation: <code>REQUIRED</code> (joins existing), <code>REQUIRES_NEW</code> (suspends existing, creates new).", table_cell_style),
            Paragraph("\"Be mindful of self-invocation: calling a <code>@Transactional</code> method from within the same class bypasses the Spring CGLIB proxy, causing the transaction to silently not start.\"", table_cell_style)
        ],
        [
            Paragraph("<b>Global Exception Handling</b>", table_cell_bold),
            Paragraph("Use <code>@RestControllerAdvice</code> with <code>@ExceptionHandler</code> methods. Returns consistent HTTP status codes (400, 401, 403, 404, 500) and standard error DTO bodies (RFC 7807 Problem Details).", table_cell_style),
            Paragraph("\"Prevents stack traces leaking to clients and provides structured machine-readable error codes to frontend clients.\"", table_cell_style)
        ],
        [
            Paragraph("<b>Spring Security & JWT Filter Chain</b>", table_cell_bold),
            Paragraph("Requests pass through <code>SecurityFilterChain</code>. A custom <code>OncePerRequestFilter</code> intercepts incoming HTTP requests, extracts the <code>Bearer &lt;token&gt;</code>, validates signature & expiration, and populates the <code>SecurityContextHolder</code>.", table_cell_style),
            Paragraph("\"Guarantees stateless authentication across microservices without session storage overhead.\"", table_cell_style)
        ]
    ]

    spring_table = Table(spring_table_data, colWidths=[110, 214, 180])
    spring_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#FFFFFF'), colors.HexColor('#F8FAFC')]),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(spring_table)
    story.append(Spacer(1, 10))

    # 5. STAGE 2: STANDOUT WEAPONS (KAFKA, MONGO, AI)
    story.append(Paragraph("4. Stage 2: The Standout Weapons (Kafka, Mongo & Gemini AI)", h1_style))
    story.append(Paragraph("These are your core differentiators. Master these production architectural narratives to prove you are a top-tier engineer:", body_style))

    story.append(Paragraph("<b>A. Apache Kafka & Event Streaming (The Gmail Tracker Pipeline):</b>", h2_style))
    story.append(Paragraph("&bull; <b>Core Architecture:</b> Topic, Partition, Offset, Consumer Group. Partitions allow horizontal scaling; Kafka guarantees ordering <i>only within a single partition</i>.", bullet_style))
    story.append(Paragraph("&bull; <b>Producer Guarantees:</b> <code>acks=all</code> (all in-sync replicas acknowledge), <code>enable.idempotence=true</code> (prevents duplicate message writes on network retries).", bullet_style))
    story.append(Paragraph("&bull; <b>Consumer Groups & Rebalancing:</b> If a consumer crashes or is added, Kafka triggers rebalance. Offset commit strategies: Avoid auto-commit (<code>enable.auto.commit=false</code>) in critical pipelines; commit manually after successful database persistence to prevent message loss.", bullet_style))
    story.append(Paragraph("&bull; <b>Talenlio Event Flow:</b> Google Pub/Sub push webhook ➔ <code>GmailWebhookController</code> ➔ dispatches event to Kafka <code>EMAIL_TOPIC</code> ➔ <code>GmailSyncEventListener</code> processes sync asynchronously ➔ Calls Gemini AI ➔ Writes to Firestore. Decouples fast webhook responses from heavy AI processing.", bullet_style))

    story.append(Paragraph("<b>B. MongoDB Performance Engineering (Real Production Post-Mortems):</b>", h2_style))
    story.append(Paragraph("&bull; <b>Fixing the $facet 100MB Memory Crash:</b> In candidate search queries, a single aggregation used <code>$facet</code> to compute both total count and paginated result documents. In large datasets, the in-memory buffer exceeded MongoDB's 100MB RAM ceiling, throwing <code>UNHANDLED_ERROR 99999</code>. <b>Fix:</b> Separated count and pagination into two parallel, indexed queries.", bullet_style))
    story.append(Paragraph("&bull; <b>Eliminating Full Collection Scans (COLLSCAN):</b> User lookup queries were executing <code>$toLower</code> inside the filter across 62,000+ records. Functions inside filters invalidate B-Tree index lookups, forcing full collection scans. <b>Fix:</b> Stored normalized lowercase strings and indexed the stored field directly (IXSCAN).", bullet_style))
    story.append(Paragraph("&bull; <b>Data Modeling Rule (Anti-Pattern):</b> Never store unbounded growing arrays inside a single Mongo document (16MB document limit and document relocation cost). Fan-out relationships must be stored as separate rows/documents.", bullet_style))

    story.append(Paragraph("<b>C. Production Generative AI Integration (Google Gemini SDK):</b>", h2_style))
    story.append(Paragraph("&bull; <b>Structured Output vs Text:</b> Migrated from unstructured API calls to the official Google Gen-AI SDK using <code>GeminiAiService.generateData(String prompt, Class&lt;T&gt; clazz)</code> to enforce strict schema-validated JSON.", bullet_style))
    story.append(Paragraph("&bull; <b>Production Guardrails:</b> Input truncated at 30,000 characters to prevent token buffer overruns; sanitization pipeline strips markdown code fences (<code>```json</code>) before Jackson parsing; API timeout and quota retry fallback strategies.", bullet_style))

    story.append(PageBreak())

    # 6. STAGE 3 & COMMUNICATION
    story.append(Paragraph("5. Stage 3 & Communication: Full-Stack Edge & Interview Delivery", h1_style))
    story.append(Paragraph("To complete your profile as an autonomous engineer and convert technical discussions into job offers:", body_style))

    story.append(Paragraph("<b>A. Angular & Full-Stack Fundamentals:</b>", h2_style))
    story.append(Paragraph("&bull; <b>RxJS Reactive Operators:</b> <code>switchMap</code> (cancels previous inner observable—used for search autocomplete), <code>mergeMap</code> (runs concurrently), <code>exhaustMap</code> (ignores incoming emissions while busy—used for save/submit buttons), <code>catchError</code> (graceful fallback).", bullet_style))
    story.append(Paragraph("&bull; <b>Change Detection (Default vs OnPush):</b> <code>OnPush</code> only checks the component when <code>@Input()</code> reference changes, an event originates from the component, or an async pipe emits. Drastically improves render performance in large dashboards.", bullet_style))
    story.append(Paragraph("&bull; <b>Real-time Firestore Listeners:</b> Set up Angular service subscriptions listening to Firestore subcollection snapshots, updating Kanban board cards reactively without manual HTTP polling.", bullet_style))

    story.append(Paragraph("<b>B. The 90-Second Self-Introduction (Word-for-Word Script):</b>", h2_style))
    intro_box_data = [[
        Paragraph(
            "\"Hi, I am Vaibhav Bhadane. I am a Software Engineer with over a year of hands-on production experience building distributed backend systems and full-stack web applications.<br/><br/>"
            "At Talenlio, I worked on our core recruitment platforms—Standout and HireOS. On the backend, I specialize in <b>Java and Spring Boot</b>, designing event-driven microservices using <b>Apache Kafka</b> and <b>Google Cloud Pub/Sub</b>. I owned our <b>Gmail Email Tracker</b> feature end-to-end, which ingests webhook events into Kafka and integrates the <b>Google Gemini AI SDK</b> to classify candidate emails into recruitment stages with real-time sync to Firestore.<br/><br/>"
            "I've also handled production database tuning in MongoDB, solving memory bottlenecks and query latency, as well as building responsive interfaces in <b>Angular</b>. I am passionate about clean architecture, performance optimization, and building resilient systems, and I am excited about opportunities to contribute to high-scale engineering teams.\"",
            code_card_style
        )
    ]]
    intro_table = Table(intro_box_data, colWidths=[504])
    intro_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F1F5F9')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
    ]))
    story.append(intro_table)
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>C. The 4-Step Framework for Handling Unknown Questions:</b>", h2_style))
    story.append(Paragraph("1. <b>Pause and Clarify:</b> Take a 2-second breath. Do not guess blindly. Restate the question to ensure you understand the goal.", bullet_style))
    story.append(Paragraph("2. <b>Be Transparent:</b> Say: <i>\"I haven't used [Tool X] directly in production yet, but based on its purpose...\"</i>", bullet_style))
    story.append(Paragraph("3. <b>Bridge to Known Experience:</b> <i>\"...it solves a similar problem to [Tool Y] which I used at Talenlio. In Talenlio, we handled that by...\"</i>", bullet_style))
    story.append(Paragraph("4. <b>Reason First Principles:</b> Explain how you would approach designing the solution (e.g. data consistency, caching, latency). Interviewers value structured thinking over rote memorization.", bullet_style))

    story.append(Spacer(1, 10))
    story.append(Paragraph("6. The 90-Day Execution Timeline & Milestones", h1_style))

    timeline_data = [
        [
            Paragraph("Phase", table_header_style),
            Paragraph("Weekly Focus", table_header_style),
            Paragraph("Exact Deliverables & Milestones", table_header_style)
        ],
        [
            Paragraph("<b>MONTH 1<br/>(Days 1 - 30)</b>", table_cell_bold),
            Paragraph("<b>Weeks 1–2:</b> Java 17 Core (OOP, HashMap, Streams, Threads)<br/>"
                      "<b>Weeks 3–4:</b> Spring Boot (IoC, Beans, @Transactional, REST, Security)<br/>"
                      "<b>Daily:</b> Spoken Introduction & Phone screening scripts", table_cell_style),
            Paragraph("&bull; Answer 30 core Java & Spring Boot questions without notes.<br/>"
                      "&bull; Deliver the 90-second intro fluently in English.<br/>"
                      "&bull; Zero coding blanks on core Collections and Streams.", table_cell_style)
        ],
        [
            Paragraph("<b>MONTH 2<br/>(Days 31 - 60)</b>", table_cell_bold),
            Paragraph("<b>Weeks 5–6:</b> Kafka & Pub/Sub event streams + MongoDB tuning<br/>"
                      "<b>Week 7:</b> Gemini AI SDK integration + Angular RxJS basics<br/>"
                      "<b>Week 8:</b> Resume & Profile Overhaul + Mock Interview #1 & #2", table_cell_style),
            Paragraph("&bull; Flawless 5-minute STAR explanation of Gmail Tracker & Mongo fix.<br/>"
                      "&bull; Launch optimized profile on Instahyre, Weekday & Wellfound.<br/>"
                      "&bull; Pass 2 technical mock interviews.", table_cell_style)
        ],
        [
            Paragraph("<b>MONTH 3<br/>(Days 61 - 90)</b>", table_cell_bold),
            Paragraph("<b>Weeks 9–10:</b> Active application blitz (10 applications/day)<br/>"
                      "<b>Weeks 11–12:</b> Attend technical rounds, system design, and offer closing", table_cell_style),
            Paragraph("&bull; 3–5 active recruiter screening calls per week.<br/>"
                      "&bull; Convert technical interviews into final rounds.<br/>"
                      "&bull; Secure 1 to 2 written job offers in the INR 10–16+ LPA band.", table_cell_style)
        ]
    ]

    timeline_table = Table(timeline_data, colWidths=[90, 204, 210])
    timeline_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#FFFFFF'), colors.HexColor('#F8FAFC')]),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(timeline_table)

    doc.build(story, canvasmaker=NumberedCanvas)
    print("Roadmap PDF built successfully at:", pdf_filename)

if __name__ == '__main__':
    build_pdf()
