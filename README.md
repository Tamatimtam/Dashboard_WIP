# Dashboard WIP (Solarpunk)

A lightweight recreation of the provided dashboard mockup using semantic HTML, modern CSS, and Vanilla JavaScript with GSAP for animations.

## What's inside
- `index.html` – structure and SVG artwork (no inline scripts/styles)
- `styles.css` – tiny entrypoint that imports modular CSS from `css/`
- `css/` – modular styles:
	- `base/variables.css`, `base/globals.css`
	- `layout/structure.css`
	- `components/hero.css`, `components/topbar.css`, `components/cards.css`, `components/charts.css`
	- `utilities/utilities.css`, `utilities/responsive.css`
- `js/main.js` – ESM bootstrap
- `js/animations/*` – entrance and hover micro-interactions
- `js/charts/*` – line, bars, donut animations

## Run locally
This is a static site. Open `index.html` directly or serve the folder with any static server.

```bash
# Option 1: Python (installed by default on most systems)
python3 -m http.server --directory . 5173
# Then open http://localhost:5173/home/timtam/Documents/code/Dashboard_WIP/

# Option 2: Node (if installed)
npx serve .
```

## Notes
- The grain overlay uses an inline SVG `feTurbulence` mapped as a background image and blended with `mix-blend-mode: overlay` for a soft organic texture.
- GSAP powers subtle, natural motion; animations respect the user's `prefers-reduced-motion` setting.
- The color system and shadows aim to keep a warm, solarpunk aesthetic with tactile depth.

## Project docs (analysis & planning)
- `docs/brainstorming_ideation.md` – narasi ideation (ID), EDA ringkas, insight, rekomendasi, dan aturan kompetisi.
- `docs/dashboard_panels.md` – spesifikasi panel, visual, interaksi, dan pedoman aksesibilitas.
- `docs/pitch.md` – ringkasan singkat (6–8 bullets) untuk presentasi.