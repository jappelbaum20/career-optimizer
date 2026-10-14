# Notion databank: setup, schema and recovery

## Resolve the right workspace

Use the connected Notion tool's access discovery if provided; inspect read, search, create, update, query and view capabilities and restrictions. Search narrowly for the supplied HQ or “Career HQ”; read the selected page before writing. Confirm ownership/destination if ambiguous. No search results, a limited search or a permission failure do not prove absence.

For new setup, create **Career HQ — [preferred name]** in the user's selected private parent, or a private root/draft where the host supports it. Explain if the chosen parent is shared; never change sharing settings automatically. Follow the tool's current content format and creation instructions. Do not assume a database ID is its data source ID. Fetch each database to obtain current schema and data source IDs before row writes or queries.

## Small core, optional depth

Create the Profile page and three databases below. Add Documents only when file tracking is useful. Put contacts and interviews in Activities initially; split them later only if the user needs it. Name changes are fine: the resource map, not a hard-coded title, identifies the sources. Existing compatible databases can be reused. Schema version: 1.

### Career HQ page

- **Purpose and owner:** career objective, preferred name, private/shared scope as observed.
- **Resource map:** Profile page URL; each database URL and data source ID; property-name mappings if reusing an existing schema; optional document folder link.
- **Setup:** onboarding states and current step, deferred topics, outstanding conflicts, storage consent and exclusions.
- **Search configuration:** roles, hard filters and preferences live in Profile; link to them rather than maintaining a second editable copy. Record schedule cadence/time/timezone, notification policy, scan limits, scheduler task ID, state, next run, and last verified date.
- **Run ledger:** run key, started/finished at, per-source coverage, completed/partial/failed, last complete search cutoff, result counts, delivered opportunity IDs, errors and pending operations. Keep recent entries here; archive older entries to a linked page when size affects retrieval.
- **Change/migration receipts:** old-to-new ID map, counts and pending items. Never store secrets here.

### Profile page (prose sections)

1. Current goal, preferred name, language and optional document contact details.
2. Verified role chronology, exact official titles, education and certifications with status/dates; evidence source and last confirmation date.
3. Search preferences: ranked roles/sectors, seniority, locations/remote/travel, timing, work eligibility if relevant, hard filters vs flexible preferences, optional compensation target/currency/period. Blank means unknown, not zero or unconstrained.
4. Evidence-backed strengths, transferable skills, known gaps; links to Experience.
5. Voice and document conventions: language/spelling, approved sample, format preferences, master document/source links.
6. Disclosure rules: what may be named, sensitive figures, approved generic wording, confidentiality exceptions explicitly confirmed by the user.
7. Storage preferences and review date. Current salary, health/family context and other sensitive details are not required; save only with explicit opt-in.

### Experience database

| Property | Type | Purpose |
|---|---|---|
| Name | Title | Project, role achievement or story |
| Record Key | Text | Stable import ID or locally assigned unique key |
| Type | Select: Project, Achievement, Story | Retrieval |
| Employer / Role | Text | Role at time |
| Period | Date range | Approximate dates may remain in page prose |
| Skills | Multi-select | User-evidenced skills |
| Evidence State | Select: User confirmed, Source supported, Needs confirmation | Reliability, not a performance grade |
| Disclosure | Select: Approved wording only, Private, Needs review | Default Needs review |
| Source | URL | Evidence when a durable URL exists |
| Last Reviewed | Date | Recency |

Page body: context, personal responsibility, actions, outcomes, scale/metrics with provenance, team vs individual attribution, approved public wording, restrictions, uncertainties, optional STAR story and competency tags. Qualitative evidence is valid. Never convert a guessed metric into a confirmed field.

### Opportunities database

| Property | Type | Purpose |
|---|---|---|
| Name | Title | Company — role |
| Record Key | Text | Deduplication key |
| Company | Text | Employer |
| Role | Text | Posting title |
| Requisition ID | Text | Employer's ID, if known |
| Source URL | URL | Canonical posting |
| Location | Text | Location(s), remote eligibility |
| Status | Select: Discovered, Saved, Drafting, Ready, Applied, Interview, Offer, Accepted, Rejected, Withdrawn, Closed | User workflow state |
| Availability | Select: Verified open, Unverified, Closed | Separate posting availability from application progress |
| Fit | Select: Strong, Possible, Stretch, Excluded, Unknown | Evidence-based judgment, not a hiring probability |
| First Seen | Date | First discovery |
| Last Checked | Date | Source verification date |
| Posted | Date | Source date only |
| Deadline | Date | Explicit deadline only |
| Applied On | Date | Confirmed submission |
| Next Action | Text | Agreed next step |
| Next Action On | Date | Agreed due date |
| Last Surfaced | Date | Digest delivery deduplication |

