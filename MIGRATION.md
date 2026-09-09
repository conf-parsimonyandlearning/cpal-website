# CPAL 2027 migration

The official site's existing `2027` branch (`0c3481ea6da75d4cf4b98ef943dcdc5da6260ecb`, also the inspected `main` tip) is the base. Content comes from `DakeBU/cpal-website-2027` at `c0c788d9371d0ec697406e261625f1dd206ec2a0`.

## Structure and deployment

Both sites use Jekyll 3.9.0 and just-the-docs 0.5.4. The source uses `_data/organizers.yml`, custom includes, a page layout, Sass, JavaScript, Markdown pages and image assets. The official site previously used generated collections and `_db`.

The source deploys `main` to GitHub Pages with `actions/deploy-pages`. That workflow was deliberately not imported. The official repository's `CLAUDE.md` describes Cloudflare Pages integration, and cpal.cc responds via Cloudflare. Its existing `.github/workflows/claude.yml` is unchanged. No Pages settings, DNS settings, production configuration or production branch are changed by this migration. The connected GitHub tools do not expose Cloudflare's project settings.

The intended review target is **2027**, never main. A feature branch may receive a Cloudflare preview if the existing integration enables it; this migration does not add or dispatch a deployment workflow.

## Changes

- Imported all source pages, data, templates, styles and assets; retained its published facts and explicit forthcoming content.
- Set `url: https://cpal.cc`, empty `baseurl`, official repository metadata and `CNAME: cpal.cc`. Registration and OpenReview navigation use root paths. No source preview prefix remains in built 2027 pages.
- Localized the Tokyo banner and all 24 organizer portraits. Jere Sulam and Ambar Pal's source image hosts returned HTTP 403; their identified portraits are copied from the official 2026 organizer and 2024 Rising Stars archives, respectively. Credits remain in `_data/organizers.yml` and the attribution page.
- Removed the old official `assets/js/just-the-docs.js` override: together with the new custom handler it toggled category menus twice. The pinned theme supplies the base script. Adjusted the mobile contact footer to prevent content overlap.
- Excluded old draft pages under `assets/todo` and internal maintenance files from the current website. Original historical collections, database files and other assets remain in Git.
- Preserved `/cfp/` and `/other_years/` as legacy link pages.

## Historical archives

2024 and 2025 continue to link to their existing subdomains (both returned HTTP 200 on 2026-09-09). The 2026 subdomain did not resolve. Instead of sending visitors back to the new homepage, `/past/` links to a self-contained, frozen **/2026/** archive (36 HTML pages plus assets, approximately 26 MB).

The 2026 archive is pre-rendered and checked in so ordinary `bundle exec jekyll build` preserves it without requiring a custom deployment command or plugin. It retains the previous site's original theme, styles, images, program and papers. Internal root links were moved under `/2026/`, an existing email link was corrected to `mailto:`, and unpublished `assets/todo` pages and `CLAUDE.md` were omitted. No 2024/2025 branch is modified.

To reproduce the archive, extract the pinned official base commit into a separate temporary source directory, install its locked gems, then build it with:

```sh
JEKYLL_ENV=production bundle exec jekyll build --baseurl /2026 --destination /tmp/cpal-2026-built
```

From this migration checkout, import the result with:

```sh
python3 scripts/import_archive.py /tmp/cpal-2026-built
```

Do not use the current 2027 source to regenerate the 2026 archive.

## Build and preview

With Ruby and Bundler 2.4.22 installed:

```sh
bundle install
JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py
python3 -m http.server 4027 --bind 127.0.0.1 --directory _site
```

Open http://127.0.0.1:4027/ (committee: `/organization_committee/`; archive: `/2026/`). Serve the built site from the host root, with empty baseurl, matching cpal.cc. A same-host preview does not need a repository-name subpath.

## Validation

- Production Jekyll build passes with strict front matter.
- 77 generated HTML pages (41 current pages and 36 archived pages); 3,924 internal HTML references checked, including fragments, images and canonical URLs; zero missing targets.
- 24 locally stored organizer portraits checked for image validity and browser loading.
- Chrome desktop and mobile checks cover homepage, call for papers, deadlines, committee, venue, registration, OpenReview, archive index, 2026 homepage and 2026 program. All return HTTP 200; no broken images or JavaScript errors. Desktop category navigation and the mobile menu are exercised.
- `git diff --check` passes. Original source hard line breaks are preserved using explicit `<br>` tags.

Registration, OpenReview, submission forms, speakers and other forthcoming content remain at the status supplied by the source. This migration does not invent unannounced portals or conference information.
