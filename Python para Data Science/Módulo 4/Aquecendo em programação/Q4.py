# 4 Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.
média = 0
x = 0
while True:
    temp = float(input('Insira ums temperatura, -273°C encerra:'))
    média += temp
    x += 1
    if temp == -273:
        break

print(f'A média é {média/x:.2f}°C')