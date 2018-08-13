import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(0)  # initializing the choice, i.e. Python

languages = [
    ("Rotate_image"),
    ("Convert_to_black_and_white_image"),
    ("Blur_the_image"),
    ("Change_the_size"),
    ("Quit")
]

def ShowChoice():
  n=v.get()  
  if n == 0:
    #win = Toplevel()
    window = tk.Toplevel(root)
    tk.Label(window,
       text="""Choose :""",
       justify = tk.LEFT,
       padx = 20).pack()
    tk.Radiobutton(window,
             text="Left",
             padx = 20,
             variable=v,
             value=1).pack(anchor=tk.W)
    tk.Radiobutton(window,
             text="Right",
             padx = 20,
             variable=v,
             value=2).pack(anchor=tk.W)    
    
  else:
    quit()      


tk.Label(root, 
         text="""SELECT YOUR CHOICE:""",
         justify = tk.LEFT,
         padx = 50).pack()

for val, language in enumerate(languages):
  tk.Radiobutton(root, 
                  text=language,
                  indicatoron = 0,
                  width = 50,
                  padx = 50, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)

root.mainloop()

