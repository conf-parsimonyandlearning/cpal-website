# Instructions for Adding New Speakers

This file contains instructions for adding the 4 new keynote speakers requested in Issue #16.

## New Speakers to Add

1. **Andreas Krause** - ETH Zurich
   - Website: https://las.inf.ethz.ch/krausea
   - Photo URL (suggested): https://las.inf.ethz.ch/krausea (check page for image)

2. **Matthias Bethge** - Tübingen University
   - Website: https://bethgelab.org/people/matthias/
   - Photo URL (suggested): https://bethgelab.org/people/matthias/ (check page for image)

3. **Jared Tanner** - University of Oxford
   - Website: https://people.maths.ox.ac.uk/tanner/
   - Photo URL (suggested): https://people.maths.ox.ac.uk/tanner/ (check page for image)

4. **Leena Chennuru Vankadara** - University College London
   - Website: https://leenachennuru.github.io/
   - Photo URL (suggested): https://leenachennuru.github.io/ (check page for image)

## Steps to Complete

### 1. Download Photos

Download professional photos for each speaker from their webpages listed above and save them to:
```
assets/images/speakers/raw/
```

Name them:
- `krause.jpg` (or .png)
- `bethge.jpg` (or .png)
- `tanner.jpg` (or .png)
- `vankadara.jpg` (or .png)

### 2. Process Images to 1:1 Aspect Ratio

Run the image preparer script on the raw images:

```bash
cd _db
uv run python data/image-preparer.py ../assets/images/speakers/raw --aspect-ratio 1.0
```

This will create processed images in `assets/images/speakers/raw/processed_images/`

### 3. Move Processed Images

Move the processed images to the speakers directory with appropriate names:

```bash
mv ../assets/images/speakers/raw/processed_images/krause_processed.png ../assets/images/speakers/krause.png
mv ../assets/images/speakers/raw/processed_images/bethge_processed.png ../assets/images/speakers/bethge.png
mv ../assets/images/speakers/raw/processed_images/tanner_processed.png ../assets/images/speakers/tanner.png
mv ../assets/images/speakers/raw/processed_images/vankadara_processed.png ../assets/images/speakers/vankadara.png
```

### 4. Add to Database

Add the following entries to the `make_speakers()` function in `_db/data/cpal_2025.py`:

```python
speakers.append(
    Speaker(
        name="Andreas Krause",
        role="Keynote Speaker",
        website="https://las.inf.ethz.ch/krausea",
        affiliation="ETH Zurich",
        photo="krause.png",
        talk="TBA",
        abstract="TBA",
        bio="TBA",
        day="TBA",  # Set appropriate day
        start="TBA",  # Set appropriate time
        end="TBA",  # Set appropriate time
        location=day_two_str,  # Or day_one_str as appropriate
    )
)

speakers.append(
    Speaker(
        name="Matthias Bethge",
        role="Keynote Speaker",
        website="https://bethgelab.org/people/matthias/",
        affiliation="Tübingen University",
        photo="bethge.png",
        talk="TBA",
        abstract="TBA",
        bio="TBA",
        day="TBA",
        start="TBA",
        end="TBA",
        location=day_two_str,
    )
)

speakers.append(
    Speaker(
        name="Jared Tanner",
        role="Keynote Speaker",
        website="https://people.maths.ox.ac.uk/tanner/",
        affiliation="University of Oxford",
        photo="tanner.png",
        talk="TBA",
        abstract="TBA",
        bio="TBA",
        day="TBA",
        start="TBA",
        end="TBA",
        location=day_two_str,
    )
)

speakers.append(
    Speaker(
        name="Leena Chennuru Vankadara",
        role="Keynote Speaker",
        website="https://leenachennuru.github.io/",
        affiliation="University College London",
        photo="vankadara.png",
        talk="TBA",
        abstract="TBA",
        bio="TBA",
        day="TBA",
        start="TBA",
        end="TBA",
        location=day_two_str,
    )
)
```

### 5. Generate YAML Files

```bash
cd _db/data
uv run python cpal_2025.py --speakers
```

### 6. Commit Changes

Commit all changes including:
- Raw speaker photos (for verification)
- Processed speaker photos
- Updated database file
- Generated YAML files

## Notes

- All speaker photos should be 1:1 aspect ratio (400x400 pixels after processing)
- The image-preparer.py script uses face detection to automatically crop and center photos
- Keep the rounded rectangle border style (border-radius: 25%) - not circles like organizers
