import customtkinter as ctk
ctk.set_appearance_mode('dark')
#funçao-------------------------

def votacao():
    fb= float(cx1.get())
    lula = float(cx2.get())
    if(fb>lula):
        resultado.configure(text=f'Flavio bolsonaro ganhou')
    elif(fb<lula):
        resultado.configure(text=f'FLula ganhou')
    else:
        resultado.configure(text=f'Empate, teremos uma nova eleiçao')
        

#------------ Janela -------------
janela = ctk.CTk()
janela.geometry('600x450')
janela.title('Teste')
janela.resizable(False, False)
janela.iconbitmap('')

#------ Elementos da Janela ------

titulo = ctk.CTkLabel(
    janela,
    width=100,
    height=100,
    font=('Arial', 30),
    text_color="#FFFFFF",
    text='Eleições 2026'
)
titulo.pack()

cx1 = ctk.CTkEntry(
    janela,
    width=400,
    height=50,
    font=('Arial', 20),
    text_color="#FFFFFF",
    placeholder_text='Digite a porcetagem de FB'
)
cx1.pack(pady=10)

cx2 = ctk.CTkEntry(
    janela,
    width=400,
    height=50,
    font=('Arial', 20),
    text_color="#FFFFFF",
    placeholder_text='Digite a porcetagem de Lula'
)
cx2.pack(pady=10)

buttom1 = ctk.CTkButton(
    janela,
    text='Resultado',
    width=150,
    height=50,
    fg_color="#00DA1D",
    text_color="#FFFFFF",
    hover_color="#00A716",
    font=('Arial', 30),
    cursor='cross',
    command=votacao
)
buttom1.pack(pady=30)


resultado = ctk.CTkLabel(janela,
                         text='',
                         font=('arial',20),
                         text_color='white')
resultado.pack()
#---------------------------------
janela.mainloop()