Page body: short JD snapshot/summary with source/date; requirements and evidence matches; unknown hard filters; stated pay with currency and period; strengths/gaps; user preference signals and explicit rejection reasons; document version links; status history and activity links. Compensation absent from a posting stays unknown. Never overwrite user-maintained Status during a scan. “Closed” availability does not imply rejection of an existing application.

### Activities database

| Property | Type | Purpose |
|---|---|---|
| Name | Title | Event, contact note, interview or follow-up |
| Record Key | Text | Stable key for safe retries |
| Type | Select: Contact, Interview, Follow-up, Status change, Review | Activity type |
| Opportunity | Relation to Opportunities, or URL if unsupported | Linked application |
| Occurred On | Date | Event date, when known |
| Due On | Date | Future action |
| State | Select: Planned, Done, Cancelled | Execution state |
| Contact | Text | Name/role only when needed |
| Outcome | Text | Confirmed result |

Page body: context, source/user report, interview questions and debrief, draft-message links, confirmed sent/submitted receipt if applicable, next step. Creating a draft does not make State Done for a sending task.

### Optional Documents database

Name (Title), Kind (Select: CV, Letter, Portfolio, Certificate, Other), Version (Text), Source URL (URL), Opportunity (Relation or URL), Created On (Date), State (Select: Draft, Reviewed, Final), Notes (Text). Track durable files in a user-selected connected folder; a temporary chat download is labelled temporary, not permanent storage. Preserve source templates and earlier approved versions.

## Create and verify in sequence

1. Read the current HQ/resource map. If creating, create HQ once and persist its returned link before dependent operations.
2. Create or resolve Profile. Create Experience and Opportunities; capture returned IDs. Create Activities after Opportunities so its relation points to the actual data source. Documents is optional.
3. Build properties with the currently exposed tool schema. Text fallback for unsupported select/relation/view features is acceptable if documented in the map. Do not invent REST endpoints, tokens, connector IDs or unsupported API parameters.
4. Record actual resource IDs and property mappings in HQ after each successful operation. If an asynchronous tool returns a pending job, wait for success and fetch its result before dependent work.
5. Fetch schemas and read back the saved profile/checkpoint. Confirm the expected properties and mappings. Verify a real authorized first Experience/Opportunity record by reading it back; do not create fake career entries merely to test.
6. Create optional views if supported: open opportunities, upcoming actions, interviews, unresolved evidence. If view creation is unavailable, give the equivalent filter/sort instructions for the UI; core setup still works.

## Writes, duplicates and errors

- Before create, look up Record Key and relevant source key in the correct data source. For opportunities prefer employer + requisition ID; otherwise canonical URL without tracking parameters. Preserve identity-bearing query parameters. If neither exists, compare company + normalized title + location and flag uncertain duplicates instead of blindly merging.
- A missing search match after limited results is not proof of absence. Follow pagination/cursors until the relevant result set is complete, or report deduplication as incomplete and stop dependent writes. For queries use the fetched schema/property names; bind untrusted text where supported.
- Re-fetch before updating existing records. Patch only the authorized fields; preserve status, notes and richer user corrections. Do not replace an entire page with a stale summary.
- After a timeout or unknown create outcome, search/re-read by key and parent before retrying. If existence remains uncertain, stop that mutation and record it as pending. Do not manufacture duplicate HQs or opportunities.
- A partial setup resumes from verified resources; missing pieces are retried, existing pieces reused. A failed save does not undo already verified writes. Return saved links and unsaved items separately.
- Serialize writes within a run. Overlapping scans use the same run key and check for a running ledger entry. Notion provides no assumed atomic lock/uniqueness guarantee: if concurrent execution cannot be excluded, defer the later run and report the limit.
- Permission loss, quota restriction or unsupported querying: preserve the last confirmed state, provide an unsaved summary, and ask only for the smallest connection/manual action needed. Do not broaden workspace permissions automatically.

## Manual setup fallback

Guide the recipient to create a private Notion page named Career HQ and a child Profile page. Add three full-page table databases with the properties above (select options can be pasted as listed). Add links to each in HQ. They can paste the Profile and Setup sections from the current intake summary. Relations can start as ordinary links. Then have them connect/share only this area with their Notion app and provide the HQ URL. Fetch and verify it before claiming connection or saving further data.

Export or deletion requests operate only on the identified person's workspace and explicit scope. A plugin update never resets or migrates user records silently; inspect schema version and propose additive changes while preserving existing data.
