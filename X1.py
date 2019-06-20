#Calculadora Nutricional
#Criador: Alexsandro Monteiro
#Data: 01/05/2017

from tkinter import *

window = Tk()
var1 = StringVar()
var2 = StringVar()

def bt_click():
    altura = float(ed1.get())
    peso = float(ed2.get())
    idade = int(ed3.get())
    alturacm = float(altura) * 100
    IMC_ = float(peso) / float(altura)**2
    Ideal1 = (float(altura) ** 2) * 18.5
    Ideal2 = (float(altura) ** 2) * 24.9
    print(altura)
    print(peso)
    print(idade)
    print("%.2f" %IMC_)
    print("%.2f" %Ideal1)
    print("%.2f" % Ideal2)

#--------------------------------------------
    if var2.get() == "Sedentário":
        atividade = 1.2
        if var1.get() == "M":
            sexoM = (66.5 + (13.75 * float(peso)) + (5 * float(alturacm)) - (6.7 * int(idade)))
            result = float(sexoM) * float(atividade)
            result_IMC["text"] = "%.2f" %IMC_
            result_TMB["text"] = "%.2f" %sexoM
            result_GET["text"] = "%.2f" %result
            result_Ideal_P["text"] = "%.0f" %Ideal1,"-","%.0f" % Ideal2
            print("%.2f" %sexoM)
            print("%.2f" %result)
            print("%.0f" %Ideal1, "-", "%.0f" %Ideal2)

        if var1.get() == "F":
            sexoF = (655.1 + (9.6 * float(peso)) + (1.85 * float(alturacm)) - (4.7 * int(idade)))
            result = float(sexoF) * float(atividade)
            result_IMC["text"] = "%.2f" %IMC_
            result_TMB["text"] = "%.2f" %sexoF
            result_GET["text"] = "%.2f" %result
            result_Ideal_P["text"] = "%.0f" % Ideal1, "-", "%.0f" % Ideal2
            print("%.2f" %sexoF)
            print("%.2f" %result)
            print("%.2f" % Ideal1," - ","%.2f" % Ideal2)
#---------------------------------------------

    if var2.get() == "Exercícios Leves":
        atividade = 1.375
        if var1.get() == "M":
            sexoM = (66.5 + (13.75 * float(peso)) + (5 * float(alturacm)) - (6.7 * int(idade)))
            result = float(sexoM) * float(atividade)
            result_IMC["text"] = "%.2f" %IMC_
            result_TMB["text"] = "%.2f" %sexoM
            result_GET["text"] = "%.2f" %result
            result_Ideal_P["text"] = "%.0f" %Ideal1,"-","%.0f" % Ideal2
            print("%.2f" %sexoM)
            print("%.2f" %result)
            print("%.0f" %Ideal1, "-", "%.0f" %Ideal2)

        if var1.get() == "F":
            sexoF = (655.1 + (9.6 * float(peso)) + (1.85 * float(alturacm)) - (4.7 * int(idade)))
            result = float(sexoF) * float(atividade)
            result_IMC["text"] = "%.2f" %IMC_
            result_TMB["text"] = "%.2f" %sexoF
            result_GET["text"] = "%.2f" %result
            result_Ideal_P["text"] = "%.0f" % Ideal1, "-", "%.0f" % Ideal2
            print("%.2f" %sexoF)
            print("%.2f" %result)
            print("%.2f" % Ideal1," - ","%.2f" % Ideal2)
#------------------------------------------------
    if var2.get() == "Moderado":
        atividade = 1.55
        if var1.get() == "M":
            sexoM = (66.5 + (13.75 * float(peso)) + (5 * float(alturacm)) - (6.7 * int(idade)))
            result = float(sexoM) * float(atividade)
            result_IMC["text"] = "%.2f" %IMC_
            result_TMB["text"] = "%.2f" %sexoM
            result_GET["text"] = "%.2f" %result
            result_Ideal_P["text"] = "%.0f" %Ideal1,"-","%.0f" % Ideal2
            print("%.2f" %sexoM)
            print("%.2f" %result)
            print("%.0f" %Ideal1, "-", "%.0f" %Ideal2)

        if var1.get() == "F":
            sexoF = (655.1 + (9.6 * float(peso)) + (1.85 * float(alturacm)) - (4.7 * int(idade)))
            result = float(sexoF) * float(atividade)
            result_IMC["text"] = "%.2f" %IMC_
            result_TMB["text"] = "%.2f" %sexoF
            result_GET["text"] = "%.2f" %result
            result_Ideal_P["text"] = "%.0f" % Ideal1, "-", "%.0f" % Ideal2
            print("%.2f" %sexoF)
            print("%.2f" %result)
            print("%.2f" % Ideal1," - ","%.2f" % Ideal2)

