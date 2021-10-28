# deve-se conhecer de antemão qual é o último primo dentro da cadeia de números primos a ser gerado
# ex: dentro de uma cadeia de 200.000 números primos, o maior primo é 2.750.159
from math import floor, log
import time

time_start = time.time()

def sieve_of_eratosthene(num_primes):

    # encontra-se o último número primo dentro de uma cadeia de números primos
    # ex: em uma cadeia de 200.000 primos, 2750159 é o último número primo encontrado
    LAST_PRIME_FOUND = floor(num_primes * log(num_primes) + num_primes * (log(log(num_primes))))

    prime_numbers = []

    # Cria-se uma lista referente a todos os inteiros entre 0 e N:
    A = [True] * (LAST_PRIME_FOUND + 1)

    # Define os números 0 e 1 como não primos:
    A[0] = A[1] = False

    # Percorra a lista até encontrar o primeiro número primo:
    for value, prime in enumerate(A):

        # O número é primo?
        if prime:

            # Retorna o número primo:
            prime_numbers.append(value)

            # Remova da lista todos os múltiplos do número encontrado:
            for i in range(value ** 2, LAST_PRIME_FOUND + 1, value):
                A[i] = False

    return prime_numbers

primes = list(sieve_of_eratosthene(200000))

time_end = time.time()
print("Executado em %.3f segundos" % (time_end - time_start))

print("Saída:", [primes[i] for i in [7, 1, 199999, 4]]) # Saída: [19, 3, 2750159, 11]
