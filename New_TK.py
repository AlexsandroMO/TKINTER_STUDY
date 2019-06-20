# http://www.facom.ufu.br/~wendelmelo/terceiros/ModuloC.pdf

# CURSO:     AULA DE PYTHON
# ASSUNTO:   ORIENTAÇÃO A OBJETO COM PYTHON TKINTER
# CRIADO:    22/05/2019

#Limpar labels

from functools import partial
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tinydb import TinyDB, Query, where
import numpy as np
#
# class Sistema:
#     def __init__(self, master=None):
#         Toplevel.__init__(self, master=master)
#
#         self.frame = Frame(master)
#         self.frame.pack()
#         self.menu = Menu(master)
#         self.menuCadastro = Menu(self.menu)
#         self.menuCadastro.add_command(label='Clientes')
#         self.menuCadastro.add_command(label='Fornecedores')
#         self.menuCadastro.add_command(label='Estoque')
#         self.menu.add_cascade(labe='Cadastro', menu=self.menuCadastro)
#         self.menuConsulta = Menu(self.menu)
#         self.menuConsulta.add_command(label='Cliente')
#         self.menuConsulta.add_command(label='Fornecedores')
#         self.menuConsulta.add_command(label='Estoque')
#         self.menu.add_cascade(labe='Consulta', menu=self.menuConsulta)
#         master.config(menu=self.menu)

