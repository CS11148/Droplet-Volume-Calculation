import cv2
import os

def extract_frames(video_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))  # Frames per second
    count = 0
    
    while cap.isOpened():
        cap.set(cv2.CAP_PROP_POS_FRAMES, count * fps * 15)  # Move to every 15 seconds
        ret, frame = cap.read()
        if not ret:
            break
        minutes = (count * 15) // 60
        seconds = (count * 15) % 60
        output_path = os.path.join(output_folder, f"{minutes}m{seconds}.png")
        cv2.imwrite(output_path, frame)
        print(f"Saved: {output_path}")
        count += 1
    
    cap.release()
    print("Frame extraction complete.")

# Example usage
video_file = "input.mp4"  # Change this to your video file path
output_dir = "frames_output"
extract_frames(video_file, output_dir)
