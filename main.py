from tkinter import *
from PIL import Image, ImageTk
import requests

def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=300, height=414)
# Load the background image using Pillow
pil_background_img = Image.open("background.png")
background_img = ImageTk.PhotoImage(pil_background_img)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Load the Kanye button image using Pillow
pil_kanye_img = Image.open("kanye.png")
kanye_img = ImageTk.PhotoImage(pil_kanye_img)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
