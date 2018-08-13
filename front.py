import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("Rotate_image"),
    ("Convert_to_black_and_white_image"),
    ("Blur_the_image"),
    ("Change_the_size"),
    ("Quit")
]

def ShowChoice():
    print(v.get())

tk.Label(root, 
         text="""SELECT YOUR CHOICE:""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root, 
                  text=language,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)


root.mainloop()