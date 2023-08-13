import cv2


def display_frame_at_timestamp(video_path, timestamp):
    try:
        # Open the video file
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print("Error: Could not open video file.")
            return

        # Calculate the frame number based on the timestamp and video's frame rate
        frame_rate = cap.get(cv2.CAP_PROP_FPS)
        frame_number = int(frame_rate * timestamp)

        # Set the video's position to the calculated frame number
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

        # Read the frame at the specified timestamp
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to read frame.")
            return

        # Display the frame
        cv2.imshow("Frame at Timestamp", frame)
        cv2.waitKey(0)

        # Release the video capture object and close the display window
        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Example usage
if __name__ == "__display_frame__":
    video_path = r"C:\Users\DJISI\Desktop\technion\simester7\project\PhysioAssist\_collect_data\name.mp4"
    timestamp = 10.0  # Example timestamp in seconds

    display_frame_at_timestamp(video_path, timestamp)
