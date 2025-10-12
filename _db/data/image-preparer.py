#!/usr/bin/env python
# -*- coding: utf-8 -*-

# imports
import argparse
import glob
import os

import cv2
import matplotlib.pyplot as plt
from PIL import Image

# Load the pre-trained Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


import cv2


def detect_face(image_path):
    # Load the image using OpenCV
    img = cv2.imread(image_path)

    # Check if the image was successfully loaded
    if img is None:
        print(f"Error: Could not open {image_path}. Check the file path and format.")
        return None, None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image (returns all detected faces)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) == 0:
        print(f"No face detected in {image_path}")
        return None, None

    # Calculate the center of the image (to prioritize faces near the center)
    img_center_x, img_center_y = img.shape[1] // 2, img.shape[0] // 2

    # Function to score faces based on size and distance from the center of the image
    def face_score(face):
        x, y, w, h = face
        face_center_x, face_center_y = x + w // 2, y + h // 2
        size_score = w * h  # Face size (prefer larger faces)
        distance_score = (
            (face_center_x - img_center_x) ** 2 + (face_center_y - img_center_y) ** 2
        ) ** 0.5
        return size_score - distance_score  # Larger face + closer to center = better

    # Sort faces by the score (higher score is better)
    best_face = max(faces, key=face_score)

    x, y, w, h = best_face

    # DEBUG: Plot the bounding box over the image
    img_with_box = img.copy()
    cv2.rectangle(
        img_with_box, (x, y), (x + w, y + h), (255, 0, 0), 2
    )  # Draw bounding box

    # Convert to RGB format for matplotlib
    img_rgb = cv2.cvtColor(img_with_box, cv2.COLOR_BGR2RGB)

    # Plot the image with the bounding box
    plt.figure(figsize=(8, 6))
    plt.imshow(img_rgb)
    plt.title(f"Detected face in {image_path}")
    plt.axis("off")  # Hide axis labels
    plt.show()

    return (x, y, w, h), img


# Parameters for padding control
top_bottom_padding_percentage = 0.5  # 50% of the face height above and below
left_right_padding_percentage = 0.2  # 20% of the face width to the left and right
target_height = 400  # Output height


def adjust_bounding_box(x, y, w, h, img_width, img_height):
    # Add padding based on percentage of height and width
    padding_top_bottom = int(h * top_bottom_padding_percentage)
    padding_left_right = int(w * left_right_padding_percentage)

    # Adjust the bounding box with padding
    crop_top = max(0, y - padding_top_bottom)
    crop_bottom = min(img_height, y + h + padding_top_bottom)
    crop_left = max(0, x - padding_left_right)
    crop_right = min(img_width, x + w + padding_left_right)

    # New crop width and height after padding
    crop_width = crop_right - crop_left
    crop_height = crop_bottom - crop_top

    return crop_top, crop_bottom, crop_left, crop_right, crop_width, crop_height


def ensure_aspect_ratio(
    crop_top,
    crop_bottom,
    crop_left,
    crop_right,
    crop_width,
    crop_height,
    img_width,
    img_height,
    target_aspect_ratio,
):
    # Calculate current aspect ratio (height:width)
    current_aspect_ratio = crop_height / crop_width

    if current_aspect_ratio < target_aspect_ratio:
        # Current crop is too wide - need to reduce width
        # Calculate the required width to match the target aspect ratio
        required_width = int(crop_height / target_aspect_ratio)
        width_reduction = crop_width - required_width

        # Add equal padding to both sides (reduce width equally from both sides)
        pad_left = width_reduction // 2
        pad_right = width_reduction - pad_left

        crop_left += pad_left
        crop_right -= pad_right

    elif current_aspect_ratio > target_aspect_ratio:
        # Current crop is too tall - need to reduce height
        # Calculate the required height to match the target aspect ratio
        required_height = int(crop_width * target_aspect_ratio)
        height_reduction = crop_height - required_height

        # Add equal padding to top and bottom (reduce height equally from top and bottom)
        pad_top = height_reduction // 2
        pad_bottom = height_reduction - pad_top

        crop_top += pad_top
        crop_bottom -= pad_bottom

    # Return the adjusted coordinates
    return crop_top, crop_bottom, crop_left, crop_right


def crop_and_resize(image, face_box, target_aspect_ratio):
    x, y, w, h = face_box
    img_height, img_width = image.shape[:2]

    # Step 1: Adjust bounding box with controllable padding
    crop_top, crop_bottom, crop_left, crop_right, crop_width, crop_height = (
        adjust_bounding_box(x, y, w, h, img_width, img_height)
    )

    # Step 2: Ensure the adjusted box has the correct aspect ratio
    # Instead of expanding the crop, we'll trim it to maintain aspect ratio
    crop_top, crop_bottom, crop_left, crop_right = ensure_aspect_ratio(
        crop_top,
        crop_bottom,
        crop_left,
        crop_right,
        crop_right - crop_left,  # Use actual width after padding
        crop_bottom - crop_top,  # Use actual height after padding
        img_width,
        img_height,
        target_aspect_ratio,
    )

    # Step 3: Crop the image
    cropped_img = image[crop_top:crop_bottom, crop_left:crop_right]

    # Convert the cropped image to PIL format for resizing
    cropped_img_pil = Image.fromarray(cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB))

    # Calculate target width based on target aspect ratio and target height
    target_width = int(target_height / target_aspect_ratio)

    # Resize to the final size
    resized_img = cropped_img_pil.resize(
        (target_width, target_height), Image.Resampling.LANCZOS
    )

    return resized_img


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Process images with face detection and cropping")
    parser.add_argument(
        "input_dir",
        help="Input directory containing images"
    )
    parser.add_argument(
        "--aspect-ratio", 
        type=float, 
        default=1.0, 
        help="Target aspect ratio (height/width) for cropped images (default: 1.0 for 1:1 square)"
    )
    
    args = parser.parse_args()
    target_aspect_ratio = args.aspect_ratio
    input_dir = args.input_dir
    
    output_dir = os.path.join(input_dir, "processed_images")

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    image_paths = (
        glob.glob(f"{input_dir}/*.jpg")
        + glob.glob(f"{input_dir}/*.jpeg")
        + glob.glob(f"{input_dir}/*.png")
    )

    for image_path in image_paths:
        face_box, img = detect_face(image_path)

        if face_box:
            # Perform crop and resize
            result_img = crop_and_resize(img, face_box, target_aspect_ratio)

            # Generate output file name
            file_name = os.path.basename(image_path)
            name_without_ext = os.path.splitext(file_name)[0]
            output_path = os.path.join(output_dir, f"{name_without_ext}_processed.png")

            # Save the processed image
            result_img.save(output_path)
            print(f"Processed image saved as {output_path}")


if __name__ == "__main__":
    main()
