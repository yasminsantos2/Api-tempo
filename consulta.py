from clima import buscar_clima   # o MESMO miolo

cidade = input("Digite o nome da cidade: ")
dados = buscar_clima(cidade)

print()
print(f"Clima em {dados['cidade']}:")
print(f"  Temperatura: {dados['temperatura']}°C")
print(f"  Sensação: {dados['sensacao']}°C")
print(f"  Umidade: {dados['umidade']}%")
print(f"  Descrição: {dados['descricao']}")