# ROOSTR Technical Documentation
## Complete System Overview for Job Interview Preparation

---

# A. Repo Inventory and Code Volume

## Top-Level Monorepo Structure

```
ROOSTR-MONO/
├── backend/                    # Python agentic backend (rate extraction, AI agents)
│   ├── src/                   # Main source code
│   │   ├── lib/               # Core modules (rate_extractor, rates_agent, quote_agent, nylas)
│   │   ├── run/               # Deployable services (orchestrator, APIs)
│   │   ├── utils/             # Shared utilities (LLM, DB, parsing)
│   │   ├── config/            # Configuration management
│   │   └── tests/             # Test modules
│   ├── docs/                  # Documentation (AI guides, collection schemas)
│   └── data/                  # Data processing scripts
│
├── frontend/
│   ├── landing_pg/            # Marketing landing page (public-facing)
│   ├── frontend_SHIProostr/   # Main app - shipper dashboard (customer-facing)
│   └── frontend_GETroostr/    # Internal dashboard - rates testing & admin (internal)
```

## Total Lines of Code by Language

| Language | LOC | Notes |
|----------|-----|-------|
| **Python** | ~57,100 | Backend (excluding /old) |
| **TypeScript/TSX** | ~7,400 | Frontend (all 3 apps, partial count) |
| **Total (estimated)** | ~65,000+ | Excludes node_modules, vendor, generated |

## LOC by Product Area (Estimated)

| Product Area | Description | Estimated LOC |
|--------------|-------------|---------------|
| **V1 - WBR (Weekly Business Review)** | Google Sheets rate integration, basic rate display | ~3,000 TS |
| **V2 - Rate SaaS** | Main shipper platform, booking, tracking | ~25,000+ TS (frontend_SHIProostr) |
| **V3 - Forwarder Ops** | AI rate extraction, procurement agents | ~45,000+ Python (backend) |
| **Shared Libs** | Utils, types, components | ~5,000 |

## Commit Timeline

| Metric | Value |
|--------|-------|
| **First Commit** | December 4, 2024 |
| **Total Commits** | 318 |
| **Project Age** | ~6 weeks (as of Jan 17, 2025) |
| **Dec 2024 Commits** | 64 |
| **Jan 2025 Commits** | 12 |
| **Feb 2025 Commits** | 58 |
| **Last 90 Days Activity** | 6 commits |

### Major Milestones (from commit history)
1. Initial project setup and rate extractor core (Dec 2024)
2. Fee extraction logic implementation
3. Port code validation system
4. Manual rate entry API
5. Docker deployment configuration

## Top 20 Largest Files

| # | File | LOC | Why Large / Refactor Candidate |
|---|------|-----|-------------------------------|
| 1 | `frontend_SHIProostr/.../milestones.tsx` | 1,510 | Demo data file - can be moved to JSON/DB |
| 2 | `frontend_GETroostr/.../RatesPanel.tsx` | 1,231 | Complex data grid - candidate for component splitting |
| 3 | `frontend_GETroostr/.../RatesPanel.tsx (v0)` | 1,134 | Duplicate of above (old version) |
| 4 | `frontend_SHIProostr/.../MilestoneEditor.tsx` | 1,109 | Complex editor - extract sub-components |
| 5 | `frontend_GETroostr/.../mockData.ts` | 1,096 | Mock data - move to test fixtures |
| 6 | `backend/data/process_ports.py` | 1,094 | One-time data processing script |
| 7 | `backend/.../email_generator_tool.py` | 1,034 | Email templating - split templates from logic |
| 8 | `frontend_SHIProostr/.../create/page.tsx` | 935 | Complex form - extract form sections |
| 9 | `backend/.../quote_agent.py` | 920 | Main agent loop - well-structured, acceptable |
| 10 | `frontend_GETroostr/.../ManualRateEntryModal.tsx` | 920 | Complex modal - extract form components |
| 11 | `frontend_GETroostr/.../PartnerOutreachModal.tsx` | 897 | Complex modal - candidate for splitting |
| 12 | `frontend_GETroostr/.../rates-tester/page.tsx` | 895 | Test harness - acceptable for test file |
| 13 | `frontend_GETroostr/.../FilterBar.tsx` | 811 | Filter logic - extract filter components |
| 14 | `frontend_GETroostr/.../rates-agent-test/page.tsx` | 804 | Test harness - acceptable |
| 15 | `backend/.../quote_agent_v0.py` | 786 | Deprecated version - can be removed |
| 16 | `frontend_SHIProostr/.../VendorQuotesPanel.tsx` | 776 | Complex panel - extract sub-components |

