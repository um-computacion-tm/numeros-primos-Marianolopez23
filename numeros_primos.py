def is_prime(valor):
    divisor = valor - 1
    while divisor>1:
        if valor%divisor==0:
            return False
        divisor=divisor-1
    return True