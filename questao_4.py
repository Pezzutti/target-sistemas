fats = {"SP":67836.43,
        "RJ":36678.66,
        "MG":29229.88,
        "ES":27165.48,
        "Outros":19849.53}

total = sum(fats.values())

percents = {"SP":0.0,
            "RJ":0.0,
            "MG":0.0,
            "ES":0.0,
            "Outros":0.0}

for item in fats:
    percents[item] = str(round(fats[item]/total*100, 2)) + '%'

print(percents)