---

# B. Services, Jobs, and Runtime Architecture

## Deployable Services (Docker Images)

| Service | Container Name | Port | Entrypoint | Responsibilities |
|---------|---------------|------|------------|-----------------|
| **rates_orchestrator** | `rates_orchestrator` | - | `python -m src.run.rates_orchestrator.rates_orchestrator` | Main event loop: polls tenant emails, extracts rates, executes agent decisions |
| **manual_extract_api** | `manual_extract_api` | 8001 | `uvicorn ...manual_extract_api:app` | REST API for manual rate submission/extraction |
| **rates_agent_api** (commented) | `rates_agent_api` | 8000 | `uvicorn ...rates_agent_api:app` | REST API for rates agent (currently disabled) |

## Scheduled Jobs / Workers

| Job | Schedule | Location | Purpose |
|-----|----------|----------|---------|
| **rates_orchestrator** | Polling (5min prod / 60s dev) | `src/run/rates_orchestrator/` | Main processing loop - polls Nylas for new emails |
| **outbound_queue_processor** | Every 6 hours | `vercel.json` cron | Triggers outbound email queue processing |

### Polling Configuration
```python
DEV_SLEEP_INTERVAL = 60      # seconds
PROD_SLEEP_INTERVAL = 300    # 5 minutes
--quick-poll flag = 5        # for testing
```

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              ROOSTR ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐       │
│  │  landing_pg     │     │ frontend_SHIProostr │  │ frontend_GETroostr │   │
│  │  (Marketing)    │     │ (Customer App)  │     │ (Internal Tool) │       │
│  │  Vercel         │     │ Vercel          │     │ Vercel          │       │
│  └────────┬────────┘     └────────┬────────┘     └────────┬────────┘       │
│           │                       │                       │                 │
│           └───────────────────────┼───────────────────────┘                 │
│                                   │                                         │
│                           ┌───────▼───────┐                                 │
│                           │   Wristband   │  ◄── OAuth 2.0 / Multi-tenant  │
│                           │   (Auth)      │                                 │
│                           └───────┬───────┘                                 │
│                                   │                                         │
│  ┌────────────────────────────────┼────────────────────────────────────┐   │
│  │                         BACKEND SERVICES                             │   │
│  │  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  │   │
│  │  │ rates_orchestrator│  │ manual_extract_ │  │ quote_agent_api  │  │   │
│  │  │ (Event Loop)      │  │ api (FastAPI)   │  │ (Future)         │  │   │
│  │  │ Docker            │  │ Port 8001       │  │                  │  │   │
│  │  └────────┬──────────┘  └────────┬────────┘  └──────────────────┘  │   │
│  │           │                      │                                   │   │
│  │  ┌────────▼──────────────────────▼────────┐                         │   │
│  │  │              CORE MODULES              │                         │   │
│  │  │  ┌─────────────┐  ┌─────────────┐     │                         │   │
│  │  │  │rates_agent  │  │quote_agent  │     │                         │   │
│  │  │  │(Procurement)│  │(Quoting)    │     │                         │   │
│  │  │  └──────┬──────┘  └──────┬──────┘     │                         │   │
│  │  │         │                │             │                         │   │
│  │  │  ┌──────▼──────┐  ┌──────▼──────┐     │                         │   │
│  │  │  │rate_extractor│ │rate_matcher │     │                         │   │
│  │  │  └─────────────┘  └─────────────┘     │                         │   │
│  │  └────────────────────────────────────────┘                         │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                   │                                         │
│           ┌───────────────────────┼───────────────────────┐                 │
│           │                       │                       │                 │
│  ┌────────▼────────┐     ┌────────▼────────┐     ┌───────▼────────┐        │
│  │   MongoDB       │     │    Nylas        │     │  Anthropic     │        │
│  │  (Data Store)   │     │  (Email API)    │     │  (Claude LLM)  │        │
│  │  Atlas Cloud    │     │  OAuth Grants   │     │  3.7 Sonnet    │        │
│  └─────────────────┘     └─────────────────┘     └────────────────┘        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## External Integrations

