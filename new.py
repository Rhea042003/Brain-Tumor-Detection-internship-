import tkinter as tk
from tkinter import END
from PIL import ImageTk, Image
import subprocess
import os
from PIL import Image, ImageTk


def verify_user():
    username = entry_username.get()
    password = entry_password.get()
    entry_username.delete(0, END)
    entry_password.delete(0, END)

    if username == 'admin' and password == 'admin123':
        root.attributes('-alpha', 0)  # Make the window fully transparent
        main_page()
    else:
        lbl_error.config(text="Invalid username or password")

def display_images():
    dataset_path = 'E:\BrainTumorDetectionFlask-master\Images'
    image_files = os.listdir(dataset_path)

    for file_name in image_files:
        # Load image using PIL
        image_path = os.path.join(dataset_path, file_name)
        image = Image.open(image_path)

        # Create a Tkinter window and display the image
        window = tk.Toplevel()
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(window, image=photo)
        label.pack()

        # Keep the window open until it is closed
        window.mainloop()

def main_page():
    new_window = tk.Toplevel()
    new_window.title("Hand Geture Based Virtual Assistant")
    new_window.geometry("400x300")
    new_window.attributes('-alpha', 0.5)  # Set transparency level for the new window
    def display_images():
            dataset_path = 'Images'
            image_files = os.listdir(dataset_path)

            for file_name in image_files:
                # Load image using PIL
                image_path = os.path.join(dataset_path, file_name)
                image = Image.open(image_path)

                # Create a Tkinter window and display the image
                window = tk.Toplevel()
                photo = ImageTk.PhotoImage(image)
                label = tk.Label(window, image=photo)
                label.pack()

                # Keep the window open until it is closed
                window.mainloop()

    def run_brigness():
        subprocess.Popen(['python', 'bright.py'])
    # Set background color
    background_color = "lightblue"
    new_window.configure(bg=background_color)

    # Buttons
    button1 = tk.Button(new_window, text="Display", width=50, height=5, command=display_images())
    button1.pack(pady=20)

    button2 = tk.Button(new_window, text="Hand Geture Based Volume Control", width=50, height=5)
    button2.pack(pady=20)

    button3 = tk.Button(new_window, text="Hand Geture Based Brightness Control", width=50, height=5,command=run_brigness)
    button3.pack(pady=20)


root = tk.Tk()
root.title("Hand Geture Based Virtual Assistant")
root.geometry("400x300")
root.attributes('-alpha', 0.5)  # Set transparency level for the main window

# # Load background image
# background_image = Image.open("")
# background_photo = ImageTk.PhotoImage(background_image)
# background_label = tk.Label(root, image=background_photo)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Login frame
login_frame = tk.Frame(root, bg="gray", padx=30, pady=30)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

# Username label and entry
label_username = tk.Label(login_frame, text="Username:", fg="white", bg="gray")
label_username.grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(login_frame)
entry_username.grid(row=0, column=1, padx=10, pady=10)

# Password label and entry
label_password = tk.Label(login_frame, text="Password:", fg="white" ,bg="gray")
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(login_frame, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Error label
lbl_error = tk.Label(login_frame, text="", fg="white", bg="gray")
lbl_error.grid(row=2, columnspan=2, padx=10, pady=10)

# Login button
login_button = tk.Button(login_frame, text="Login", bg="green", fg="white", command=verify_user)
login_button.grid(row=3, columnspan=2, padx=10, pady=10, sticky="WE")

root.mainloop()


def run_ppt():
    subprocess.Popen(['python', 'ppt.py'])