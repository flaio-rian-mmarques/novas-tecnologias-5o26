# lista de veículos
frota = [
    
]

print("Cadastro de Veículos") #inicia o programa

# laço para cadastrar os veículos, o usuário pode digitar 'sair' para encerrar o cadastro
while True:
    # solicita as informações do veículo ao usuário
    marca = input("Digite a marca do veículo (ou 'sair' para encerrar): ")
    if marca.lower() == 'sair': #verifica se o usuário deseja encerrar o cadastro
        break
    modelo = input("Digite o modelo do veículo: ")
    ano = input("Digite o ano do veículo: ")
    placa = input("Digite a placa do veículo: ")
    valor = input("Digite o valor do veículo: ")

    # cria um dicionário para armazenar as informações do veículo e adiciona à frota
    veiculo = {
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'placa': placa,
        'valor': valor
    }
    
    frota.append(veiculo)
    print(f"\n{modelo} cadastrado com sucesso!\n")

# exibe a frota de veículos cadastrados
print("\nFrota de Veículos Cadastrados:")

#calcula a soma dos valores dos veículos e, depois, exibe a média
soma = 0

for veiculo in frota:
    print(f"Marca: {veiculo['marca']}, Modelo: {veiculo['modelo']}, Ano: {veiculo['ano']}, Placa: {veiculo['placa']}, Valor: {veiculo['valor']}")
    soma += float(veiculo['valor'])

print(f"\nMédia dos valores dos veículos: {soma / len(frota):.2f}")

for veiculo in frota:
    if float(veiculo['valor']) > soma / len(frota): #verifica se o valor do veículo é maior que a média
        print(f"Veículo com valor acima da média: {veiculo['modelo']} - Valor: {veiculo['valor']}")