def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2 if num2 != 0 else "Erro: Divisão por zero"
    else:
        return 0

# Soma
resultado1 = calculadora(10, 5, 1)  
# Subtração
resultado2 = calculadora(10, 5, 2)  
# Multiplicação
resultado3 = calculadora(10, 5, 3)  
# Divisão
resultado4 = calculadora(10, 5, 4)  
# Operação inválida
resultado5 = calculadora(10, 5, 5)  

print(resultado1)  
# 15
print(resultado2)  
# 5
print(resultado3)  
# 50
print(resultado4)  
# 2.0
print(resultado5)  
# 0