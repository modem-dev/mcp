# Logo assets

Brand color: `#44BDA3` (Modem primary teal — see [modem.dev/brand](https://modem.dev/brand)).

| File | Status | Needed by |
| --- | --- | --- |
| `wordmark-light.svg` / `wordmark-dark.svg` | ✅ copied from monorepo `apps/docs/logo/` | general use |
| `logo-square.svg` (1:1, 200×200) | ✅ exported | Claude Connectors Directory |
| `logo-64.png` (64×64, 228 B) | ✅ exported | OpenAI Plugin Directory (must be under 5 KB) |
| `logo-400.png` (400×400, 810 B) | ✅ exported | Cline |

The square exports all derive from the same source mark as the monorepo favicon
(`apps/docs/favicon.svg`), so the directory icon matches the one the docs site already serves.
Regenerate the rasters from the SVG rather than editing them by hand:

```bash
rsvg-convert -w 400 -h 400 assets/logo-square.svg -o assets/logo-400.png
rsvg-convert -w 64 -h 64 assets/logo-square.svg -o assets/logo-64.png
pngquant --force --quality 65-95 --output assets/logo-64.png -- assets/logo-64.png
```

Directories can reference these at stable raw URLs
(`https://raw.githubusercontent.com/modem-dev/mcp/main/assets/...`).
