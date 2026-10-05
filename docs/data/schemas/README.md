# CSL-JSON schema

`csl-data.json` is the unmodified official Citation Style Language input schema,
retrieved 2026-10-05 from
https://raw.githubusercontent.com/citation-style-language/schema/master/schemas/input/csl-data.json.

SHA-256: `23b2c062d7526060f4631bb04b4b3ba237e488484253e327bd00fa691861b811`

Schema ID: https://resource.citationstyles.org/schema/v1.0/input/json/csl-data.json

The upstream MIT license is retained in `CSL-LICENSE.txt`. The schema permits a
`custom` object; WOEAI stores all workflow fields there. Runtime workflow
validation lives in `woeai/publications/registry.py`; the registry check command
also validates the complete bibliography against this vendored upstream schema.
