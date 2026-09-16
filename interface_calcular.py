import customtkinter as ctk

# Configuração da aparência
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

#funções-----------------------------

def calcular():
    d = int(distancia.get())
    c = float(consumo.get())
    p = float(preco.get())

    formula = (d/c)*p
    resultado.configure(text=f'O valor para a viagem é de R${formula:.2f}')

# Janela
janela = ctk.CTk()
janela.geometry('400x400')
janela.resizable(False, False)
janela.title('Sistema de Acesso - 2026')
janela.iconbitmap('3668862-car-drive-expenses-service_108021.ico')


# Título
titulo = ctk.CTkLabel(
    janela,
    text='APP VIAGEM',
    text_color='#f7f8fa',
    font=('Verdana', 30)
)
titulo.pack(pady=20)


# Distância
distancia = ctk.CTkEntry(
    janela,
    width=350,
    height=40,
    border_color='#f7f8fa',
    placeholder_text='Digite a distância da viagem em KM'
)
distancia.pack(pady=10)


# Consumo
consumo = ctk.CTkEntry(
    janela,
    width=350,
    height=40,
    border_color='#f7f8fa',
    placeholder_text='Digite o consumo do seu veículo'
)
consumo.pack(pady=10)


# Preço do combustível
preco = ctk.CTkEntry(
    janela,
    width=350,
    height=40,
    border_color='#f7f8fa',
    placeholder_text='Digite o preço atual do combustível'
)
preco.pack(pady=10)


# Botão
botao = ctk.CTkButton(
    janela,
    width=200,
    height=40,
    text='Calcular Gasto',
    text_color='black',
    fg_color='#f7f8fa',
    cursor='hand2',
    border_color='#cc1212',
    hover_color='#cc1212',
    border_width=2,
    font=('times new Roman', 20, 'bold'),
    command=calcular
)
botao.pack(pady=10)

resultado = ctk.CTkLabel(janela,
                      text='',
                      text_color='white',
                      font=('arial',20))
resultado.pack(pady=10)



# Executa a janela
janela.mainloop()