class FirstWindow(Toplevel):
    def bt_click(self, button):
        print(button['text'], '\n')

        if button['text'] == 'Registrar':
            db2 = TinyDB('db2.json')

            if self.ed_firstname.get() != '' and self.ed_secondname.get() != '' and self.ed_var.get() != '' and self.ed_var2.get() != '' and self.ed_var3.get() != '' and self.ed_var4.get() != '' and self.ed_cpf.get() != '' and self.ed_email.get() != '' and self.ed_password.get() != '' and self.ed_confirmpass.get() != '' and self.ed_cel.get() != '':

                if len(self.ed_password.get()) < 6:
                    messagebox.showinfo("Atenção!", 'Sua senha precisa ser igual ou maior a 6 dígitos')
                    self.ed_password.delete(0, 'end')

                elif self.ed_password.get() != self.ed_confirmpass.get():
                    messagebox.showinfo("Atenção!", 'Senhas não são identicas')
                    self.ed_password.delete(0, 'end')
                    self.ed_confirmpass.delete(0, 'end')

                elif len(self.ed_cpf.get()) > 11 or len(self.ed_cpf.get()) < 11 or type(int(self.ed_cpf.get())) != int:
                    messagebox.showinfo("Atenção!", 'CPF informado é inválido')
                    self.ed_cpf.delete(0, 'end')

                elif len(self.ed_cel.get()) > 11 or len(self.ed_cel.get()) < 11 or type(
                        int(self.ed_cel.get())) != int:
                    messagebox.showinfo("Atenção!", 'Celular informado é inválido')
                    self.ed_cel.delete(0, 'end')

                else:

                    dados = {
                        'FirstName': self.ed_firstname.get().upper(),
                        'SecondName': self.ed_secondname.get().upper(),
                        'Date_day': self.ed_var2.get(),
                        'Date_month': self.ed_var3.get(),
                        'Date_year': self.ed_var4.get(),
                        'Gender': self.ed_var.get(),
                        'CPF': self.ed_cpf.get(),
                        'Email': self.ed_email.get(),
                        'Senha': self.ed_password.get(),
                        'Confirm': self.ed_confirmpass.get(),
                        'Cel': self.ed_cel.get()
                    }

                    db2.insert(dados)

                    print(db2.all())

                    lb_result = Label(self, text='Cadastro Realizado com Sucesso')
                    lb_result.place(x=100, y=350)

                    self.ed_firstname.delete(0, 'end')
                    self.ed_secondname.delete(0, 'end')
                    self.ed_cpf.delete(0, 'end')
                    self.ed_email.delete(0, 'end')
                    self.ed_password.delete(0, 'end')
                    self.ed_confirmpass.delete(0, 'end')
                    self.ed_cel.delete(0, 'end')
                    self.combo.delete(0, 'end')
                    self.combodata1.delete(0, 'end')
                    self.combodata2.delete(0, 'end')
                    self.combodata3.delete(0, 'end')

            else:
                enter_list = [self.ed_firstname.get(), self.ed_secondname.get(), self.ed_var2.get(), self.ed_var3.get(),self.ed_var4.get(), self.ed_var.get(),
                              self.ed_cpf.get(), self.ed_email.get(), self.ed_password.get, self.ed_confirmpass.get(),
                              self.ed_cel.get()]

                list_applications = ['Primeiro Nome', 'Segundo Nome', 'Data de Nascimento', 'Genero', 'CPF', 'Emial', 'Senha', 'Confirmar Senha', 'Cel']

                cont = 0
                for a in enter_list:
                    if a == '':
                        messagebox.showinfo("Atenção!",
                                            'O item {} precisa ser Preenchido.'.format(list_applications[cont]))
                    cont += 1

    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        # Configuração da janela de Cadastro
        self.title('Janela Cadastro')

        self.ed_var = StringVar()
        self.ed_var2 = StringVar()
        self.ed_var3 = StringVar()
        self.ed_var4 = StringVar()

        self.lb_firstname = Label(self, text='Primeiro Nome:')
        self.lb_firstname.place(x=30, y=70)

        self.ed_firstname = Entry(self, width=20)
        self.ed_firstname.place(x=170, y=70)

        self.lb_secondname = Label(self, text='Segundo Nome:')
        self.lb_secondname.place(x=30, y=100)

        self.ed_secondname = Entry(self, width=20)
        self.ed_secondname.place(x=170, y=100)

        self.lb_date = Label(self, text='Data de Nascimento:')
        self.lb_date.place(x=30, y=130)

        d = np.arange(1, 32, 1)
        dia = []

        for a in d:
            dia.append(a)
            self.combodata1 = ttk.Combobox(self, width=5, textvariable=self.ed_var2)
            self.combodata1['value'] = (dia)
            self.combodata1.grid(column=1, row=0)
            self.combodata1.place(x=170, y=130)

        mes = 'Janeiro, Fevereiro, Março, Abril, Maio, Junho, Julho, Agosto, Setembro, Outubro, Novembro, Dezembro'

        self.combodata2 = ttk.Combobox(self, width=10, textvariable=self.ed_var3)
        self.combodata2['value'] = (mes.split(','))
        self.combodata2.grid(column=1, row=0)
        self.combodata2.place(x=230, y=130)

        a_ = np.arange(1935, 2020, 1)
        ano = []

        for a in a_:
            ano.append(a)
            self.combodata3 = ttk.Combobox(self, width=5, textvariable=self.ed_var4)
            self.combodata3['value'] = (ano)
            self.combodata3.grid(column=1, row=0)
            self.combodata3.place(x=320, y=130)

        self.lb_gender = Label(self, text='Gênero:')
        self.lb_gender.place(x=30, y=160)

        self.combo = ttk.Combobox(self, width=10, textvariable=self.ed_var)
        self.combo['value'] = ('Masculino', 'Feminino')
        self.combo.grid(column=1, row=0)
        self.combo.place(x=170, y=160)

        self.lb_cpf = Label(self, text='CPF:')
        self.lb_cpf.place(x=30, y=190)

        self.ed_cpf = Entry(self, width=20)
        self.ed_cpf.place(x=170, y=190)

        self.lb_cel = Label(self, text='Cel:')
        self.lb_cel.place(x=30, y=220)

        self.ed_cel = Entry(self, width=20)
        self.ed_cel.place(x=170, y=220)

        self.lb_email = Label(self, text='Email:')
        self.lb_email.place(x=30, y=250)

        self.ed_email = Entry(self, width=20)
        self.ed_email.place(x=170, y=250)

        self.lb_password = Label(self, text='Senha:')
        self.lb_password.place(x=30, y=280)

        self.ed_password = Entry(self, width=20)
        self.ed_password["show"] = "*"
        self.ed_password.place(x=170, y=280)

        self.lb_confirmpass = Label(self, text='Confimar Senha:')
        self.lb_confirmpass.place(x=30, y=310)

        self.ed_confirmpass = Entry(self, width=20)
        self.ed_confirmpass["show"] = "*"
        self.ed_confirmpass.place(x=170, y=310)

        self.bt_enter = Button(self, width=7, text='Registrar', command=self.bt_click)
        self.bt_enter['command'] = partial(self.bt_click, self.bt_enter)
        self.bt_enter.place(x=30, y=380)

        self.configure(background='green')
        self.geometry('450x450')


