import time

num = int(input("Type the limit number. Ex: 1000: "))
time_start = time.time()

print("Prime numbers between 0 and %i " % num)

primes_list = [2,]
print(primes_list[0])

def gen_prime_numbers_1(primes_list, num):

    # just odd numbers (not even)
    for x in range(3, num + 1, 2):
        num_divisoes = 0
        
        # pega o primeiro número e tenta dividi-lo pelos número primos menores que ele.
        for y in primes_list:
            
            # Quando o cociente for menor que o divisor para de testar números primos maiores.
            if x // y < y:
                break

            # Se der para dividir o número por algum número primo já descoberto então ele não é primo.
            if x % y == 0:
                # marca que ele não é primo.
                num_divisoes = 1
                break

        # se não tiver nenhuma divisão adiciona o número na lista de primos.
        if num_divisoes == 0:
            primes_list.append(x)
            print(x)
            num_divisoes = 0


gen_prime_numbers_1(primes_list, num)

print("Existe %i números primos entre 0 e %i" % (len(primes_list), num))

time_end = time.time()
print("Executado em %.3f segundos" % (time_end - time_start))