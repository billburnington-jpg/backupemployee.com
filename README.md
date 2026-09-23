# backupemployee.com

The marketing site. One static page, no build step, no dependencies.

    index.html      the page (canonical source: edit this)
    favicon.svg     folder mark, also the source of the tab icon
    og.png          1200x630 link preview, rendered from src/og.html
    CNAME           custom domain for GitHub Pages
    src/og.html     source of og.png (headless Chrome screenshot, 2x then downscaled)
    src/page.html   artifact-formatted copy of the page, kept for reference
    tools/make_artifact.py  index.html -> build/artifact.html for a Claude artifact preview

## Preview locally

    python3 -m http.server 8000   # then open http://localhost:8000

## Deploy

GitHub Pages serves `main` from the repository root. Pushing to `main` publishes.
`CNAME` holds the domain; the DNS records live at GoDaddy (four A records for the apex
plus a www CNAME to the Pages host).

## Not here

The product itself is `~/Developer/backupemployee/`, which is private and stays private.
Positioning, pricing and pipeline live in `~/Developer/agentix/`. Nothing commercial and no
client data belongs in this repo, which is public.
