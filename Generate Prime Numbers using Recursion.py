def is_prime(n, i=2):
    if i * i > n:
        return n > 1
    if n % i == 0:
        return False
    return is_prime(n, i+1)

def generate_primes(n, current=2):
    if current > n:
        return
    if is_prime(current):
        print(current, end=" ")
    generate_primes(n, current+1)

generate_primes(20)
