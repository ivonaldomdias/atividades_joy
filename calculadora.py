def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2 if num2 != 0 else "Erro!"
    else:
        return 0

# adição
conta1 = calculadora(10, 6, 1)  
# Subtração
conta2 = calculadora(10, 4, 2)  
# Multiplicação
conta3 = calculadora(10, 9, 3)  
# Divisão
conta4 = calculadora(10, 43, 4)  
# Teste erro
conta5 = calculadora(10, 11, 5)  

print(conta1)  
# 15
print(conta2)  
# 5
print(conta3)  
# 50
print(conta4)  
# 2.0
print(conta5)  
# 0
