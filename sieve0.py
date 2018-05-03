"""
Implement the Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    answer = list(range(2, bound))

    for divisor in range(2, bound):
        # remove all multiple of divisor from answer
        for i in range(len(answer)):
            if answer[i] != 1:
                if answer[i] != divisor:
                    if answer[i] % divisor == 0:
                        answer[i] = 1
    
    return([num for num in answer if num != 1])

print(len(compute_primes(200)))
print(len(compute_primes(2000)))
