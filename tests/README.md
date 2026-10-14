# Development checks

Install PyYAML and jsonschema into a disposable environment, then run:

```text
python scripts/validate_and_package.py --negative-tests --output dist
```

The bundled manifest schema is from https://agent-plugins.org/schemas/1.0.0/plugin.schema.json, retrieved 2026-10-14. It validates portable manifest fields. OpenAI extension checks are focused local checks, not an official host importer certification.

The script checks skill YAML, version consistency, reference containment/existence, an instruction-only runtime allowlist, common secret/local-path patterns and the marketplace path. Negative fixtures exercise invalid metadata, a missing reference and a private local path. ZIP construction is deterministic and round-tripped byte-for-byte.

Behavioral simulations and recipient live acceptance are separate from static packaging validation. See docs/VALIDATION.md.
