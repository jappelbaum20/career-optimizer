# Career Optimizer

A reusable ChatGPT plugin for your own career: guided intake, a private Notion career databank, job discovery, CVs, applications, interviews, networking and offers.

**[Download the plugin ZIP](https://github.com/jappelbaum20/career-optimizer/releases/latest)** · **[Start here](docs/START-HERE.md)**

## What it does

- Guides new people through seven short, resumable onboarding steps. A CV is optional, and urgent work can start before full setup.
- Creates or reuses a private Notion Career HQ with a Profile page and Experience, Opportunities and Activities databases. Documents tracking is optional.
- Helps configure daily, weekday or weekly job searches, with deduplication, current source checks, useful notifications and pause/change support.
- Supports truthful CV and LinkedIn writing, tailored letters, fit analysis, project logging, application tracking, mock interviews, negotiation and search reviews.
- Keeps each recipient's personal information in their own workspace. There are no bundled personal profiles, account identifiers, API keys or local-machine requirements.

## Install in ChatGPT

1. Download **Career-Optimizer-3.0.0.zip** from the release, rather than GitHub's source-code ZIP.
2. Open ChatGPT's **Plugins** area and use its ZIP upload/add option if available for your account. Upload the ZIP as a plugin, not as an ordinary chat attachment. Review and enable it.
3. Connect the official **Notion** app/plugin using your own Notion account and the destination you want to use. The ZIP does not include a Notion server or inherit anyone else's connection.
4. Start a new chat, select **Career Optimizer** from the `@` menu, and say:

   > Set this up for me step by step. Help me create a private Notion Career HQ, build my profile and choose whether to enable daily or weekly job searches.

Installation options depend on plan, workspace permissions and surface. If the ZIP option is absent, check with your workspace administrator or use a supported Work/desktop plugin installation surface. Do not treat attaching the ZIP to a chat as installation. [Full setup and fallback guide](docs/START-HERE.md).

### Codex / desktop repository marketplace

```text
codex plugin marketplace add jappelbaum20/career-optimizer --ref v3.0.0
```

Open the Plugins Directory, choose this source and install Career Optimizer. Restart/refresh if it is not shown. This is an alternative install path; it does not activate Notion or schedules by itself.

## Models and capabilities

Designed for GPT-6.1 Sol and newer capable instruction-following models. Instructions are outcome-based, load only relevant workflows and avoid fixed model IDs in runtime settings. The plugin cannot select a model, add unavailable tools or guarantee future-model behavior. Select your preferred available model in ChatGPT.

Notion read/write tools are required for the databank; current web search is required for live job discovery; host scheduling is required for recurring execution; document tools are needed for native file outputs. Basic coaching and copyable drafts can continue without those connections. Each missing capability is reported honestly.

## Privacy and actions

No custom server, telemetry, install hooks or background executable is included. Career data is processed by the host and the connected services you authorize. Keep Career HQ private unless you deliberately choose a shared destination. Sensitive salary and personal details are optional. Do not paste credentials into chat.

The assistant drafts applications and messages. It does not automatically apply, send outreach, change a public profile or accept offers. Scheduling requires your request and a verified task-creation result. Installing an update preserves your Notion records.

## Release and verification

Version 3.0.0 redesigns the supplied Career Optimizer v2 template for reusable plugin distribution. See [changes](CHANGELOG.md), [validation](docs/VALIDATION.md) and [compatibility sources](docs/COMPATIBILITY.md).

This repository and release are GitHub distribution, not publication in OpenAI's public plugin directory. Recipient-account ZIP installation, live Notion setup and unattended schedule execution require validation in that account.
