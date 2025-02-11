import matplotlib.pyplot as plt

# Definindo os valores
valor_total = 80  # valor total pago pelas 10 caixas
quantidade_caixas = 10  # número de caixas
lucro_desejado = 500  # lucro desejado

# Calculando o custo por caixa
custo_por_caixa = valor_total / quantidade_caixas

# Taxa de 0,4% sobre o valor total
taxa = 0.004  # 0,4% de taxa

# Calculando o valor adicional da taxa sobre o valor total
valor_taxa = valor_total * taxa

# Calculando o custo total, incluindo a taxa
custo_total_com_taxa = valor_total + valor_taxa

# Calculando o valor de venda total necessário para obter lucro desejado
valor_venda_necessario = custo_total_com_taxa + lucro_desejado

# Calculando o preço de venda por caixa necessário
preco_venda_por_caixa = valor_venda_necessario / quantidade_caixas

# Gerando os dados para o gráfico
caixas = [i for i in range(1, 11)]
precos = [(custo_total_com_taxa + lucro_desejado) / i for i in caixas]

# Criando o gráfico
plt.figure(figsize=(8, 6))
plt.plot(caixas, precos, marker='o', color='b', linestyle='-', label='Preço de Venda por Caixa')

# Adicionando título e rótulos aos eixos
plt.title("Preço de Venda por Caixa para Lucro de R$500", fontsize=14)
plt.xlabel("Número de Caixas", fontsize=12)
plt.ylabel("Preço de Venda por Caixa (R$)", fontsize=12)

# Exibindo a legenda
plt.legend()

# Mostrando o gráfico
plt.grid(True)
plt.show()
