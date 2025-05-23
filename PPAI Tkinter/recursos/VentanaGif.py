# archivo: recursos/VentanaGif.py
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

class VentanaGif(tk.Toplevel):
    def __init__(self, gif_path):
        super().__init__()
        self.title("Visualización Animada del Sismo")
        self.geometry("600x600")
        self.label = tk.Label(self)
        self.label.pack()

        self.frames = []
        self.load_gif(gif_path)
        self.animate(0)

    def load_gif(self, path):
        gif = Image.open(path)
        self.frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)]

    def animate(self, index):
        self.label.configure(image=self.frames[index])
        self.after(100, lambda: self.animate((index + 1) % len(self.frames)))
