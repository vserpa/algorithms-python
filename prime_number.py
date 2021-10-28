import math
import time

# Primo: somente dividido por 1 e ele mesmo
# Fatoração: divisão de um número não primo por primos
# divisor: qdo a divisão por um n não deixa resto
# saber se um número é primo: conhecer os divisores

# Source Eratóstenes: https://escolakids.uol.com.br/matematica/numeros-primos.htm
# Source usando loop: https://www.pythonprogressivo.net/2018/06/Primos-Python-Como-Saber-Numero-e-Primo.html

# crivo de eratóstenes
# para esta versão funcionar, são adicionados os ultimos divisores primos da sequência, um a um
def is_prime_eratostenes(number):
	if number == 1:
		return False

	if number == 2:
		return True

	# números pares não são primos (exceto o 2)
	if number % 2 == 0:
		return False

	if number == 3:
		return True

	# múltiplos de 3 não são primos (exceto o 3)
	if number % 3 == 0:
		return False

	if number == 5:
		return True

	# múltiplos de 5 não são primos (exceto o 5)
	if number % 5 == 0:
		return False

	if number == 7:
		return True

	# multiplos de 7 não são primos (exceto o 7)
	if number % 7 == 0:
		return False

	if number == 11:
		return True

	# multiplos de 11 não são primos (exceto o 11)
	if number % 11 == 0:
		return False

	if number == 13:
		return True

	if number % 13 == 0:
		return False

	return True

# esta implementação conta os multiplicadores do número
# diferente da anterior, ela não tem limite (não é necessário adicionar os primos manualmente)
def is_prime(number):

	if number == 1:
		return False
	
	mult = False
	
	for count in range(2, number):
		if (number % count == 0):
			mult = True
			break

	if mult:
		return False
	else:
		return True

def primes_gen(final_number):
	primes = [2]
	for n in range(3, final_number):
		if (is_prime(n)):
			primes.append(n)

	return primes


# no loop, works only 1 to 100
def is_prime_candidate(n):

	if (n == 2  or n == 3 or n == 5 or n == 7):
		return True

	if ((n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0)):
			return False
	
	qrd = math.sqrt(n)
		
	if (qrd % 1 == 0):
		return False
	
	return True


time_start = time.time()

is_correct = True

for number in range(1, 101):
    candidate_result = is_prime_candidate(number)
    system_result = is_prime(number)
    if (candidate_result != system_result):
        print('Number {} is prime: {}, expect {}'.format(number, candidate_result, system_result))
        is_correct = False

if (is_correct):
    print('All sounds good!')
else:
    print('Problems found!!!!')

print(primes_gen(200000))

time_end = time.time()
print("Executado em %.3f segundos" % (time_end - time_start))