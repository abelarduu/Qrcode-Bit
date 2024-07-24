from src import MASTER
from pathlib import Path
from customtkinter import *
from PIL import Image
import pyqrcode

class QRCodeFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#f2f2f2")
        
        self.lbl2 = CTkLabel(self, text="Link:", font=("segoe ui black", 15))
        self.lbl2.grid(row=2, column=2, columnspan=3, padx=10)

        self.linkEntry = CTkEntry(self, width=250)
        self.linkEntry.grid(row=3, column=2, columnspan=3, padx=5)

        self.btnOk = CTkButton(self, text="Converter", width=250, command=self.show_qrcode)
        self.btnOk.grid(row=4, column=2, columnspan=3, padx=10, pady=10)

    def create_qrcode(self):
        """Cria o QR code a partir do link inserido"""
        link = str(self.linkEntry.get())
        url = pyqrcode.create(link)
        url.png('Qrcode.png', scale=4)

    def show_qrcode(self):
        """Mostra o QR code gerado na tela"""
        self.create_qrcode()
        self.img = CTkImage(light_image=Image.open(Path(__file__).parent / 'Qrcode.png'), size=(250, 250))
        self.imglbl = CTkLabel(self, image=self.img, text=None)
        self.imglbl.grid(row=5, column=2, columnspan=3, padx=10, pady=10)
        
class App:
    def __init__(self):
        """Inicializa a aplicação"""
        # Frame principal para centralizar o app
        MAIN_FRAME = CTkFrame(MASTER, fg_color= "white")
        MAIN_FRAME.grid(row=3, column=2, rowspan=7, columnspan=3, pady=10)

        # Adiciona a imagem do logo ao MASTER
        self.img = CTkImage(light_image=Image.open(Path(__file__).parent / 'src/assets/logo.png'), size=(267, 64))
        self.imglbl = CTkLabel(MAIN_FRAME, image=self.img, text=None)
        self.imglbl.grid(row=1, column=2, columnspan=3, padx=10, pady=10)
                
        # Instancia o QRCodeFrame e adiciona na tela
        self.qr_frame = QRCodeFrame(MAIN_FRAME)
        self.qr_frame.grid(row=3, column=2, columnspan=3, padx=10, pady=10)
        
        # Inicia o loop principal
        MASTER.mainloop()

if __name__ == "__main__":
    App()
