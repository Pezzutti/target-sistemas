import json
from statistics import mean

with open('dados.json') as f:
    dados = json.load(f)

values = []

for day in dados:
    if day["valor"] != 0.0:
        values.append(day["valor"])

lowest = min(values)
print(f"Menor valor do mês: R$ {round(lowest, 2)}")
highest = max(values)
print(f"Maior valor do mês: R$ {round(highest, 2)}")

avg = mean(values)
above_avg = [x for x in values if x > avg]

print(f"Há {len(above_avg)} dias com faturamento acima da média mensal.")