import time

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

time_start = time.time()

print(primes_gen(100))

time_end = time.time()
print("Executado em %.3f segundos" % (time_end - time_start))