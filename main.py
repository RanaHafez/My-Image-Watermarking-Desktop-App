import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter.messagebox import askokcancel, showinfo


def size_ratio(old_size, fit_size):
    factor = min(float(fit_size[1]) / old_size[1], float(fit_size[0]) / old_size[0])
    width = int(old_size[0] * factor)
    height = int(old_size[1] * factor)
    return width, height


# TODO choosing a file
def open_file():
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=[("Image File", '.jpg')],
    )
    return filename


def show_image():
    image_name = open_file()
    image = Image.open(image_name)
    original_size = image.size
    new_size = size_ratio(original_size, (400, 400))
    # TODO adding the water mark
    image_d = ImageDraw.Draw(image)
    wm_size = int(original_size[0]/400)
    my_font = ImageFont.truetype('ZakirahsCasual.ttf', wm_size*30)
    image_d.text((23,36), "@RanaHafez", font=my_font, fill="#CCF3EE")

    # resizing the image to fit the required space
    image = image.resize(size_ratio(original_size, new_size))
    # showing the image
    tk_image = ImageTk.PhotoImage(image)
    my_img = tk.Label(image=tk_image)
    my_img.image = tk_image

    # resizing the image pack before saving
    image = image.resize(original_size)

    def save():
        # TODO Saving or cancelling
        answer = askokcancel(title='Confirmation.', message='Confirm saving the image.')
        if answer:
            # saving the image
            image.save(image_name)
            showinfo(
                title="Image Saved",
                message="Image is Saved"
            )
        if not answer:
            showinfo(
                title="Canceling",
                message="No Image is Saved."
            )
        # resetting the image back to normal
        my_img.image = ""
        save_button.pack_forget()
        my_img.pack_forget()

    save_button.config(command=save)
    my_img.pack()
    save_button.pack(pady=50)


# TODO the GUI Set-up
window = tk.Tk()
window.title('Add Water Mark')
window.geometry("500x600")
window.resizable(True, True)
window.config(bg="#F9F3EE")

img_space = tk.Label()
# a button for choosing an image
open_File_button = tk.Button(text="Open Image",width=30,command=show_image, bg="#97C4B8", fg="white")
open_File_button.pack(pady=50)
# a button for saving the selected image
save_button = tk.Button(text="save", bg="#F9CEEE", fg="black", width=30)

window.mainloop()