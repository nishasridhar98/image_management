import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python
root.geometry("450x300+10+10")

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
        text= """SELECT YOUR CHOICE:""",
        justify = tk.LEFT,
        padx = 20,
        pady = 20).grid()

def choose(root):  
  root.from_dir = filedialog.askdirectory() + "/" 


root.select = tk.Button(root, text="Choose Folder", command=choose)
#root.save

root.select.grid(column=1,row=30, pady=10, padx=5)




for val, language in enumerate(languages):
   tk.Radiobutton(root,
                 text=language,
                 padx = 20,
                 variable=v,
                 command=ShowChoice,
                 value=val).grid()


root.mainloop()


