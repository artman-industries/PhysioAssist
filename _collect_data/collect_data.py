import os
import tkinter as tk
import cv2

from _collect_data.display_frame import display_frame_at_timestamp
from _collect_data.download_video import download_video
from _collect_data.download_video import get_video_id
from PIL import Image, ImageTk

current_video_path = None  # r"C:\Users\DJISI\Desktop\technion\simester7\project\PhysioAssist\_collect_data\5dlubcRwYnI.mp4"


# https://www.youtube.com/watch?v=5dlubcRwYnI
def download_video_and_save_path(url):
    # todo: if the url is in the database dont download it!!!
    download_video(url)
    ttt = os.path.join(os.getcwd(), get_video_id(url))
    print(f'{ttt=}')
    current_video_path = os.path.join(os.getcwd(), get_video_id(url))
    print(f'{current_video_path=}')


def save_frame():
    # Placeholder function for saving the frame
    pass


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

# Timestamp input and display button
timestamp_label = tk.Label(root, text="Enter Timestamp:", font=font_style, bg=bg_color)
timestamp_label.grid(row=1, column=0, padx=10, pady=10)

timestamp_entry = tk.Entry(root, font=font_style)
timestamp_entry.grid(row=1, column=1, padx=10, pady=10)

# Second row for the second frame
timestamp_label2 = tk.Label(root, text="Enter Timestamp for Second Frame:", font=font_style, bg=bg_color)
timestamp_label2.grid(row=2, column=0, padx=10, pady=10)

timestamp_entry2 = tk.Entry(root, font=font_style)
timestamp_entry2.grid(row=2, column=1, padx=10, pady=10)

# Create a label to display frames
frame_label = tk.Label(root)
frame_label.grid(row=3, columnspan=3, padx=10, pady=10)


def display_frames():
    timestamp_1 = float(timestamp_entry.get())
    timestamp_2 = float(timestamp_entry2.get())

    frame_1 = display_frame_at_timestamp(current_video_path, timestamp_1)
    frame_2 = display_frame_at_timestamp(current_video_path, timestamp_2)

    if frame_1 is not None and frame_2 is not None:
        img_1 = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
        img_1 = cv2.resize(img_1, (320, 240))  # Resize for display

        img_2 = cv2.cvtColor(frame_2, cv2.COLOR_BGR2RGB)
        img_2 = cv2.resize(img_2, (320, 240))  # Resize for display

        composite_image = cv2.hconcat([img_1, img_2])
        composite_image = Image.fromarray(composite_image)
        composite_image = ImageTk.PhotoImage(image=composite_image)

        frame_label.configure(image=composite_image)
        frame_label.image = composite_image


# Button to display frames
display_button = tk.Button(root, text="Display Frames", font=font_style, command=display_frames)
display_button.grid(row=1, column=2, padx=10, pady=10)


def display_frames_sequence(start_time, end_time, num_frames=10):
    sequence_window = tk.Toplevel(root)
    sequence_window.title("Frame Sequence Display")

    canvas = tk.Canvas(sequence_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(sequence_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    frame_sequence = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_sequence, anchor=tk.NW)

    for i in range(num_frames):
        timestamp = start_time + (i / (num_frames - 1)) * (end_time - start_time)
        frame = display_frame_at_timestamp(current_video_path, timestamp)

        if frame is not None:
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (320, 240))
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(image=img)

            frame_label = tk.Label(frame_sequence)
            frame_label.configure(image=img)
            frame_label.image = img
            frame_label.grid(row=i, column=0, padx=10, pady=10)

    frame_sequence.update_idletasks()  # Update canvas size

    canvas.config(scrollregion=canvas.bbox(tk.ALL))


# Button to display frames
display_sequence_button = tk.Button(root, text="Display Sequence", font=font_style,
                                    command=lambda: display_frames_sequence(float(timestamp_entry.get()),
                                                                            float(timestamp_entry2.get())))
display_sequence_button.grid(row=2, column=2, padx=10, pady=10)

root.mainloop()