#--------------------------------------------------
    if var2.get() == "Exercícios Pesados":
        atividade = 1.725
        if var1.get() == "M":
            sexoM = (66.5 + (13.75 * float(peso)) + (5 * float(alturacm)) - (6.7 * int(idade)))
            result = float(sexoM) * float(atividade)
            result_IMC["text"] = "%.2f" %IMC_
            result_TMB["text"] = "%.2f" %sexoM
            result_GET["text"] = "%.2f" %result
            result_Ideal_P["text"] = "%.0f" %Ideal1,"-","%.0f" % Ideal2
            print("%.2f" %sexoM)
            print("%.2f" %result)
            print("%.0f" %Ideal1, "-", "%.0f" %Ideal2)

        if var1.get() == "F":
            sexoF = (655.1 + (9.6 * float(peso)) + (1.85 * float(alturacm)) - (4.7 * int(idade)))
            result = float(sexoF) * float(atividade)
            result_IMC["text"] = "%.2f" %IMC_
            result_TMB["text"] = "%.2f" %sexoF
            result_GET["text"] = "%.2f" %result
            result_Ideal_P["text"] = "%.0f" % Ideal1, "-", "%.0f" % Ideal2
            print("%.2f" %sexoF)
            print("%.2f" %result)
            print("%.2f" % Ideal1," - ","%.2f" % Ideal2)
#---------------------------------------------------

    if var2.get() == "Exercícios Muito Pesados":
        atividade = 1.9
        if var1.get() == "M":
            sexoM = (66.5 + (13.75 * float(peso)) + (5 * float(alturacm)) - (6.7 * int(idade)))
            result = float(sexoM) * float(atividade)
            result_IMC["text"] = "%.2f" %IMC_
            result_TMB["text"] = "%.2f" %sexoM
            result_GET["text"] = "%.2f" %result
            result_Ideal_P["text"] = "%.0f" %Ideal1,"-","%.0f" % Ideal2
            print("%.2f" %sexoM)
            print("%.2f" %result)
            print("%.0f" %Ideal1, "-", "%.0f" %Ideal2)

        if var1.get() == "F":
            sexoF = (655.1 + (9.6 * float(peso)) + (1.85 * float(alturacm)) - (4.7 * int(idade)))
            result = float(sexoF) * float(atividade)
            result_IMC["text"] = "%.2f" %IMC_
            result_TMB["text"] = "%.2f" %sexoF
            result_GET["text"] = "%.2f" %result
            result_Ideal_P["text"] = "%.0f" % Ideal1, "-", "%.0f" % Ideal2
            print("%.2f" %sexoF)
            print("%.2f" %result)
            print("%.2f" % Ideal1," - ","%.2f" % Ideal2)

if var2.get() == "":
        if var1.get() == "M":
            sexoM = (66.5 + (13.75 * float(peso)) + (5 * float(alturacm)) - (6.7 * int(idade)))
            print("%.2f" % sexoM)

        if var1.get() == "F":
            sexoF = (655.1 + (9.6 * float(peso)) + (1.85 * float(alturacm)) - (4.7 * int(idade)))
            print("%.2f" % sexoF)

#-----------------------------------------
combo1 = Spinbox(window, width=5, values=("M", "F"), textvariable=var1).place(x=120, y=180)
combo2 = Spinbox(window, width=18, values=("", "Sedentário", "Exercícios Leves","Moderado", "Exercícios Pesados", "Exercícios Muito Pesados"), textvariable=var2).place(x=120, y=150)

#---------------------------------

# Lista = Listbox(window, width=13, height=2)#, command=Lista_click)
# Lista.place(x=250, y=90)

lb1 = Label(window, text="CALCULADORA NUTRICIONAL", bg="black", foreground="white")
lb1['font']=('Arial','15','bold')

lb2 = Label(window, text="ALTURA (m)", bg="black", foreground="red")
lb2.place(x=30, y=50)

lb3 = Label(window, text="PESO (Kg)", bg="black", foreground="red")
lb3.place(x=30, y=80)

lb4 = Label(window, text="IDADE", bg="black", foreground="red")
lb4.place(x=30, y=110)

lb5 = Label(window, text="ATIVIDADES", bg="black", foreground="red")
lb5.place(x=260, y=150)

lb6 = Label(window, text="SEXO", bg="black", foreground="red")
lb6.place(x=260, y=180)
#-----------------------------------------------------------------
IMC = Label(window, text="IMC:", bg="gray", foreground="white")
IMC.place(x=260, y=50)

result_IMC = Label(window, text="", bg="black", foreground="white")
result_IMC.place(x=295, y=50)

TMB = Label(window, text="TMB:", bg="gray", foreground="white")
TMB.place(x=260, y=80)

result_TMB = Label(window, text="", bg="black", foreground="white")
result_TMB.place(x=295, y=80)

GET = Label(window, text="GET:", bg="gray", foreground="white")
GET.place(x=260, y=110)

result_GET = Label(window, text="", bg="black", foreground="white")
result_GET.place(x=295, y=110)

Ideal_P = Label(window, text="Peso_Ideal:", bg="gray", foreground="white")
Ideal_P.place(x=190, y=220)

result_Ideal_P = Label(window, text="", bg="black", foreground="white")
result_Ideal_P.place(x=280, y=220)

lb1.pack()

#---------------------------------------
ed1 = Entry(window)
ed1.place(x=120, y=50)

ed2 = Entry(window)
ed2.place(x=120, y=80)

ed3 = Entry(window)
ed3.place(x=120, y=110)

#-------------------------------------------------
bt = Button(window, width=7, text="Calcular", bg="yellow", command=bt_click)
bt.place(x=30, y=150)
bt['font']=('Arial','12','bold')

#------------------------------
window.wm_title("COMUNICATION_ARDUINO_SERIAL")
window["bg"]= "black"
window.geometry("350x250+800+120")

window.mainloop()




#============================
#============================




def status_check(self, var):
    if var == 1:
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