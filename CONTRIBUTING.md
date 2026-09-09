# Contributing to the CPAL 2027 website

Content is intentionally data-driven and launch-stage conservative.

- Edit `_data/organizers.yml` to update names, roles, affiliations, websites,
  portraits, or portrait credits.
- Edit the corresponding Markdown page for public content.
- Check `CONTENT_STATUS.md` before publishing a deadline, portal, sponsor,
  speaker, or policy.
- Run `bundle exec jekyll build` before merging.

Please keep external links on HTTPS and provide attribution for newly added
images or logos.

Organizer portraits use a fixed 100 × 100 px circular frame. `photo_scale` and
`photo_offset_x` / `photo_offset_y` in `_data/organizers.yml` normalize head size
and framing using CSS only; retain the original image and its credit. Check the
full committee page on desktop and mobile after replacing a portrait.