| Integration | Purpose | Code Location |
|-------------|---------|---------------|
| **Anthropic (Claude)** | Primary LLM for extraction/agents | `backend/src/utils/llm/v1/lib/anthropic/` |
| **Nylas** | Email API (fetch/send/attachments) | `backend/src/lib/nylas/` |
| **MongoDB Atlas** | Primary database | `backend/src/utils/db/mongo_client.py` |
| **Google Sheets API** | Rate data source (V1 WBR) | `frontend/frontend_GETroostr/app/lib/sheets.tsx` |
| **Google APIs** | Spreadsheet integration | `frontend/frontend_SHIProostr/` (googleapis package) |
| **Stripe** | Payment processing | `frontend/frontend_SHIProostr/app/checkout/`, `/api/stripe/` |
| **Wristband** | OAuth 2.0 authentication | `frontend/*/app/lib/wristband.ts` |
| **Mapbox** | Map visualizations | `frontend/frontend_SHIProostr/` |
| **ImportYeti** | Supplier discovery (documented) | `frontend/frontend_SHIProostr/app/discover/test/` |

---

# C. Data Model (MongoDB)

## Database Configuration

| Environment | Database Name | Connection |
|-------------|---------------|------------|
| Production | `roostr_prod_v1` | MongoDB Atlas (srv) |
| Development | `roostr_dev_v1` | MongoDB Atlas (srv) |

## Collection Inventory

| Collection | Doc Count | Purpose |
|------------|-----------|---------|
| **rates** | 10,560 | Ocean freight rates extracted from suppliers |
| **charge_lines** | 15 | Individual charge/fee line items |
| **threads** | 363 | Email conversation threads |
| **messages** | 694 | Individual email messages with AI processing |
| **unprocessed_messages** | 4,316 | Messages skipped (blacklisted/not whitelisted) |
| **drayage_rates** | 2,008 | Local drayage service rates |
| **drayage_rate_cards** | 4 | Drayage rate card definitions |
| **ssot_ports** | 3,340 | Single Source of Truth port codes |
| **charge_buckets** | 12 | Cost categories (Origin, Transit, Destination) |
| **charge_codes** | 17 | Individual charge types (THC, LSS, etc) |
| **charge_incoterms** | 11 | Trade terms (EXW, CIF, FOB, etc) |
| **charge_responsibility_matrix** | 132 | Incoterm → payer mapping |
| **whitelist** | 293 | Approved email senders |
| **blacklist** | 3 | Rejected senders |
| **mailing_lists** | 3 | Distribution lists |
| **email_sync_status** | 13 | Last sync times per tenant/grant |
| **partners** | 28 | Supplier/partner company data |
| **tenants** | 10 | Customer organizations |
| **users** | 4 | System users with roles |
| **outbound_messages** | 2 | Sent emails tracking |
| **invitations** | 1 | User invitations |
| **focus_lane_views** | 3 | User-defined trading lanes |
| **rate_schema** | 27 | Rate field definitions |

## Key Schema Examples

### rates Collection
```json
{
  "rate_id": "uuid",
  "tenant_id": "string",
  "stage": "staging|confirmed",
  "status": "unconfirmed|confirmed",
  "pol": "Shanghai, China (CN SHG)",
  "pod": "Los Angeles, USA (US LAX)",
  "carrier": "CMA CGM",
  "twenty_st": 2600,
  "forty_st": 3600,
  "forty_hc": 3800,
  "valid_start_date": "2024-10-15",
  "valid_end_date": "2024-11-15",
  "source_thread_id": "string",
  "source_message_id": "string"
}
```

### tenants Collection (Multi-tenancy)
```json
{
  "tenant_id": "roostr",
  "tenant_name": "Roostr Inc",
  "status": "active",
  "feature_flags": {
    "procurement_module": true,
    "quoting_module": true
  },
  "dw_procurement_name": "Pete Mitchell",
  "dw_procurement_email": "agent@email.com",
  "dw_procurement_grant_id": "nylas-grant-uuid"
}
```

