#http://www.facom.ufu.br/~wendelmelo/terceiros/ModuloC.pdf

#CURSO:     AULA DE PYTHON
#ASSUNTO:   ORIENTAÇÃO A OBJETO COM PYTHON TKINTER
#CRIADO:    22/05/2019

'''
import functools
import tkinter as t

class Tela(t.Frame):
    def __init__(self, parent, nome):
        t.Frame.__init__(self, parent)
        self.nome = nome
        t.Label(self, text='Voce esta na ' + self.nome).pack()

class Menu(t.Frame):
    def __init__(self, parent, *subtelas):
        t.Frame.__init__(self, parent)
        self.current_frame = self
        for subtela in subtelas:
            t.Button(subtela, text='Voltar',
                command=functools.partial(self.muda_tela, self)).pack()
            t.Button(self, text=subtela.nome,
                command=functools.partial(self.muda_tela, subtela)).pack()

    def muda_tela(self, qual):
        self.current_frame.pack_forget()
        qual.pack()
        self.current_frame = qual

if __name__ == '__main__':
    root = t.Tk()
    root.resizable(0, 0)
    t1 = Tela(root, 'Primeira tela')
    t2 = Tela(root, 'Segunda tela')
    t3 = Tela(root, 'Terceira tela')

    m = Menu(root, t1, t2, t3)
    m.pack()

    root.mainloop()
'''


from tkinter import *

class Sistema:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.menu = Menu(master)
        self.menuCadastro = Menu(self.menu)
        self.menuCadastro.add_command(label='Clientes')
        self.menuCadastro.add_command(label='Fornecedores')
        self.menuCadastro.add_command(label='Estoque')
        self.menu.add_cascade(labe='Cadastro', menu=self.menuCadastro)
        self.menuConsulta = Menu(self.menu)
        self.menuConsulta.add_command(label='Cliente')
        self.menuConsulta.add_command(label='Fornecedores')
        self.menuConsulta.add_command(label='Estoque')
        self.menu.add_cascade(labe='Consulta', menu=self.menuConsulta)
        master.config(menu=self.menu)

root = Tk()
root.geometry('600x400')
Sistema(root)
root.mainloop()



'''
from tkinter import *

class FirstWindow(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Primeira Janela')
        self.configure(background='green')
        self.geometry('480x240')


class SecondWindow(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Segunda Janela')
        self.configure(background='darkgray')
        self.geometry('480x240')


class ThirdWindow(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela principal
        self.title('Terceira Janela')
        self.configure(background='yellow')
        self.geometry('480x240')


class MainWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, master=None)

        # Configuração da janela principal
        self.master.title('Janela Principal')
        self.master.geometry('480x240')
        self.configure(borderwidth=4)
        self.configure(background='white')

        for name in ("button1", "button2", "button3"):
            self.button = Button(self, text=name)
            self.button.bind("<Button-1>", self.handle_event)
            self.button.pack(side='left', fill='x', expand=True)

        # Empacotamos o frame principal
        self.pack(fill='both', expand=True)

    def handle_event(self, event):
        btn_name = event.widget.cget('text')
        if btn_name.endswith('1'):
            window = FirstWindow()
        if btn_name.endswith('2'):
            window = SecondWindow()
        if btn_name.endswith('3'):
            window = ThirdWindow()

        window.mainloop()


if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.mainloop()
'''