#!/usr/bin/python3
"""Is winner module"""


def isWinner(x, nums):
    """Is Winner Function"""
    if x <= 0 or nums is None or len(nums) == 0:
        return

    # A helper function to perform the Sieve of Eratosthenes
    def sieve(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not primes
        for start in range(2, int(n**0.5) + 1):
            if sieve[start]:
                for i in range(start * start, n + 1, start):
                    sieve[i] = False
        return [i for i, is_prime in enumerate(sieve) if is_prime]

    # Prepare the prime sieve for all possible rounds
    max_n = max(nums)
    primes = sieve(max_n)

    # Cache to store results of rounds for quicker access
    maria_wins = 0
    ben_wins = 0

    # Simulate each game round
    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        # Count the number of prime numbers <= n
        prime_count = 0
        for prime in primes:
            if prime > n:
                break
            prime_count += 1

        # Maria wins if prime_count is odd, Ben wins if even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