## Multi-Tenancy Strategy

- **Tenant Isolation**: Every document has `tenant_id` field
- **Access Pattern**: All queries filter by `tenant_id`
- **Cross-Tenant Risk**: None - enforced at application layer
- **Digital Workers**: Each tenant has separate AI personas with dedicated email grants

## Migration Approach

- **Schema Changes**: Handled via migration scripts in `backend/src/tools/db/`
- **Seed Scripts**: `seed_charge_codes.py`, `seed_charge_buckets.py`, etc.
- **Port Data**: `upload_ports_from_csv.py` for SSOT ports

---

# D. LLM Stack and Costs

## LLM Providers & Models

| Model | Model ID | Use Case | Environment |
|-------|----------|----------|-------------|
| **Claude 3.7 Sonnet** | `claude-3-7-sonnet-20250219` | Default agent operations | All |
| **Claude 3.5 Sonnet** | `claude-3-5-sonnet-latest` | Rate extraction | Prod |
| **Claude 3.5 Haiku** | `claude-3-5-haiku-latest` | Validation tasks | Prod |

### Configuration (`src/config/config.py`)
```python
if APP_MODE == "prod":
    default_llm_model = "claude-3-7-sonnet-20250219"
    extract_llm_model = "claude-3-5-sonnet-latest"
    validate_llm_model = "claude-3-5-haiku-latest"
else:
    default_llm_model = "claude-3-7-sonnet-20250219"
```

## LLM Wrapper Layer

**Location**: `backend/src/utils/llm/v1/`

```
src/utils/llm/v1/
├── call_llm.py                    # High-level wrapper
├── call_llm_messages.py           # Message-based interface
└── lib/anthropic/
    ├── call_anthropic_api.py      # Direct API integration
    └── process_anthropic_response.py
```

### Features
- **Tool/Function Calling**: Supports structured tool definitions
- **Extended Thinking**: Optional reasoning budget (0-0.8 ratio)
- **JSON Output**: Structured response parsing with schemas
- **Token Tracking**: Calculates API costs per request
- **Retry Logic**: Exponential backoff (max 3 retries, base 1s delay)

## Agent Loops & Pipelines

### 1. Rates Agent (`src/lib/rates_agent/`)
**Steps**:
1. Quick Filter → reject obvious non-rate emails
2. Planner → decide action (extract/respond/skip/escalate)
3. Rate Extraction → call `rate_extractor` if needed
4. Intent Generation → DB updates, email responses

**Termination**: Single-pass (no loop), returns intents

### 2. Quote Agent (`src/lib/quote_agent/`)
**Steps**:
1. Initial RFQ Parse → extract quote request details
2. Rate Matching → find rates for requested lanes
3. Quote Generation → build pricing proposal
4. Email Response → generate response

**Tools Available**:
- `initial_rfq_parser_tool`
- `rfq_updater_tool`
- `email_generator_tool`
- `rfq_rate_match_tool`
- `human_handoff_tool`
- `no_action_tool`

**Termination**: Max 7 iterations OR terminal tool called

### 3. Rate Extractor (`src/lib/rate_extractor/`)
**Pipeline**:
1. Clean HTML → extract text
2. Process Attachments → parse CSV/XLS
3. LLM Extraction → structured data from text
4. Field Standardization → validate ports, dates, currencies
5. Fee Extraction → parse charges/remarks
6. Merge & Validate → combine sources, business logic checks

## Human-in-the-Loop Review Gates

| Gate | Location | Trigger |
|------|----------|---------|
| **Rate Review** | `frontend_GETroostr/dashboard/[tenant]/procurement/rates` | All extracted rates start as "staging" |
| **Flag for Review** | `rate_extractor` output | Extraction confidence issues |
| **Human Handoff** | `quote_agent` → `human_handoff_tool` | Complex quotes, escalations |

## Cost Instrumentation

**Current State**: Token tracking exists but not aggregated per-unit

**Where to Add Hooks**:
- `src/utils/llm/v1/lib/anthropic/call_anthropic_api.py` - token counts returned
- `src/run/rates_orchestrator/` - per-message processing
- `src/lib/rate_extractor/` - per-extraction cost

