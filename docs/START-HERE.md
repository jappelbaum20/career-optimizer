# Start here

## Before you begin

You need a ChatGPT account with plugin/skill access, and a Notion account for your career databank. Live job searches need web access. Automatic daily or weekly searches also need the host's scheduling feature. Access varies by plan and workspace; the assistant checks what is actually available.

No developer account, local Python, API key or server is needed for normal use. You sign into Notion through the official connection flow. This package adds the career workflow; connect Notion separately.

## 1. Install

Download the plugin ZIP from [Releases](https://github.com/jappelbaum20/career-optimizer/releases/latest). Open [ChatGPT Plugins](https://chatgpt.com/plugins) and use the ZIP upload option when available. Enable the plugin and select Career Optimizer from the `@` menu in a new chat.

If your account does not offer ZIP import, use a supported Work/desktop plugin surface or ask your workspace administrator about custom plugins. Desktop/Codex users can add the repository marketplace as shown in the README. Simply uploading the ZIP as a conversation attachment is not a plugin installation.

If you already have an older copy, use the host's update/reinstall flow, then start a new chat and verify the version. Do not delete your Notion databank.

## 2. Start intake

Say: **“Set up Career Optimizer for me, one step at a time.”**

The assistant will guide you through:

1. Your goal and quick/full intake preference.
2. A private Notion workspace, new or existing.
3. Career basics and verified chronology.
4. Projects, achievements and personal contribution.
5. Target jobs and hard constraints.
6. Writing preferences and confidentiality.
7. A useful first result and optional job-search schedule.

You can say **skip**, **later**, **correct that**, or **resume my setup**. A CV, LinkedIn export or old letter helps but is optional. You can also say “I need a letter now; finish setup later.”

## 3. Connect Notion

Use the official Notion app/plugin connection in ChatGPT. Sign into your own Notion account and give it access to your chosen private career area. Never share your password or API token in chat.

Tell the assistant whether to create a new private Career HQ or reuse an existing page, and provide the existing page link when applicable. It will create or map the Profile, Experience, Opportunities and Activities resources, save their links and verify the results. It will ask before using an ambiguous or unexpectedly shared destination.

The assistant should return a working Career HQ link. Open it and check the Profile and databases. If tools cannot create databases, the included schema provides a manual Notion setup path. Without a connection, intake can continue in chat, clearly marked unsaved.

## 4. Choose regular searches

After a successful first scan, say, for example:

> Search for matching jobs every weekday at 08:00 Europe/London. Save new matches to my Career HQ and notify me only about useful new roles, important changes or upcoming actions.

Or:

> Give me a weekly job digest each Monday at 09:00 Europe/Zurich, with up to five matches and application follow-ups.

These are examples, not your defaults. Choose your own timezone, cadence and scope. The assistant should report **active** only after the host confirms a real task. Review its next run and first actual result in **Scheduled**. A prompt, a Notion entry or a promise alone is not an active schedule.

If scheduling isn't available, ask for the completed task prompt and run it manually, or create it in a supported ChatGPT Scheduled interface. It remains **not scheduled** until the host confirms activation. Cloud/web tasks use accessible connected sources; local desktop tasks may require the app and computer to remain running.

To change it, say **“Make my digest weekly”**, **“Change my timezone to…”**, or **“Pause my job searches.”** Check that the actual scheduled task changed; editing a Notion preference alone does not pause it.

## 5. Use it day to day

- “Is this role a good fit?” followed by a posting URL or text.
- “Tailor my CV using my Profile and Experience records.”
- “Log this project; I supported the rollout but did not lead it.”
- “I submitted my application for [company and role] today.”
- “Run a mock interview, one question at a time.”
- “Compare these offers, separating guaranteed pay from bonus and equity.”

Original documents remain preserved. Generated downloads should be saved to your chosen durable folder; a temporary chat link is not a permanent archive.

## Troubleshooting

| What happens | What to do |
|---|---|
| Plugin absent from `@` menu | Check installation/enabled state and workspace permission; refresh or start a new chat |
| Notion page cannot be found | Provide its exact URL and check connection access; don't create duplicates blindly |
| Setup stopped partway | Say “Resume setup” with the HQ link; existing confirmed resources should be reused |
| Save failed | Keep the unsaved handover, restore connection, then reconcile it with the current HQ |
| Schedule is only proposed | Complete activation in the host; verify status and next run |
| Scan has no results | Read coverage: no matches, source failure and missing connection are different outcomes |
| Duplicate job or wrong fact | Give the exact record and correction; preserve history and update the existing entry |
| Moving to a new chat/device | Use the same connected account and provide the HQ URL if it is not discoverable |

## Final personal check

Confirm the assistant can read your correct HQ, save and read back one real authorized record, find a current posting, and distinguish a draft from a submitted application. If you enable scheduling, review the first unattended run before relying on it.
