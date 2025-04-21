import math

# Verificando se um número é primo
def numPrimo(num):
    if (num % 2) == 0 and num > 2: 
        return "Este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Este número não é primo"
    return "Este número é primo"


numPrimo(541)