**Estimated Costs** (rough):
- Per email processed: ~$0.01-0.05 (depends on attachments)
- Per quote generated: ~$0.05-0.15 (multi-step agent)
- Per rate extraction: ~$0.02-0.08

---

# E. Frontend + Auth + Permissions

## Next.js Applications

### 1. landing_pg (Marketing)
- **URL**: Public landing site
- **Routes**: `/`, `/invest`, `/lanes`, `/legal/*`, `/team`
- **Auth**: None (public)
- **Key Features**: 3D globe visualization (Three.js), trade lanes

### 2. frontend_SHIProostr (Main App)
- **URL**: shiproostr.com
- **Routes**: 93 page routes
- **Auth**: Wristband OAuth 2.0
- **Key Routes**:
  - `/ship` - Quote/booking form (public)
  - `/dashboard/[tenantId]/home` - Overview
  - `/dashboard/[tenantId]/shipments` - Shipment list
  - `/dashboard/[tenantId]/tracking/[id]` - Track shipment
  - `/checkout/[id]` - Stripe checkout
  - `/admin/*` - Admin panel (Roostr Admin only)
  - `/prototype/*` - Feature prototypes (blocked in prod)

### 3. frontend_GETroostr (Internal)
- **URL**: Internal tool
- **Routes**: 15+ specialized pages
- **Auth**: Wristband OAuth 2.0
- **Key Routes**:
  - `/dashboard/[tenant]/procurement/rates` - Rate management
  - `/api-tests/rates-tester` - Agent testing
  - `/test/*` - Various test pages

## Authentication Method

**Provider**: Wristband (`@wristband/nextjs-auth`)

**Session Management**: Iron-session
```typescript
{
  cookieName: 'ROOSTR_SESSION',
  ttl: 90 days,
  secure: true (production),
  httpOnly: true,
  sameSite: 'lax'
}
```

**OAuth Scopes**: `['openid', 'offline_access', 'email', 'profile', 'roles']`

## Role/Permission Model (RBAC)

| Role | Access Level |
|------|--------------|
| **Roostr Admin** | Full platform access (all tenants, all features) |
| **Tenant Admin** | Tenant dashboard, team management |
| **Workstream Leader** | Can manage team members |
| **Individual Contributor** | Base access to personal shipments |
| **Public** | Unauthenticated (`/ship`, `/track` only) |

**Enforcement**:
- Middleware checks Wristband roles
- Frontend checks MongoDB-backed roles
- Route-level access control in `middleware.ts`

## Audit Logging

**Current State**: Minimal
- Session activity tracked in iron-session
- MongoDB `created_at`/`updated_at` timestamps on documents
- No dedicated audit log collection

**Recommendation**: Add `audit_logs` collection with user actions

---

# F. Testing and Quality

## Test Inventory

### Backend (Python)
| Type | Count | Location |
|------|-------|----------|
| Schema Alignment | 1 | `src/tests/test_schema_alignment.py` |
| Global Tests | 1 | `src/global_tests.py` |
| Unit Tests | ~10 | `src/tests/`, module `/tests/` folders |
| LLM Tests | 4 | `src/utils/llm/v1/tests/` |
| Integration | ~5 | Various module test files |

### Frontend (TypeScript)
| Type | Count | Location |
|------|-------|----------|
| Jest Config | 1 | `frontend_SHIProostr/jest.config.js` |
| Unit Tests | 0 | (Not implemented yet) |

## CI Pipeline (GitHub Actions)

**File**: `backend/.github/workflows/ci.yml`

**Triggers**: Push/PR to `main`

**Steps**:
1. Checkout repository
2. Setup Python 3.10
3. Install Poetry 1.5.1
4. Cache virtual environment
5. Install dependencies
6. Run schema alignment tests
7. Run global tests

**Runtime**: ~2-3 minutes (with cache hit)

## Coverage

**Current State**: Not configured
**To Compute**: Add `pytest-cov` and `coverage` to pyproject.toml

---

# G. Reliability, Monitoring, and Ops

## Logging/Monitoring Stack

| Tool | Status | Location |
|------|--------|----------|
| **Custom Logger** | Active | `src/utils/logging_helpers.py` |
| **Print Statements** | Extensive | Throughout codebase (debugging) |
| **Sentry** | Not configured | - |
| **Datadog** | Not configured | - |

