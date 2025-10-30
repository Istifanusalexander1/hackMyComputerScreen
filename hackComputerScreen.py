from tkinter import *

screen = Tk()
t = True

screen.attributes('-fullscreen', t)
screen.attributes('-topmost', t)
screen.config(background='#000')

screen.protocol("WM_DELETE_WINDOW", lambda: None)

label = Label(
    screen,
    text="YOU ARE HACKED!",
    font=("Arial Black", 150, "bold"),
    fg="white",
    bg="#000"
)
label.pack(expand=True)

def handle_key(event):
    global t
    key = event.char.lower()

    if key == 'q':
        screen.destroy()
    elif key == 'c':
        t = False
        screen.attributes('-fullscreen', t)
        screen.attributes('-topmost', t)
        screen.geometry("600x400")
        screen.config(background='#222')
        label.config(bg='#222', fg='white', font=("Arial Black", 35, "bold"))

screen.bind("<Key>", handle_key)

screen.mainloop()
