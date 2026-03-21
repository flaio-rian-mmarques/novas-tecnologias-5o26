def calcular_financiamento(preco, entrada, parcelas):
    valor_financiado = preco - entrada
    valor_total = valor_financiado * (1 + 1.5/100 * parcelas)
    parcela = valor_total / parcelas
    return parcela

preco_veiculo = float(input("Digite o preço do veículo: "))
valor_entrada = float(input("Digite o valor da entrada: "))
numero_parcelas = int(input("Digite o número de parcelas: "))

if (numero_parcelas > 72):
    print("Número de parcelas não pode ser maior que 72.")
else:
    print(f"Valor da parcela: {calcular_financiamento(preco_veiculo, valor_entrada, numero_parcelas):.2f}")