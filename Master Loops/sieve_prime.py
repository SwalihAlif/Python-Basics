def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    primes = [i for i in range(n+1) if is_prime[i]]
    return primes


n = 50
print(sieve_of_eratosthenes(n))