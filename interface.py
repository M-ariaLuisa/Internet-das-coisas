import customtkinter as ctk
ctk.set_appearance_mode('dark')

#janela------------------------

janela = ctk.CTk()
janela.geometry('350x350')
janela.resizable(False,False)
janela.title('Sistema de Acesso - 2026')
janela.iconbitmap('security-protection-protect-key-password-login_108554.ico')
#------------------------------

#corpo da janela-----------------
titulo = ctk.CTkLabel(janela,
                      text='Sistema de login',
                      text_color='#37deb4',
                      font=('arial',40))
titulo.pack()

login = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     border_color='#37deb4',
                     placeholder_text='Digite o seu login',
                     
                     )
login.pack(pady=30)



senha = ctk.CTkEntry(janela,
                     width=400,
                     height=40,
                     border_color='#37deb4',
                     placeholder_text='Digite a sua senha',
                     show='🖤'
                     
                     )
senha.pack()

botao = ctk.CTkButton(janela,
                      width=200,
                      height=40,
                      text='Acessar',
                      fg_color='#37deb4',
                      text_color='black',
                      cursor = 'hand2',
                      font=('arial',30))
botao.pack(pady=30)


















janela.mainloop()
