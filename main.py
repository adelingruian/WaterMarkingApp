import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont

MAIN_FONT = ("Helvetica", 8, "normal")

def add_watermark(imported_image, watermark):
    """Adds the watermark on the image, then saves the file in the same folder with a new name:
    <old_name>-watermark.<old_extension>, then displays the image"""
    with Image.open(imported_image) as image:
        image_width, image_height = image.size
        draw = ImageDraw.Draw(image)

        font_size = int(image_width/8)
        font = ImageFont.truetype("arial.ttf", font_size)
        x, y = int(image_width/2), int(image_height/2)

        draw.text((x, y), watermark, font=font, fill='#FFF', anchor='ms')
        save_path = '-watermark.'.join(imported_image.split('.'))
        result_label.config(text=f"Image succesfully saved at: {save_path}.")
        image.save(save_path)
        image.show()

def get_images_path():
    """Gets image path from a fieldialog, and stores it in the entry"""
    filetypes = (
        ('Images', '*.jpg'),
        ('All files', '*.*')
    )
    images_path = tk.filedialog.askopenfilename(title="Select images", initialdir='/', filetypes=filetypes)
    images_path_entry.insert(0, images_path)

def start_watermark():
    """Checks for fields to not be empty, then calls the add_watermark function """
    if watermark_entry.get() == "":
        messagebox.showerror(title="Opss", message="You need to type in a watermark text.")
        return
    elif len(watermark_entry.get()) > 10:
        messagebox.showerror(title="Opss", message="The watermark must have less then 10 characters.")
        return
    if images_path_entry.get() == "":
        messagebox.showerror(title="Opss", message="You need to specify a file first.")
        return

    add_watermark(images_path_entry.get(), watermark_entry.get())

window = tk.Tk()
window.title("WaterMarking App")
window.config(width=400, height=600, padx=100, pady=20)

title_frame = tk.Frame()
title_frame.grid(row=1, column=1, columnspan=1)
title_label = tk.Label(title_frame, text='WaterMarking', font=("Helvetica", 24, "italic"))
title_label.grid(row=1, column=1)
title_label2 = tk.Label(title_frame, text='App', font=("Helvetica", 24, "bold"))
title_label2.grid(row=1, column=2)

field_frame = tk.Frame(pady=50)
field_frame.grid(row=2, column=1, columnspan=1)
images_path_label = tk.Label(field_frame, text= "Image Path: ", font=MAIN_FONT,)
images_path_label.grid(row=1, column=1)
images_path_entry = tk.Entry(field_frame, width='30')
images_path_entry.grid(row=1, column=2)
images_path_button = tk.Button(field_frame, text='Select image', font=MAIN_FONT, command=get_images_path)
images_path_button.grid(row=1, column=3)


watermark_label = tk.Label(field_frame, text='Type your watermark:', font=MAIN_FONT)
watermark_label.grid(row=2, column=1)
watermark_entry = tk.Entry(field_frame, width='42')
watermark_entry.grid(row=2, column=2, columnspan=2)

result_label = tk.Label(text="", font=MAIN_FONT, fg='red')
result_label.grid(row=3, column=1)
watermark_button = tk.Button(text='Add watermark', font=MAIN_FONT, command=start_watermark)
watermark_button.grid(row=4, column=1)



window.mainloop()

