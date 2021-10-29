# Primo: somente dividido por 1 e ele mesmo
# Fatoração: divisão de um número não primo por primos
# divisor: qdo a divisão por um n não deixa resto
# saber se um número é primo: conhecer os divisores

# Source Eratóstenes: https://escolakids.uol.com.br/matematica/numeros-primos.htm

# o método utiliza a teoria do crivo de eratóstenes
# para esta versão funcionar, são adicionados os ultimos divisores primos da sequência, um a um
# é uma implementação ingênua e deve ser usada apenas para fins educacionais
def is_prime(number):
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

    # multiplos de 13 não são primos (exceto o 13)
	if number % 13 == 0:
		return False

	return True


number = 377
print("{} is prime: {}".format(number, is_prime(number)))