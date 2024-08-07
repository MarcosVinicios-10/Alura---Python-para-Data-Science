"""
2 Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. 
Considere que a colônia A inicia com 4 elementos e a B com 10.
"""
A = 4
B = 10

for e in range(1, 100000000000000):
    A = A + ((A * 3)/100)
    B = B + ((B*1.5)/100)

    if A >= B:
        print(f'Levaram {e} dias para que a colônia A fosse maior ou ou igual a colônia B,\n A:\t {A:.2f} bactérias.\n B:\t {B:.2f} Bactérias.')
        break