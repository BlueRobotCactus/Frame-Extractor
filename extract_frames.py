import cv2
import os
import argparse

def extract_frames(input_file, output_dir='frames'):
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

        # Construct the output filename; e.g., frame_000001.png
        frame_count_str = str(frame_count).zfill(6)
        output_filepath = os.path.join(output_dir, f"frame_{frame_count_str}.png")

        # Save the frame as a .png image
        cv2.imwrite(output_filepath, frame)
        
        frame_count += 1

    # Release the video capture object
    cap.release()
    print(f"Extraction complete! {frame_count} frames saved in '{output_dir}'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract frames from a .mkv file.")
    parser.add_argument("input_file", help="Path to the input .mkv file.")
    parser.add_argument("--output_dir", default="frames", help="Output directory for the extracted frames.")
    
    args = parser.parse_args()

    extract_frames(args.input_file, args.output_dir)
