# shaungarwood.github.io

Personal blog at [shaungarwood.com](https://shaungarwood.com). Built with Astro and the Spectre theme.

## Tech Stack

- **[Astro](https://astro.build)** — static site generator
- **[Spectre](https://github.com/louisescher/spectre)** — terminal-inspired theme (local copy in `/package`)
- **MDX** — blog posts with component support
- **Pagefind** — client-side search (runs post-build; search only works after `pnpm build`, not in dev)
- **`@astrojs/rss`** — RSS feed at `/rss.xml`
- **`@astrojs/sitemap`** — auto-generated sitemap
- **Geist / Geist Mono** — fonts (self-hosted in `/public/fonts`)
- **[Lucide icons](https://lucide.dev/icons)** — icon set used throughout the UI (browse at lucide.dev/icons)
- **pnpm** — package manager

## Project Layout

```
src/
├── content/
│   ├── posts/          # Blog posts (.mdx)
│   ├── projects/       # Project showcases (.mdx)
│   ├── other/          # Misc pages (about.mdx)
│   ├── info.json       # Quick info items (location, skills, etc.)
│   ├── socials.json    # Social links
│   └── tags.json       # Available post tags
├── pages/
│   ├── index.astro     # Homepage
│   ├── blog.astro      # Post listing
│   ├── blog/[post].astro
│   ├── projects.astro
│   └── rss.xml.ts      # RSS feed
├── components/
├── layouts/
│   └── Layout.astro    # Root layout (head, nav, grid)
├── styles/
│   ├── reset.css       # Fonts + CSS reset
│   └── globals.css     # Colors, shared styles
└── assets/             # Profile picture, etc.

package/                # Local Spectre Astro integration
public/                 # Static assets (fonts, favicon, OG image)
```

## Running Locally

Requires [pnpm](https://pnpm.io).

```bash
pnpm install
pnpm dev
```

The dev server starts at `http://localhost:4321`.

## Writing a Post

1. Copy `src/content/posts/new-post-template.mdx` to a new file in the same directory.
2. Fill out the frontmatter:

```yaml
---
title: "Post Title"
description: "One-liner for previews and SEO."
image: "../assets/your-image.png"
createdAt: MM-DD-YYYY
draft: false
tags:
  - docker
---
```

3. Write the post in MDX below the frontmatter.
4. Set `draft: true` to keep it out of production builds.

Available tags are defined in `src/content/tags.json`.

## Signing a Post

Posts can be GPG signed to prove authorship. Signed posts show a "Cryptographically proven to be Shaun" badge with a verification trail.

```bash
./scripts/sign-post.py src/content/posts/my-post.mdx
```

The script:
1. Injects `signed: true` into the post's frontmatter
2. Creates a detached armor signature at `public/signatures/<slug>.asc`

The signature covers the full MDX file (frontmatter + content), so any post-publish edits will invalidate it. Re-run the script to re-sign after edits.

The raw MDX source is served at `/source/<slug>` so readers can verify without touching GitHub:

```bash
curl https://shaungarwood.com/source/my-post > post.mdx
curl https://shaungarwood.com/signatures/my-post.asc > post.asc
gpg --fetch-keys https://shaungarwood.com/pgp-key.asc
gpg --verify post.asc post.mdx
```

CI will warn on any push or PR that contains unsigned published posts.

## Building

```bash
pnpm build    # runs astro build + pagefind indexing
pnpm preview  # preview the production build
```

## Verify Page (`/verify`)

`src/pages/verify.astro` — identity verification page. It surfaces:

- **Keyoxide** profile linking the PGP key to controlled accounts
- **PGP public key** fingerprint + downloadable `.asc` file (served from `public/pgp-key.asc`)
- **DID document** at `/.well-known/did.json` (`did:web:shaungarwood.com`)

To update the fingerprint or Keyoxide URL, edit the constants at the top of `verify.astro`.

## Deployment

Deployed to GitHub Pages via the workflow in `.github/workflows/`. Pushes to `master` trigger a build and deploy automatically.

Custom domain is set via the `CNAME` file (`shaungarwood.com`).
