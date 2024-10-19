while True:
    temperatura = int(input("Qual a temperatura desejada? (Digite -1 para desligar o chuveiro): "))
    
    if temperatura == -1:
        print("Chuveiro desligado.")
        break  # O loop termina quando o usuário deseja desligar
    
    if temperatura < 20:
        print("Está muito frio. Ajuste a temperatura.")
    elif 20 <= temperatura <= 35:
        print("Chuveiro funcionando normalmente.")
    else:
        print("Chuveiro está muito quente. Ajuste a temperatura.")