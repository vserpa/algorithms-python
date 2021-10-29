import math

# correct method
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


# candidate method
def is_prime_candidate(n):

	if (n == 2  or n == 3 or n == 5 or n == 7):
		return True

	if ((n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0)):
			return False
	
	qrd = math.sqrt(n)
		
	if (qrd % 1 == 0):
		return False
	
	return True

# check if a candidate method is correct
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