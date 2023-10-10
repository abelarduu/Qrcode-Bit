############
#QRcode Bit#
############
from customtkinter import *
from os.path import dirname
from PIL import Image
import pyqrcode

class Master(CTk):
    def __init__(self, width= int, height= int, title= str, resizable= bool):
        super().__init__()
        self.minsize(width,height)
        self.title(title)
        self.resizable(resizable,resizable)
        self.iconbitmap(dirname(__file__) +"\\resources/icon.ico")
        set_appearance_mode("Light")
        self.configure(fg_color="#66bcf2")
        
        self.rowconfigure(7, weight=6)
        self.columnconfigure(3, weight=3)

class Frame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.lbl1= CTkLabel(self, text="QRcode bit", font=("segoe ui black", 15))
        self.lbl1.grid(row=2,column=2,columnspan=3, padx=10)
        
        self.lbl2= CTkLabel(self, text="Link:", font=("segoe ui semibold", 15))
        self.lbl2.grid(row=3,column=2,columnspan=3, padx=10)

        self.linkEntry= CTkEntry(self, width= 250)
        self.linkEntry.grid(row=4,column=2,columnspan=3, padx=10)

        self.btnOk= CTkButton(self, text="Converter", width= 250, command= self.showQrcode)
        self.btnOk.grid(row=5, column=2,columnspan=3, padx=10,pady=10)

    def createQRcode(self):
        link = str(self.linkEntry.get())
        url= pyqrcode.create(link)
        img= url.png('Qrcode.png', scale= 4)
        
    def showQrcode(self):
        self.createQRcode()
        self.img =CTkImage(light_image=Image.open(dirname(__file__) +'/Qrcode.png'), size=(250,250))
        self.imglbl= CTkLabel(self, image= self.img, text= None)
        self.imglbl.grid(row=6, column=2,columnspan=3, padx=10, pady=10)

class App:
    def __init__(self):
        self.master= Master(350,450,"Qrcode Bit",True)
        self.frame= Frame(self.master)

        self.frame.grid(row=2,column=2,rowspan=7,columnspan=3)
        self.master.mainloop()

if __name__ =="__main__":
    App()