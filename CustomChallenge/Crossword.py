import tkinter as tk

version = "1.0"
window = tk.Tk()

window.title("Crossword v.%s" % version)
# window.wm_iconbitmap("...")  # Uncomment when .ico is ready
window.geometry("640x640")
canvas = tk.Canvas(master=window, bg="#000000")

line = canvas.create_line(0, 0, 50, 50)

canvas.pack()
window.mainloop()
