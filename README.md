# Image Classifier - BTech Mini Project

This project is an image classification tool built using Python, TensorFlow, and Tkinter. It enables users to classify images based on the VGG16 model, search for images by category within a folder, and provides a brief Wikipedia summary of the predicted class. A voice assistant feature reads the summary aloud, with threading enabled for smooth performance.

## Features

- **Image Classification**: Select an image and classify it using the VGG16 model pre-trained on ImageNet.
- **Folder Image Search**: Search for images within a folder by specifying a category or term.
- **Class Explanation**: Receive a summary explanation of the classified image from Wikipedia, read aloud via text-to-speech.
- **Threading Support**: Background tasks, such as reading summaries, are handled in separate threads to keep the interface responsive.
- **GUI**: User-friendly interface created with Tkinter.

## Requirements

- Python 3.x
- TensorFlow
- Keras
- Pillow (PIL)
- Tkinter (comes pre-installed with Python)
- pyttsx3 (for text-to-speech)
- wikipedia-api

Install the required packages:
```bash
pip install tensorflow pillow pyttsx3 Wikipedia
```
## Features:

- **Classify Image**: Click "Select Image" to load and classify an image.
- **Search for an Image**: Enter a term in the search box, select a folder, and click "Search" to locate images matching the term.
- **Explain Class**: After classification, click "Explain" to get a brief summary read aloud about the classified category.
  
## Project Structure
- `image classifier.py`: Main script with the GUI and functions for image classification, search, threading, and Wikipedia summaries.
- `test/`: Folder for storing any additional resources such as pictures to classify (if needed).

## Acknowledgements
- **VGG16 Model**: The model is pre-trained on the ImageNet dataset for image classification tasks.
- **Wikipedia**: Provides a summary of the classified image category.
