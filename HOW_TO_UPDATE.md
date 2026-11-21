# How to update this site

The site is a React app (Vite, TypeScript, Tailwind, Framer Motion). Source is in `site-src/`. GitHub Pages serves the built files in the repo root.

## Change text, roles or projects
Edit `site-src/src/content.json` (roles, clients, projects, email, WhatsApp link). Section wording is in `site-src/src/components/`.

## Add your photo
Save a transparent or plain-background portrait as `site-src/public/portrait.png` (about 900 px wide). Until it exists, the hero shows an "SA" monogram.

## Publish a change
```bash
cd site-src && ./deploy.sh     # builds and copies the result to the repo root
git add -A && git commit -m "Update site" && git push
```

## Counter (visitors, resume downloads, emails, WhatsApp)
Runs on your own Cloudflare Worker, see `tools/counter-worker/README.md`. The Worker address is set in `site-src/src/track.ts`.

## Contact form
Uses Web3Forms. The public access key is in `site-src/src/components/Contact.tsx`.
