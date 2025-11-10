#!/bin/bash
# Script to download speaker photos
# Run this script to download raw photos for new speakers

mkdir -p ../assets/images/speakers/raw

# Andreas Krause - ETH Zurich
echo "Downloading Andreas Krause photo..."
wget -O ../assets/images/speakers/raw/krause.jpg "https://las.inf.ethz.ch/krausea/files/krause.jpg" 2>/dev/null || \
curl -L -o ../assets/images/speakers/raw/krause.jpg "https://las.inf.ethz.ch/krausea/files/krause.jpg" 2>/dev/null || \
echo "Could not download Krause photo - please download manually from https://las.inf.ethz.ch/krausea"

# Matthias Bethge - Tübingen University
echo "Downloading Matthias Bethge photo..."
wget -O ../assets/images/speakers/raw/bethge.jpg "https://bethgelab.org/media/people/matthias.jpg" 2>/dev/null || \
curl -L -o ../assets/images/speakers/raw/bethge.jpg "https://bethgelab.org/media/people/matthias.jpg" 2>/dev/null || \
echo "Could not download Bethge photo - please download manually from https://bethgelab.org/people/matthias/"

# Jared Tanner - Oxford
echo "Downloading Jared Tanner photo..."
wget -O ../assets/images/speakers/raw/tanner.jpg "https://people.maths.ox.ac.uk/tanner/tanner.jpg" 2>/dev/null || \
curl -L -o ../assets/images/speakers/raw/tanner.jpg "https://people.maths.ox.ac.uk/tanner/tanner.jpg" 2>/dev/null || \
echo "Could not download Tanner photo - please download manually from https://people.maths.ox.ac.uk/tanner/"

# Leena Chennuru Vankadara - UCL
echo "Downloading Leena Chennuru Vankadara photo..."
wget -O ../assets/images/speakers/raw/vankadara.jpg "https://leenachennuru.github.io/images/profile.jpg" 2>/dev/null || \
curl -L -o ../assets/images/speakers/raw/vankadara.jpg "https://leenachennuru.github.io/images/profile.jpg" 2>/dev/null || \
echo "Could not download Vankadara photo - please download manually from https://leenachennuru.github.io/"

echo "Download complete. Check ../assets/images/speakers/raw/ for images."
echo "Next step: Run image-preparer.py to process these images to 1:1 aspect ratio"
