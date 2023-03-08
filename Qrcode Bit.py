####################################################################
# QRcode Bit - Aplicativo para conversão de links/textos em Qrcode #
####################################################################
#Importações
from tkinter import *
from tkinter.ttk import *
from os.path import dirname

#Janela(Container Pai)
class Master(Tk):
    def __init__(self, title= str, width= int, height=int, resizable= bool):
        super().__init__()
        self.title(title)                                                   #Titulo da janela
        self.geometry(f"{width}x{height}")                                  #Tamanho da janela
        self.minsize(width, height)                                         #Tamanho minino da janela
        self.iconbitmap(dirname(__file__) + '\\resources/icon.ico')         #icone
        self.config(bg="white")                                           #background
        #self.config(bg="#A557BB")                                           #background
        self.style()                                                        #Estilo dos widgets da janela
        #Verificação do redimensionamento da janela
        if resizable:
            self.resizable(True, True)
        else:
            self.resizable(False,False)

    """
        #DEFINIÇÃO DOS ESTILOS DO WIDGETS
        Esta função:
            -Padroniza todos widgets( oferecendo o mesmo estilo a cada um)
    """
    def style(self):
        self.style = Style(self)
        self.style.configure('.',background= 'white', padding=(0,10),font=("Helvetica", 15))   #configurando todos Widgets

#Interface Grafica da janela
class App:
    def __init__(self,master):
        #Configurando Grid
        master.columnconfigure(3, weight=3)
        master.rowconfigure(6, weight=6)

        self.QrcodeImg= BooleanVar(False)   #variavel boleana para a inserção da imagem QRcode
        #label Titulo
        self.lbl1= Label(master, text="QRcode bit", background= 'white')
        self.lbl1.grid(row=1,column=2,columnspan=3)
        
        #label "link"
        self.lbl1= Label(master, text="Link:")
        self.lbl1.grid(row=2,column=2,columnspan=3)

        #Caixa de entrada
        self.linkEntry= Entry(master, width= 40)
        self.linkEntry.grid(row=3,column=2,columnspan=3)

        #Botão
        self.btnOk= Button(master, text="Converter", cursor="hand2", command= self.showQrcode)
        self.btnOk.grid(row=4, column=2,columnspan=3)

    """
        #CRIAÇÃO VISUAL DO QRCODE
        Esta função:
            -Recebe o link inserido no caixa de entrada
            -Cria um QRcode do link
            -Cria um arquivo .PNG para a visualização do QRcode
    """
    def createQRcode(self):
        #importações necessárias 
        import pyqrcode

        link = str(self.linkEntry.get())        #Obtendo Link
        url= pyqrcode.create(link)              #criando QRcode
        img= url.png('Qrcode.png', scale= 4)    #criando QRcode no formato .PNG
        
    """ 
        #EXIBIÇÃO DO QRCODE NA INTERFACE
        Esta Função:
            -Chama a função "createQRcode()" para criação do QRcode
            -Pega a imagem do QRcode gerada
            -Adiciona a imagem na interface(janela)
    """
    def showQrcode(self):
        self.createQRcode()
        #img
        self.img =PhotoImage(file=dirname(__file__) +'\\Qrcode.png')
        self.QrcodeImg.set(True)
        self.imglbl= Label(master, image= self.img)
        self.imglbl.grid(row=5, column=2,columnspan=3)
##########################################
#Verificação de execução direta do módulo#
##########################################
if __name__ =="__main__":
    master= Master("Qrcode bit", 350,450,False)    #Instanciando/criando a janela
    app= App(master)                               #adicionando widgets na interface da janela
    master.mainloop()                              #verificação de de eventos em loop infinito
    