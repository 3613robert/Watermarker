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
            original_image = Image.open(file_path)

            # Create a blank image with RGBA mode
            watermark_image = Image.new("RGBA", original_image.size, (255, 255, 255, 0))

            # Draw the watermark text on the blank image
            draw = ImageDraw.Draw(watermark_image)
            font = ImageFont.truetype("arial.ttf", 150)  # Adjust font size and type
            watermark_text = "Watermark"
            draw.text((10, 10), watermark_text, fill=(255, 255, 255, 128), font=font)

            # Blend the watermark image with the original image
            watermarked_image = Image.alpha_composite(original_image.convert("RGBA"), watermark_image)

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