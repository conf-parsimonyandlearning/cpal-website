# CPAL Website Database Scripts

This directory contains Python scripts for managing the CPAL conference website content, including organizer profiles, speaker information, rising stars, tutorials, and conference programs.

## Directory Structure

```
_db/
├── pyproject.toml          # Python project dependencies (managed by uv)
├── uv.lock                 # Lock file for reproducible dependencies
├── .python-version         # Python version specification
├── README.md               # This file
└── data/                   # Database scripts and data
    ├── cpal_2024.py        # 2024 conference database
    ├── cpal_2025.py        # 2025 conference database
    ├── cpal_2026.py        # 2026 conference database
    ├── credentials.txt     # OpenReview API credentials (gitignored)
    ├── event.py            # Event data structures
    ├── papers.py           # Paper/proceedings utilities
    ├── program.py          # Program/calendar data structures
    ├── roles.py            # Role data structures (Organizer, Speaker, etc.)
    ├── image-preparer.py   # Image processing utility
    └── cpal_2025_session_dict.py  # Session mappings for 2025

```

## Setup

This project uses `uv` for dependency management. Install dependencies with:

```bash
cd _db
uv sync
```

## Basic Functionality

### 1. Image Processing

The `image-preparer.py` script automatically detects faces in raw speaker/organizer photos and crops them to the appropriate aspect ratio.

**Usage:**

```bash
uv run python data/image-preparer.py <input_directory> [--aspect-ratio RATIO]
```

**Examples:**

```bash
# Process images with 1:1 aspect ratio (square, for organizers/rising stars/speakers)
uv run python data/image-preparer.py path/to/raw/images --aspect-ratio 1.0
```

The processed images will be saved in `<input_directory>/processed_images/` with the suffix `_processed.png`.

### 2. Building Website YAML Files

The annual database scripts (e.g., `cpal_2026.py`) generate YAML files for the Jekyll website. These scripts read from the Python data structures and export to the appropriate `_collections` directories in the main website repository.

**Usage:**

```bash
cd data
uv run python cpal_2026.py [OPTIONS]
```

**Available Options:**

- `--orgs`: Export organizer YAML files to `_organizers/`
- `--speakers`: Export speaker YAML files to `_speakers/`
- `--tutorials`: Export tutorial YAML files (if applicable)
- `--stars`: Export rising star YAML files to `_risingstars/`
- `--proceedings`: Export proceedings track papers to `_proceedings/`
- `--spotlight`: Export spotlight track papers to `_spotlight/`
- `--calendar`: Generate and export the event calendar to `_calendars/`
- `--org-emails`: Print organizer email addresses (useful for communications)

**Examples:**

```bash
# Export all organizers
uv run python cpal_2026.py --orgs

# Export speakers and rising stars
uv run python cpal_2026.py --speakers --stars

# Generate the full conference calendar
uv run python cpal_2026.py --calendar

# Export everything needed for the website
uv run python cpal_2026.py --orgs --speakers --stars --calendar
```

## Workflow

A typical workflow for updating the website content:

1. **Prepare images**: Place raw speaker/organizer photos in a directory and run `image-preparer.py`
2. **Update database**: Edit the relevant `cpal_YYYY.py` file to add/update speaker, organizer, or event information
3. **Generate YAML**: Run the database script with appropriate flags to export YAML files
4. **Commit changes**: Commit both the database changes and generated YAML files to git

## Notes

- The `credentials.txt` file contains OpenReview API credentials and should never be committed to git (it's in `.gitignore`)
- All scripts assume they are being run from within the `_db/` directory
- The `root` variable in each annual database script (located in `_db/data/`) uses `Path(__file__).parent.parent.parent` to point to the website repository root
- Image paths in the database scripts should be relative to the Jekyll `assets/` directory
