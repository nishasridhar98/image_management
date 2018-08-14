import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image, ImageFilter

class FilesRenamerApp(tk.Tk):
    
    def __init__(self):
        
        tk.Tk.__init__(self)

        self.geometry("450x300+10+10")
        
        v = tk.IntVar()
        

        self.select = tk.Button(self, text="Choose File", command=self.on_choose)
        self.save = tk.Button(self, text="Save to Folder", command=self.on_save)
        self.run = tk.Button(self, text="Run", command=self.run)
        self.tb1 = tk.Text(self,width=40, height=1)
        self.tb2 = tk.Text(self,width=40, height=1)
        #self.tb3 = tk.Text(self,width=40, height=10, font="Verdana, 8")
        self.tb3 = tk.Label(self,text="""SELECT YOUR CHOICE:""",justify = tk.LEFT,width=40, height=1)
        self.tb4 = tk.Radiobutton(self,text="Rotate_the_image",variable=v,padx=20,justify = tk.LEFT,value=1,width=40, height=1)
        self.tb5 = tk.Radiobutton(self,text="Convert_to_black_and_white_image",variable=v,padx=20,justify = tk.LEFT,value=2,width=40, height=1)
        self.tb6 = tk.Radiobutton(self,text="Blur",variable=v,padx=20,justify = tk.LEFT,value=3,width=40, height=1)
        self.tb7 = tk.Radiobutton(self,text="Change_the_size",variable=v,padx=20,justify = tk.LEFT,value=4,width=40, height=1)
        self.tb8 = tk.Radiobutton(self,text="Quit",variable=v,padx=20,justify = tk.LEFT,value=5,width=40, height=1)

       


        self.tb1.grid(column=0,row=0)
        self.tb2.grid(column=0,row=1)
        self.tb3.grid(column=0,row=2)
        self.tb4.grid(column=0,row=3)
        self.tb5.grid(column=0,row=4)
        self.tb6.grid(column=0,row=5)
        self.tb7.grid(column=0,row=6)
        self.tb8.grid(column=0,row=7)


        self.select.grid(column=1,row=0, pady=10, padx=5)
        self.save.grid(column=1,row=1,padx=5)
        self.run.grid(column=1,row=3)


    def on_choose(self):
        self.from_dir = filedialog.askopenfilename() + "/" 
        self.tb1.insert("0.0", self.from_dir)

    def on_save(self):
        self.to_dir = filedialog.askdirectory() + "/"
        self.tb2.insert("0.0", self.to_dir)
    
    

    def run(self):
       v = tk.IntVar() 
       if v==0:
         im=Image.open(self.from_dir)


       elif v==1:
        im=Image.open(self.from_dir)
        im=im.convert(mode='L')

       elif v==2:
        im=Image.open(self.from_dir)
        im = im.filter(ImageFilter.BLUR)

       elif v==3:
        im=Image.open(self.from_dir)
        im.thumbnail(size)

       else:
        quit() 


app=FilesRenamerApp()
app.mainloop()
