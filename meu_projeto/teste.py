import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def limpar():
    txtcodigo.delete(0,"end")
    txtnome.delete(0,"end")
    txttelefone.delete(0,"end")
    txtemail.delete(0,"end")
    txtobservacao.delete("1.0","end")
    txtcodigo.focus_set()

def gravar():
    messagebox.showinfo("Aviso", "Dados Gravado com Sucesso",parent = tela_cli)
    limpar()


# Criando a janela principal
tela_cli = tk.Tk()
tela_cli.title("Cadastro de Cliente")
#tela_cli.geometry("1920x1080")
tela_cli.state('zoomed')
tela_cli.configure(bg="yellow")

tkimage = ImageTk.PhotoImage(Image.open(r"C:\Temp\fundo_menu.jpg").resize((tela_cli.winfo_screenwidth(), tela_cli.winfo_screenheight())))
tk.Label(tela_cli, image=tkimage).pack()

lblcodigo = tk.Label(tela_cli, text ="Codigo:", bg="whitesmoke", fg="black", font=('Calibri', 12), anchor = "w")
lblcodigo.place(x = 50, y = 60, width=85, height = 25)

txtcodigo = tk.Entry(tela_cli, width = 35, font=('Calibri', 12))
txtcodigo.place(x = 150, y = 60, width = 100, height = 25)

buscabtn = tk.Button(tela_cli, text ="Pesquisar", 
                      bg ='white',foreground='black', font=('Calibri', 12, 'bold'))
buscabtn.place(x = 280, y = 60, width = 90, height = 25)

lblnome = tk.Label(tela_cli, text ="Nome:", bg="whitesmoke", fg="black", font=('Calibri', 12), anchor = "w")
lblnome.place(x = 50, y = 100, width=85, height = 25)

txtnome = tk.Entry(tela_cli, width = 35, font=('Calibri', 12))
txtnome.place(x = 150, y = 100, width = 360, height = 25)

lbltelefone = tk.Label(tela_cli, text ="Telefone:", bg="whitesmoke", fg="black", font=('Calibri', 12), anchor = "w")
lbltelefone.place(x = 50, y = 140, width=85, height = 25)

txttelefone = tk.Entry(tela_cli, width = 35, font=('Calibri', 12))
txttelefone.place(x = 150, y = 140, width = 360, height = 25)

lblemail = tk.Label(tela_cli, text ="E-mail:", bg="whitesmoke", fg="black", font=('Calibri', 12), anchor = "w")
lblemail.place(x = 50, y = 180, width=85, height = 25)

txtemail = tk.Entry(tela_cli, width = 35, font=('Calibri', 12))
txtemail.place(x = 150, y = 180, width = 360, height = 25)

lblobservacao = tk.Label(tela_cli, text ="Observacao:", bg="whitesmoke", fg="black", font=('Calibri', 12), anchor = "w")
lblobservacao.place(x = 50, y = 220, width=85, height = 25)

txtobservacao= tk.Text(tela_cli, font=('Calibri', 12))
txtobservacao.place(x=150, y=220, width=360, height=80)

btngravar = tk.Button(tela_cli, text ="Gravar", 
                       bg ='black',foreground='white', font=('Calibri', 12, 'bold'), command = gravar) 
btngravar.place(x = 150, y = 320, width = 65)

btnexcluir = tk.Button(tela_cli, text ="Excluir", 
                       bg ='red',foreground='white', font=('Calibri', 12, 'bold'))
btnexcluir.place(x = 250, y = 320, width = 65)

btnlimpar = tk.Button(tela_cli, text ="Limpar", 
                       bg ='green',foreground='white', font=('Calibri', 12, 'bold'), command = limpar)
btnlimpar.place(x = 350, y = 320, width = 65)

btnmenu = tk.Button(tela_cli, text ="Menu", 
                       bg ='yellow',foreground='black', font=('Calibri', 12, 'bold'))
btnmenu.place(x = 450, y = 320, width = 65)

txtcodigo.focus_set()

tela_cli.mainloop()
