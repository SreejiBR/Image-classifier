import os
import PIL
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
from tensorflow import keras
import pyttsx3
import wikipedia
import threading

model = keras.applications.vgg16.VGG16(weights='imagenet')

def classify_image():
    global predicted_class
    img_path = filedialog.askopenfilename()  # Prompt the user to select an image file
    if img_path:
        img = keras.preprocessing.image.load_img(img_path, target_size=(224, 224))
        x = keras.preprocessing.image.img_to_array(img)
        x = tf.keras.applications.vgg16.preprocess_input(x)
        preds = model.predict(tf.expand_dims(x, axis=0))
        predicted_class = keras.applications.vgg16.decode_predictions(preds, top=1)[0][0][1]
        class_label.config(text=f"The image could be of class: {predicted_class}")

def browse_folder():
    global folder_path
    folder_path = filedialog.askdirectory()

def search_image():
    global folder_path
    search_term = search_entry.get()
    if search_term and folder_path:
        for filename in os.listdir(folder_path):  # Search in the selected folder
            try:
                img = keras.preprocessing.image.load_img(os.path.join(folder_path, filename), target_size=(224, 224))
            except PIL.UnidentifiedImageError:
                print(f"Cannot load image file: {filename}")
                continue
            x = keras.preprocessing.image.img_to_array(img)
            x = tf.keras.applications.vgg16.preprocess_input(x)
            preds = model.predict(tf.expand_dims(x, axis=0))
            predicted_class = keras.applications.vgg16.decode_predictions(preds, top=1)[0][0][1]
            if search_term.lower() in predicted_class.lower():
                img = Image.open(os.path.join(folder_path, filename))
                img.thumbnail((200, 200))
                img = ImageTk.PhotoImage(img)
                search_label.config(image=img)
                search_label.image = img
                search_result_label.config(text=f"Found image: {filename}")
                return
        search_result_label.config(text=f"No image matching '{search_term}' found.")
    else:
        search_result_label.config(text="Please select a folder and enter a search term.")

def explain():
    global predicted_class
    search_term = predicted_class.replace('_', ' ')
    try:
        summary = wikipedia.summary(search_term, sentences=3)
    except wikipedia.exceptions.DisambiguationError as e:
        summary = wikipedia.summary(e.options[0], sentences=3)
    def speak():
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 135)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(summary)
        engine.runAndWait()

    t = threading.Thread(target=speak)
    t.start()

root = tk.Tk()
root.title("Image Classifier - S6 MINI PROJECT")
root.minsize(900, 500)

root.configure(background="light gray")

classify_frame = tk.Frame(root)
classify_frame.pack(fill=tk.X, padx=10, pady=10)

# Set the b
classify_frame.configure(borderwidth=2)

classify_label = tk.Label(classify_frame, text="Classify Image", font=("Arial", 16))
classify_label.pack(side=tk.LEFT)

classify_button = tk.Button(classify_frame, text="Select Image", font=("Arial", 12), command=classify_image)
classify_button.pack(side=tk.LEFT, padx=(10,0))

class_label = tk.Label(root, font=("Arial", 14))
class_label.pack(padx=10, pady=10)

search_frame = tk.Frame(root)
search_frame.pack(fill=tk.X, padx=10, pady=10)

search_frame.configure(borderwidth=2)

search_label = tk.Label(search_frame, text="Search for an Image:", font=("Arial", 14))
search_label.pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame, width=30, font=("Arial", 14))
search_entry.pack(side=tk.LEFT, padx=10)

browse_button = tk.Button(search_frame, text="Browse Folder", command=browse_folder)
browse_button.pack(side=tk.LEFT, padx=5, pady=5)

search_button = tk.Button(search_frame, text="Search", command=search_image, font=("Arial", 14))
search_button.pack(side=tk.LEFT, padx=5, pady=5)

search_result_frame = tk.Frame(root)
search_result_frame.pack(padx=10, pady=10)

search_result_label = tk.Label(search_result_frame, font=("Arial", 14))
search_result_label.pack()

search_label = tk.Label(root)
search_label.pack()

close_button = tk.Button(root, text="Close", command=root.quit)
close_button.pack(side=tk.BOTTOM, padx=10, pady=10)

explain_button = tk.Button(classify_frame, text="Explain", font=("Arial", 12), command=explain)
explain_button.pack(side=tk.LEFT, padx=(10,0))

root.mainloop()