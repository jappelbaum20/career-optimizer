# Compatibility and design evidence

Checked 2026-10-14 against official documentation:

- [Package your plugin](https://developers.openai.com/plugins/build/plugins): root `plugin.json` with the Agent Plugins schema, skills under `skills/`, OpenAI presentation in `extensions.com.openai`, and repository marketplace layout. No MCP server, hooks or secret-bearing configuration is bundled.
- [Build skills](https://learn.chatgpt.com/docs/build-skills): skill entrypoint/frontmatter, progressive resources and UI metadata.
- [Plugins](https://learn.chatgpt.com/docs/plugins): installation and available surfaces are account/workspace dependent.
- [Scheduled tasks](https://learn.chatgpt.com/docs/automations): tasks can use skills and connected tools; web tasks cannot depend on local folders; test before scheduling and inspect actual runs.
- [GPT-6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol) and [GPT-6 guidance](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6.1-sol): explicit outcomes, scoped autonomy, instruction auditing and proportionate verification. The family prompting guide describes Astra-observed behaviors and says to evaluate on the chosen model; it is not evidence of a Sol-specific performance gain.

The new structure uses a short entrypoint, focused references, capability discovery and recoverable state. It does not set a model, reasoning effort or API parameter. Future model compatibility is not guaranteed without a fresh test.

Notion schema mechanics were checked against the currently exposed Notion connector descriptions (database creation, page creation, fetch and data-source querying). Runtime instructions require reading the recipient's actual tools and schema. No live personal database was created for development testing.

Publishing a GitHub release is distinct from submission/review in the OpenAI public plugin directory. No directory approval or installation in a recipient account is claimed.
