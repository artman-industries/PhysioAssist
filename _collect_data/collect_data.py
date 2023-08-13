import tkinter as tk
from tkinter import messagebox
import cv2
import os
from download_video import download_video


def display_frame(url, time, label):
    cap = cv2.VideoCapture(url)
    cap.set(cv2.CAP_PROP_POS_MSEC, time * 1000)

    ret, frame = cap.read()
    cap.release()

    if ret:
        label.config(image=tk.PhotoImage(data=cv2.imencode('.png', frame)[1].tobytes()))
    else:
        messagebox.showerror("Error", "Unable to fetch frame.")


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
                            command=lambda: download_video(url_entry.get()))
download_button.grid(row=0, column=2, padx=10, pady=10)

# Time input for frames (same as before)

# Create frame placeholders (same as before)

# Save button (same as before)

root.mainloop()
