# CPAL 2026 Website: Pending Items

This file tracks outstanding items for the 2026 website update.
It is excluded from Jekyll builds via `_config.yml`.

## Venue / Location
- [ ] Update venue location strings in `_db/data/cpal_2026.py` (currently set to "TBD"). The 2025 venue was "Simonyi Conference Center" at Stanford; the 2026 venue is in Tubingen but exact room names are not yet confirmed.

## Photos
- [ ] Rising star photos: placeholders (`image1.png` through `image18.png`) are set in the database. Actual photos need to be collected and placed in `assets/images/risingstars/`. **Temporary:** using `risingstar_noimg` layout (no photos/URLs). Revert `_config.yml` layout from `risingstar_noimg` back to `risingstar` once photos and websites are ready.

## Keynote Talks
- [ ] All keynote speaker talk titles and abstracts are TBA. Update when available.

## Rising Stars Notes
- Zhenyu Zhang (Mar 24 session): visa issues, may present remotely
- Ang Li (Mar 25 session): visa issues, may not attend in person
- Avrajit Ghosh (Mar 26 session): visa issues, still waiting for approval
- Yuqing Wang (Mar 26 session): requested online presentation

## Accepted Papers (Orals / Posters)
- [x] Proceedings track: 54 papers generated from OpenReview API (9 oral, 45 poster). Session assignments from CSV.
- [x] Spotlight track: 32 papers generated from CSV data (poster only). **Keywords missing** — spotlight OpenReview notes are not yet public (403 Forbidden). Rerun `--spotlight` once they are public to populate keywords.
- [x] Pages created: `accepted_papers.md`, `proceedings_track.md`, `spotlight_track.md`, `orals.md`, `posters.md`

## Schedule Refinements
- [ ] **Day 4 gap (3:30-4:00 PM)**: 30-minute gap between Leena Vankadara keynote (2:30-3:30) and Bernhard Scholkopf keynote (4:00-5:00). Should this be a coffee break or is it intentional?
- [ ] Confirm highlight talk session details (which papers in which sessions)
- [ ] Tutorial title for T2 slot 3 (15:30-18:00): CSV has typo "9Theoretical Insights..." -- used corrected title "Theoretical Insights on Training Instability in Deep Learning"
- [x] Days 3 and 4 registration events -- removed per user request