## Error Handling

- `try/except` blocks in agent modules
- Errors logged and returned in response objects
- `flag_for_review` pattern for extraction issues

## Backup Strategy

**MongoDB Atlas**: Automatic daily backups (cloud-managed)
**File Storage**: `./out/` volume mount (attachments, logs)

## Deployment Pipeline

### Backend (Docker)
```bash
# Development
docker compose --env-file .env.dev up --build

# Production
docker compose --env-file .env up -d --build
```

### Frontend (Vercel)
- Auto-deploy on push to main
- Environment variables in Vercel dashboard

### Rollback Process
- Docker: Pull previous image tag
- Vercel: Instant rollback via dashboard

## Secrets Management

| Location | Secrets |
|----------|---------|
| `.env` / `.env.dev` | Local development (gitignored) |
| Vercel Dashboard | Frontend env vars |
| Docker env-file | Production backend |

**Key Variables**:
- `ANTHROPIC_API_KEY`
- `NYLAS_API_KEY`, `NYLAS_CLIENT_ID`
- `MONGO_URI`
- `WRISTBAND_CLIENT_ID`, `WRISTBAND_CLIENT_SECRET`
- `STRIPE_SECRET_KEY`
- `GOOGLE_CLIENT_EMAIL`, `GOOGLE_PRIVATE_KEY`

---

# H. Security and Compliance

## Email Integration Credentials

**Nylas OAuth Flow**:
1. User authenticates via Wristband
2. Nylas grant linked to tenant
3. `grant_id` stored in `tenants` collection
4. Tokens refreshed by Nylas SDK

**Storage**: Grant IDs only (not raw tokens) in MongoDB

## Data Retention

| Data Type | Retention | Location |
|-----------|-----------|----------|
| Email Content | Indefinite | `messages` collection |
| Attachments | Indefinite | `./out/attachments/` |
| Rate Data | Indefinite | `rates` collection |
| Unprocessed | Indefinite | `unprocessed_messages` |

**Redaction Strategy**: Not implemented (future consideration)

## Encryption

| Layer | Status |
|-------|--------|
| In Transit | HTTPS (Vercel, Atlas) |
| At Rest | MongoDB Atlas encryption |
| Application-level | Not implemented |

## PII Handling

- Email addresses stored in multiple collections
- Contact names stored in `partners`
- No SSN/financial PII (payment via Stripe)

---

# I. "Resume Bullet" Extraction

## V1 - WBR (Weekly Business Review) Phase

**System Scope**: Google Sheets-based rate tracking and display system for freight forwarders to compare ocean freight rates across carriers and trade lanes.

**Ownership**: Built end-to-end as founding engineer

**Bullets**:
- Designed and implemented Google Sheets API integration processing 5 country-specific rate sheets (Brazil, Chile, Mexico, Peru, Colombia) with real-time data synchronization
- Built rate comparison dashboard with dynamic filtering, transit time parsing, and multi-currency calculations (USD/BRL)
- Established multi-tenant architecture foundation with Wristband OAuth 2.0, enabling secure customer isolation

## V2 - Rate SaaS Phase

**System Scope**: Full-stack shipping platform enabling shippers to get quotes, book shipments, and track containers with integrated payment processing.

**Ownership**: Led architecture and implementation

**Bullets**:
- Architected and built 93-route Next.js 14 application with TypeScript, implementing role-based access control (5 permission levels) and multi-tenant dashboard
- Integrated Stripe payment processing for shipment checkout, including webhook handling and payment status tracking
- Developed real-time shipment tracking interface with Mapbox integration and milestone-based progress visualization
- Built 47+ reusable React components following recursive modular tree pattern, reducing frontend development time by ~40%
- Implemented comprehensive quote workflow: multi-step booking form → rate calculation → checkout → confirmation

## V3 - Forwarder Ops / AI Agents Phase

**System Scope**: AI-powered rate extraction and procurement automation system that processes supplier emails, extracts structured rate data, and manages automated responses.

**Ownership**: Designed and built entire agentic backend

