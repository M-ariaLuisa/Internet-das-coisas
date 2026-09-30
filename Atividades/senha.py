#programa que simula o cadastro de uma senha de 4 digitos, e verifica se tem esse requisito
#além disso, verifica se a senha é composta apenas por numeros
#caso não seja,a senha não é aceita e a pessoa deve digitar novamente

senha = input('Digite uma senha de 4 digitos: ')
while len(senha) != 4 or not senha.isdigit():
    print('Senha inválida. A senha deve ter 4 dígitos e ser composta apenas por números.')
    senha = input('Digite uma senha de 4 digitos: ')
print('Senha cadastrada com sucesso!')