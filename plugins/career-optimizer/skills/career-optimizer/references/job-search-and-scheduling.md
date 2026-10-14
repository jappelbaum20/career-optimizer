# Job searches and scheduled follow-through

## Run a useful manual scan

Read the Profile's current search preferences and relevant Opportunities before searching. If role/location/hard constraints are too vague to rank usefully, ask the smallest missing question. In an unattended run, use the last confirmed configuration and flag missing essentials instead of silently broadening it.

1. Build a bounded search plan: priority employer career pages, relevant job boards and the user's keywords/locations. Default to screening up to 20 plausible postings and reporting up to 5 strong or possible fits; adapt limits to explicit preferences. A scan is a scoped sample, never “all available jobs.”
2. Use current web/search tools and open the actual posting where accessible. Prefer employer originals. Record source, checked date, stated location/remote restrictions, required qualifications and explicit deadlines. A search snippet alone is unverified; a blocked page is not proof of closure. Do not invent posted dates, salary, sponsorship or availability.
3. Apply confirmed hard filters first. Separate an explicit mismatch from an unknown requirement. Rate Strong / Possible / Stretch / Excluded / Unknown with a short evidence rationale; do not invent ATS scores or hiring probabilities. User-requested exploratory/stretch searches remain valid.
4. Deduplicate against Opportunities using [Notion rules](notion-schema.md). Exclude already applied, declined or previously surfaced unchanged roles from the new-jobs section. A material change (deadline, scope, location, reopened role) may be resurfaced with its change explained. A repost with a new ID is reviewed as a possible duplicate, not automatically a new opportunity.
5. Save only within the agreed scan scope. New candidates start Discovered; existing user Status is preserved. Update Last Checked and Availability from evidence. Keep deadline unknown if not stated. Store a short JD summary for future use if the page disappears.
6. Return up to the configured number of useful roles: role/company, location, fit reason, material gap/unknown, verified deadline if present, source link. Lead with the best next action; include coverage limitations. Zero suitable roles is a valid result; don't pad with excluded ones.

## Configure daily or weekly searches

Scheduling is optional and belongs to the recipient's host, not this ZIP. Installing the skill does not create a task. A request to run one scan is not recurring authorization.

When the user asks to schedule or selects a cadence, collect only missing choices:
- Daily (every day or weekdays) or weekly (which day).
- Local time and IANA timezone; confirm a concrete next-run time, including daylight-saving interpretation provided by the host. Do not infer the timezone from language or desired job location.
- Digest scope: roles only, or roles plus due applications/follow-ups.
- Notifications: default meaningful new/changed matches, imminent deadlines or actionable failures only; an every-run digest is available if requested.
- Destination (current chat by default where supported) and authorization to save scan results in the selected Career HQ.

Offer a weekly morning scan as a suggestion, never as a silently activated default. Example wording: “Weekly Monday at 09:00 in your timezone, with up to five new matches and upcoming actions.” Ask for missing timezone/time rather than inventing them.

### Activation procedure

1. Discover the host's actual scheduling tools and inspect existing tasks if available. Match by HQ URL + workflow purpose; update an existing matching task instead of making a duplicate. Ambiguous matches need resolution. A tool cannot be assumed available just because the skill mentions it.
2. Test the configured scan in a regular chat. Use this result to verify source access, Notion permissions and digest usefulness. A recent equivalent successful scan can serve as the test. Fix blockers before declaring scheduling ready.
3. Prepare a self-contained task prompt from [the template](../assets/scheduled-job-search.txt), replacing every bracketed field with the recipient's confirmed values and real HQ URL. No dependency on a local folder, temporary upload URL or private detail unnecessary for the search. Invoke this skill explicitly in the host-supported form.
4. With the user's scheduling authorization, create/update the actual task. Use the correct tool schema and timezone handling. If it returns a suggestion requiring user activation, label it proposed until activated. A Notion reminder or calendar entry is not equivalent to an executing job-search task.
5. Read back the scheduler result: task ID, active/paused state, configured cadence/timezone and next run if available. On timeout or unknown outcome, inspect the existing task before retrying. For an uncertain creation, search by HQ URL and purpose; if it cannot be reconciled, leave activation pending rather than creating a replacement. Save the receipt in HQ; if that save fails, report “task active, HQ receipt not saved” and keep the task ID for recovery. Do not create a second task to repair a receipt.
6. Return the verified schedule and how to view/pause it. Review the first actual run when the user returns; do not claim unattended success from a manual test.

If scheduling isn't available on the plan/surface, give the filled prompt and plain-language cadence, instruct the recipient to use ChatGPT's Scheduled interface where available, and state **not scheduled**. If Notion isn't writable, the scan may run read-only only when the user explicitly accepts it; explain that persistent deduplication/learning is reduced. Never claim continuous background work from a conversation alone.

## Each unattended run

- Re-read HQ and Profile; respect off/paused configuration and changed preferences. Check that the scheduler task matches this HQ. If HQ is inaccessible, stop writes and report a connection failure, not “no jobs.”
- Use a stable run key (task ID + scheduled occurrence/timezone). Check ledger for completed/running runs; reconcile unknown outcomes before retries. Do not overlap writes; see Notion concurrency limitations.
- Search from the last fully completed cutoff with a small overlap to catch delayed postings, or use the user-defined lookback on the first run. Undated postings can be new discoveries but are not labelled newly posted.
- Record coverage per source. On partial search failure, retain useful verified results, record partial status, and do not advance the global complete cutoff. Next run retries failed coverage and deduplicates previously saved results.
- Record result IDs and delivery state. Mark Last Surfaced only when the host confirms delivery, or as part of preparing the final response when no receipt exists with delivery explicitly recorded as unconfirmed. An uncertain notification is not grounds to send repeated duplicates; reconcile on the next run.
- For unchanged/non-actionable results, stay quiet if that was selected and supported by the host. Keep a run receipt in Notion. If the host always emits a result, report a brief no-change result and disclose that notification suppression is host-controlled.
- Notify on meaningful matches/changes, approaching agreed deadlines, or actionable access failures. Never submit applications, contact recruiters, accept offers or send messages to third parties.

## Reminders, changes and stopping

Upcoming actions use actual Deadline/Next Action On/Due On dates. Ask once for an unknown due date; don't infer a deadline from a posting age. Follow-up timing follows employer guidance or the user's preference; elapsed time is a suggestion, not permission to send.

For “pause,” “stop,” “change to weekly,” or a new timezone, locate the actual scheduler task and perform the requested change, then verify it and update HQ. Changing HQ alone does not pause a scheduler. If the scheduler cannot be reached, mark the request pending and give the manual pause path; do not say stopped. Preserve history. If the user accepts a job, ask whether to pause remaining scans rather than assuming all career work should stop.
