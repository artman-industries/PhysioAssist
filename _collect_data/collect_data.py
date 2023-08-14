import tkinter as tk
import cv2

from _collect_data.display_frame import display_frame_at_timestamp
from _collect_data.download_video import download_video
from PIL import Image, ImageTk

current_video_path = r"C:\Users\DJISI\Desktop\technion\simester7\project\PhysioAssist\_collect_data\5dlubcRwYnI.mp4"


# https://www.youtube.com/watch?v=5dlubcRwYnI
def download_video_and_save_path(url):
    current_video_path = download_video(url)
    current_video_path = current_video_path.replace('\\\\', '\\')
    print(f'{current_video_path=}')


def save_frame():
    # Placeholder function for saving the frame
    pass


def display_frame(timestamp):
    frame = display_frame_at_timestamp(current_video_path, timestamp)
    if frame is not None:
        # # Display the frame
        cv2.imshow("Frame at Timestamp", frame)
        # cv2.waitKey(0)

        # Release the video capture object and close the display window
        # cap.release()
        # cv2.destroyAllWindows()

        # # Convert the OpenCV frame to a PhotoImage format for tkinter
        # img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # img = cv2.resize(img, (640, 480))  # Resize for display
        # img = Image.fromarray(img)
        # img = ImageTk.PhotoImage(image=img)
        #
        # # Update the label with the new frame
        # frame_label.configure(image=img)
        # frame_label.image = img


# Initialize the GUI
root = tk.Tk()
root.title("YouTube Frame Display")

# Apply custom styling to the labels and buttons
font_style = ('Helvetica', 12)
bg_color = "#F0F0F0"
root.configure(bg=bg_color)

# URL input and download button
url_label = tk.Label(root, text="Enter YouTube URL:", font=font_style, bg=bg_color)
url_label.grid(row=0, column=0, padx=10, pady=10)

url_entry = tk.Entry(root, font=font_style)
url_entry.grid(row=0, column=1, padx=10, pady=10)

download_button = tk.Button(root, text="Download Video", font=font_style,
                            command=lambda: download_video_and_save_path(url_entry.get()))
download_button.grid(row=0, column=2, padx=10, pady=10)

# First row for timestamp input and display button
timestamp_label = tk.Label(root, text="Enter Timestamp:", font=font_style, bg=bg_color)
timestamp_label.grid(row=1, column=0, padx=10, pady=10)

timestamp_entry = tk.Entry(root, font=font_style)
timestamp_entry.grid(row=1, column=1, padx=10, pady=10)

display_button = tk.Button(root, text="Display Frame", font=font_style,
                           command=lambda: display_frame(float(timestamp_entry.get())))
display_button.grid(row=1, column=2, padx=10, pady=10)

# Second row for the second frame
timestamp_label2 = tk.Label(root, text="Enter Timestamp for Second Frame:", font=font_style, bg=bg_color)
timestamp_label2.grid(row=2, column=0, padx=10, pady=10)

timestamp_entry2 = tk.Entry(root, font=font_style)
timestamp_entry2.grid(row=2, column=1, padx=10, pady=10)

display_button2 = tk.Button(root, text="Display Second Frame", font=font_style,
                            command=lambda: display_frame(float(timestamp_entry2.get())))
display_button2.grid(row=2, column=2, padx=10, pady=10)

root.mainloop()