class SecondWindow(Toplevel):

    def convertTextDate(self, date_day, date_month, date_year):
        return date_day + ' de ' + date_month + ' de ' + date_year

    def convertCPF(self, cpfnumber):
        return cpfnumber[:len(cpfnumber) -8:] + '.' + cpfnumber[3:len(cpfnumber) -5:] + '.' + cpfnumber[6:len(cpfnumber) -2:] + '-' + cpfnumber[9:len(cpfnumber):]

    def convertCEL(self, celnumber):
        return '(' + celnumber[:len(celnumber)-9:] + ') ' + celnumber[2:len(celnumber)-4:] + '-' + celnumber[7:len(celnumber):]

    def bt_click2(self, button):
        print(button['text'], '\n')
        print(self.ed_name_search.get())

        if self.ed_name_search.get() != '':

            db2 = TinyDB('db2.json')

            if button['text'] == 'Localizar':
                print(db2.all())

                search = db2.search(where('FirstName') == self.ed_name_search.get().upper())

                for a in range(0, len(search)):
                    cpfnumber = search[a]['CPF']
                    celnumber = search[a]['Cel']
                    date_day = search[a]['Date_day']
                    date_month = search[a]['Date_month']
                    date_year = search[a]['Date_year']

                    self.lb_firstname = Label(self, text='Primeiro Nome:             {}'.format(search[a]['FirstName']))
                    self.lb_firstname.place(x=30, y=150)

                    self.lb_secondname = Label(self, text='Segundo Nome:             {}'.format(search[a]['SecondName']))
                    self.lb_secondname.place(x=30, y=180)

                    self.lb_date = Label(self, text='Data de Nascimento:    {}'.format(self.convertTextDate(date_day, date_month, date_year)))
                    self.lb_date.place(x=30, y=210)

                    self.lb_gender = Label(self, text='Gênero:                           {}'.format(search[a]['Gender']))
                    self.lb_gender.place(x=30, y=240)

                    self.lb_cpf = Label(self, text='CPF:                                {}'.format(self.convertCPF(cpfnumber)))
                    self.lb_cpf.place(x=30, y=270)

                    self.lb_cel = Label(self, text='Cel:                                  {}'.format(self.convertCEL(celnumber)))
                    self.lb_cel.place(x=30, y=300)

                    self.lb_email = Label(self, text='Email:                              {}'.format(search[a]['Email']))
                    self.lb_email.place(x=30, y=330)

                    self.lb_choice = Checkbutton(self, text='Editar Dados', variable=self.ed_var5, command=self.status_check)
                    self.lb_choice.grid(column=0, row=0)
                    self.lb_choice["font"] = ("Arial", "8", "bold")
                    self.lb_choice['command'] = partial(self.status_check, self.lb_choice)
                    self.lb_choice.place(x=30, y=370)

                    self.ed_name_search.delete(0, 'end')

                    self.geometry('350x420')

        else:
            self.geometry('380x150')

    def bt_click3(self, button):
        print(button['text'], '\n')
        if button['text'] == 'Limpar':
            self.lb_firstname.destroy()
            self.lb_secondname.destroy()
            self.lb_date.destroy()
            self.lb_gender.destroy()
            self.lb_cpf.destroy()
            self.lb_cel.destroy()
            self.lb_email.destroy()
            self.lb_choice.destroy()

            self.geometry('350x150')

    #Checkbutton

    def status_check(self, button):

        print(self.ed_var5)

        #self.ed_var5 = 1

        if self.ed_var5 == 1:
            self.ed_firstname = Entry(self, width=20)
            self.ed_firstname.place(x=290, y=150)

            self.ed_secondname = Entry(self, width=20)
            self.ed_secondname.place(x=290, y=180)

            d = np.arange(1, 32, 1)
            dia = []

            for a in d:
                dia.append(a)
                self.combodata1 = ttk.Combobox(self, width=5, textvariable=self.ed_var2)
                self.combodata1['value'] = (dia)
                self.combodata1.grid(column=1, row=0)
                self.combodata1.place(x=290, y=210)

            mes = 'Janeiro, Fevereiro, Março, Abril, Maio, Junho, Julho, Agosto, Setembro, Outubro, Novembro, Dezembro'

            self.combodata2 = ttk.Combobox(self, width=10, textvariable=self.ed_var3)
            self.combodata2['value'] = (mes.split(','))
            self.combodata2.grid(column=1, row=0)
            self.combodata2.place(x=345, y=210)

            a_ = np.arange(1935, 2020, 1)
            ano = []

            for a in a_:
                ano.append(a)
                self.combodata3 = ttk.Combobox(self, width=5, textvariable=self.ed_var4)
                self.combodata3['value'] = (ano)
                self.combodata3.grid(column=1, row=0)
                self.combodata3.place(x=430, y=210)

            self.combo = ttk.Combobox(self, width=10, textvariable=self.ed_var)
            self.combo['value'] = ('Masculino', 'Feminino')
            self.combo.grid(column=1, row=0)
            self.combo.place(x=290, y=240)

            self.ed_cpf = Entry(self, width=20)
            self.ed_cpf.place(x=290, y=270)

            self.ed_cel = Entry(self, width=20)
            self.ed_cel.place(x=290, y=300)

            self.ed_email = Entry(self, width=20)
            self.ed_email.place(x=290, y=330)

            self.ed_confirmemail = Entry(self, width=20)
            self.ed_confirmemail.place(x=290, y=360)

            self.bt_enter = Button(self, width=7, text='Atualizar', command=self.bt_clickX)
            self.bt_enter["font"] = ("Arial", "10", "bold")
            self.bt_enter['command'] = partial(self.bt_clickX, self.bt_enter)
            self.bt_enter.place(x=260, y=100)

            self.geometry('500x420')

            self.ed_var5 = 0

        else:
            self.ed_var5 = 1

            self.ed_firstname.destroy()
            self.ed_secondname.destroy()
            self.combo.destroy()
            self.combodata1.destroy()
            self.combodata2.destroy()
            self.combodata3.destroy()
            self.ed_cpf.destroy()
            self.ed_cel.destroy()
            self.ed_email.destroy()
            self.ed_confirmemail.destroy()
            self.bt_enter.destroy()

    def bt_clickX(self, button):
            print(button['text'], '\n')
            if button['text'] == 'Atualizar':
                print('OK')




    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.title('Janela Busca de Usuários')

        V = StringVar(self, value='')

        self.ed_var = StringVar()
        self.ed_var2 = StringVar()
        self.ed_var3 = StringVar()
        self.ed_var4 = StringVar()
        self.ed_var5 = StringVar()

        #self.ed_var5 = 0

        self.lb_name_serch = Label(self, width=20, text='Localizar do Usuário')
        self.lb_name_serch["font"] = ("Arial", "10", "bold")
        self.lb_name_serch.place(x=30, y=70)

        self.ed_name_search = Entry(self, textvariable=V, width=20)
        self.ed_name_search.place(x=200, y=70)

        self.bt_enter2 = Button(self, width=7, text='Localizar', command=self.bt_click2)
        self.bt_enter2["font"] = ("Arial", "10", "bold")
        self.bt_enter2['command'] = partial(self.bt_click2, self.bt_enter2)
        self.bt_enter2.place(x=30, y=100)

        self.bt_enter3 = Button(self, width=7, text='Limpar', command=self.bt_click3)
        self.bt_enter3["font"] = ("Arial", "10", "bold")
        self.bt_enter3['command'] = partial(self.bt_click3, self.bt_enter3)
        self.bt_enter3.place(x=260, y=100)

        self.configure(background='darkgray')
        self.geometry('350x150')

class ThirdWindow(Toplevel):


    def __init__(self, master=None):
        Toplevel.__init__(self, master=master)

        self.title('Janela A Definir')
        self.configure(background='gray')
        self.geometry('390x150')

class MainWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, master=None)

        # Configuração da janela principal

        self.master.title('Menu')
        self.master.geometry('300x100')
        self.configure(borderwidth=4)
        self.configure(background='black')

        for name in ('Cadastro', 'Consulta', 'Edição'):
            self.button = Button(self, text=name)
            self.button.bind("<Button-1>", self.handle_event)
            self.button.pack(side='left', fill='x', expand=True)

        # Empacotamos o frame principal
        self.pack(fill='both', expand=True)

    def handle_event(self, event):
        btn_name = event.widget.cget('text')
        if btn_name.endswith('Cadastro'):
            window = FirstWindow()
        if btn_name.endswith('Consulta'):
            window = SecondWindow()
        if btn_name.endswith('Edição'):
            window = ThirdWindow()

        window.mainloop()

if __name__ == '__main__':
    mainWindow = MainWindow()
    mainWindow.mainloop()