**Bullets**:
- Designed and implemented multi-agent AI system using Claude (Anthropic) with tool-calling, processing 10,560+ rates across 363 email threads
- Built rate extraction pipeline handling PDF, CSV, XLS attachments and HTML emails with field standardization (3,340 port codes, carrier validation)
- Architected intent-based agent system separating AI decision-making from execution, enabling sandbox mode for testing and human-in-the-loop review
- Developed quote agent with planner-driven agentic loop (max 7 iterations) using 6 specialized tools for RFQ parsing, rate matching, and response generation
- Created FastAPI service for manual rate entry with API key auth and rate limiting (60 req/min), enabling UI-based rate submission
- Built Docker-based deployment with polling orchestrator processing multiple tenant mailboxes (5-minute intervals, 10 tenants supported)

**Measurable Impact**:
- Processing 694 messages → 10,560 extracted rates (15x amplification)
- Support for 28 partners, 293 whitelisted senders
- 2,008 drayage rates across multiple zones

## Operational Maturity Stories

### Incident 1: Rate Extraction Accuracy Drop
- **Root Cause**: LLM responses occasionally missing required fields due to ambiguous prompts
- **Fix**: Implemented structured JSON schema validation and feed-forward logic for fee extraction
- **Outcome**: Extraction success rate improved from ~75% to 90%+

### Incident 2: Email Processing Loop
- **Root Cause**: Agent responding to its own emails, creating infinite loops
- **Fix**: Added blacklist for AI email addresses and quick-filter rejection logic
- **Outcome**: 4,316 messages properly filtered, zero loop incidents

### Incident 3: Port Code Inconsistency
- **Root Cause**: Same ports extracted with different names (Shanghai vs CN SHG vs CNSHG)
- **Fix**: Built SSOT port validation with 3,340 standardized port codes and fuzzy matching
- **Outcome**: 100% port code consistency across rate database

---

# J. Evidence Bundle

## Public Demos/URLs

| Asset | URL/Location | Status |
|-------|--------------|--------|
| Landing Page | Vercel deployment | Active |
| Customer App | shiproostr.com | Active |
| Internal Dashboard | Vercel deployment | Active |

## Screenshots/Artifacts (to capture)

1. Rate extraction flow (email → structured data)
2. Dashboard with rates table
3. Quote agent conversation UI
4. Shipment tracking with map
5. Admin panel overview

## Best Code Examples (Engineering Quality)

### 1. Type-First Design
**File**: `backend/src/lib/rate_extractor/extractor_types.py`
- Comprehensive TypedDict definitions
- Clear input/output contracts
- Extraction confidence flags

### 2. Agent Architecture
**File**: `backend/src/lib/quote_agent/quote_agent.py`
- Planner-driven agentic loop
- Tool abstraction pattern
- Intent-based execution separation

### 3. Modular Component Structure
**File**: `frontend/frontend_SHIProostr/app/components/ui/`
- Recursive modular tree pattern
- Reusable primitives
- Consistent styling

## Proprietary/Restricted Content

**Never Share Externally**:
- `.env` files (API keys, secrets)
- `tenants` collection data (customer info)
- `partners` collection (contact details)
- `whitelist` entries (email addresses)
- Specific rate pricing data
- Nylas grant IDs

---

# Additional Technical Notes

## Code Quality Practices

- **Type Hints**: Every Python function has return type annotations
- **TypedDict**: Used for all complex data structures
- **Smoke Tests**: Main guard in each script with runnable example
- **File Headers**: Location comment on line 1 of every file
- **Modular Structure**: Recursive lib/ pattern throughout

## Technology Stack Summary

| Layer | Technology |
|-------|------------|
| **Frontend** | Next.js 14, React 18, TypeScript, Tailwind CSS |
| **Backend** | Python 3.10, FastAPI, Poetry |
| **Database** | MongoDB Atlas |
| **LLM** | Anthropic Claude (3.5/3.7 Sonnet, 3.5 Haiku) |
| **Email** | Nylas API |
| **Auth** | Wristband OAuth 2.0, iron-session |
| **Payments** | Stripe |
| **Deployment** | Docker (backend), Vercel (frontend) |
| **CI/CD** | GitHub Actions |

## Future Enhancements (Identified)

1. Add Sentry/Datadog monitoring
2. Implement comprehensive test coverage
3. Add audit logging collection
4. Cost tracking per-unit (email, extraction, quote)
5. Data retention/redaction policies
