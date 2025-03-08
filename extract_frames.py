import cv2
import os
import argparse

def extract_frames(input_file, output_dir='frames', image_format='jpg', quality=80):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the video file
    cap = cv2.VideoCapture(input_file)
    if not cap.isOpened():
        print(f"Error: Cannot open file {input_file}")
        return

    frame_count = 0

    while True:
        ret, frame = cap.read()
        # If no frame is returned, we've hit the end of the video
        if not ret:
            break

        # Construct the output filename; e.g., frame_000001.jpg
        frame_count_str = str(frame_count).zfill(6)
        output_filepath = os.path.join(output_dir, f"frame_{frame_count_str}.{image_format}")

        # If saving as JPEG, you can specify JPEG quality
        # For WebP or PNG, you can specify compression params similarly
        if image_format.lower() == 'jpg' or image_format.lower() == 'jpeg':
            # cv2.IMWRITE_JPEG_QUALITY ranges from 0 to 100 (higher means better quality but bigger file size)
            cv2.imwrite(output_filepath, frame, [cv2.IMWRITE_JPEG_QUALITY, quality])
        else:
            # Default parameters for PNG or other formats
            cv2.imwrite(output_filepath, frame)

        frame_count += 1

    # Release the video capture object
    cap.release()
    print(f"Extraction complete! {frame_count} frames saved in '{output_dir}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract frames from a video file.")
    parser.add_argument("input_file", help="Path to the input file.")
    parser.add_argument("--output_dir", default="frames", help="Output directory for the extracted frames.")
    parser.add_argument("--format", default="jpg", help="Output image format (e.g., jpg, png, webp).")
    parser.add_argument("--quality", type=int, default=80, help="Quality for JPEG compression (0-100).")
    
    args = parser.parse_args()

    extract_frames(
        input_file=args.input_file, 
        output_dir=args.output_dir, 
        image_format=args.format, 
        quality=args.quality
    )
