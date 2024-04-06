from tkinter import *
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageDraw, ImageFont

class Watermarker:
    def __init__(self, window):
        self.window = window
        self.window.title('Image Watermarker')

        self.label = Label(window, text='Select an image to watermark:')
        self.label.grid(column=1, row=1)
        self.window.config(pady=20, padx=20)
        self.select_button = Button(window, text='Select Image', command=self.select_image)
        self.select_button.grid(column=0, row=2)
        self.save_button = Button(window, text='Save Image', command=self.save_image)
        self.save_button.grid(column=2, row=2)
        self.watermarked_image = None

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if file_path:
            original_image = Image.open(file_path).convert('RGBA')
            watermark = Image.open('watermark2.png').convert('RGBA')
            watermark_resized = watermark.resize(original_image.size)

            # Blend the watermark image with the original image
            watermarked_image = Image.alpha_composite(original_image, watermark_resized)

            # Save or display the watermarked image
            watermarked_image.show()

            self.watermarked_image = watermarked_image

    def save_image(self):
        # Save the image
        if self.watermarked_image:
            save_path = filedialog.asksaveasfilename(defaultextension=".png")
            if save_path:
                self.watermarked_image.save(save_path)

if __name__ == "__main__":
    root = Tk()
    watermarker = Watermarker(root)
    root.mainloop()