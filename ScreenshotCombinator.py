import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageOps
import os

def convertToGrayscaleAndCombine(images):
    gray_images = [ImageOps.grayscale(image) for image in images]
    
    gray_images[0].save('combined.pdf', 'PDF', resolution=100.0, save_all=True, append_images=gray_images[1:])
    return 'combined.pdf'

def selectImagesAndConvert():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(
        title='Select Images',
        filetypes=[('Image Files', '*.png *.jpg *.jpeg')]
    )
    
    if not file_paths:
        return
    
    images = [Image.open(path) for path in file_paths]
    output_pdf_path = convertToGrayscaleAndCombine(images)
    current_path = os.getcwd()
    tk.messagebox.showinfo("Success", f"PDF saved as {current_path}\{output_pdf_path}")

if __name__ == "__main__":
    selectImagesAndConvert()
