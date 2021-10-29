from math import floor, log
import time

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

time_start = time.time()

primes = list(sieve_of_eratosthene(200000))

time_end = time.time()
print("Run in %.3f seconds" % (time_end - time_start))

print("Saída:", [primes[i] for i in [7, 1, 199999, 4]]) # Print: [19, 3, 2750159, 11]
