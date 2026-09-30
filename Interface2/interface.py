import customtkinter as ctk

ctk.set_appearance_mode('light')


def calcular():
    try:
        n1 = float(nota1.get())
        n2 = float(nota2.get())
        n3 = float(nota3.get())

        media = (n1 + n2 + n3) / 3

        if media >= 5:
            resultado.configure(
                text=f'Aprovado! Média: {media:.1f}',
                text_color='#2E7D32'
            )
        else:
            resultado.configure(
                text=f'Reprovado! Média: {media:.1f}',
                text_color='#C62828'
            )
    except ValueError:
        resultado.configure(
            text='Digite apenas números válidos!',
            text_color='#C62828'
        )


FUNDO = '#FFF5F7'
ROSA = '#E85D8E'
ROSA_HOVER = '#D94F7A'
AMARELO = '#F6D365'
TEXTO = '#4A3B40'

janela = ctk.CTk()
janela.geometry('600x450')
janela.resizable(False, False)
janela.title('Sistema Escola')
janela.configure(fg_color=FUNDO)

titulo = ctk.CTkLabel(
    janela,
    text='Sistema Escola',
    text_color=ROSA,
    font=('Arial', 30, 'bold')
)
titulo.pack(pady=20)

nota1 = ctk.CTkEntry(
    janela,
    placeholder_text='Digite a nota da primeira unidade',
    border_color=AMARELO,
    text_color=TEXTO,
    width=400,
    height=45,
    font=('Arial', 18)
)
nota1.pack(pady=8)

nota2 = ctk.CTkEntry(
    janela,
    placeholder_text='Digite a nota da segunda unidade',
    border_color=AMARELO,
    text_color=TEXTO,
    width=400,
    height=45,
    font=('Arial', 18)
)
nota2.pack(pady=8)

nota3 = ctk.CTkEntry(
    janela,
    placeholder_text='Digite a nota da terceira unidade',
    border_color=AMARELO,
    text_color=TEXTO,
    width=400,
    height=45,
    font=('Arial', 18)
)
nota3.pack(pady=8)

botao = ctk.CTkButton(
    janela,
    width=200,
    height=45,
    text='Resultado',
    command=calcular,
    fg_color=AMARELO,
    hover_color='#EBC34F',
    text_color=TEXTO,
    cursor='hand2',
    font=('Arial', 22)
)
botao.pack(pady=25)

resultado = ctk.CTkLabel(
    janela,
    text='',
    text_color='black',
    font=('arial', 25)
)
resultado.pack(pady=10)

janela.mainloop()