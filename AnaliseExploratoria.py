import statistics

# valroes
valores = [33.33, 16.67, 8.33, 8.33, 4.17, 5.56, 5.56, 8.33, 14.29, 3.13]

# análise exploratória
media = statistics.mean(valores)
moda = statistics.mode(valores)
mediana = statistics.median(valores)

# resultados
print(f"Média: {media}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")