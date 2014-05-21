def e1():
    """Find the sum of all positive integers below 1000 divisible by 3 and 5."""
    return sum([i for i in range(1,1000) if i%3 == 0 or i%5 == 0])


def e2():
    """Find the sum of all even fibonacci numbers below 4,000,000."""
    def fib(max_fibval):
        sum_of_evens = 0
        a, b = 1, 2
        while b < max_fibval:
            a, b = b, a + b
            if a%2 == 0:
                sum_of_evens += a
        return sum_of_evens
    return fib(4000000)


def e3():
    """Find the largest prime factor of the number 600851475143."""
    def isPrime(number):
        i = 2
        while i*i <= number:
            if number % i == 0:
                return False
            i += 1
        return True

    def getFactors(number):
        i = 2
        factors = []
        while i <= number:
            if number % i == 0:
                number = number / i
                factors.append(i)
            else:
                i += 1
        return factors

    number = 600851475143
    max_prime = max([i for i in getFactors(number) if isPrime(i)])
    return max_prime


def e4():
    """Find the largest palindrome product resulting from 2 3-digit numbers."""
    def isPalindrome(number):
        number = str(number)
        while len(number) > 1:
            if number[0] != number[-1]:
                return False
            number = number[1:-1]
        return True

    max_pal = max([x*y for x in range(100,1000)
                   for y in range(100,1000) if isPalindrome(x*y)])
    return max_pal


def e5():
    """Find the smallest number that is divisible by 1 through 20."""
    def factor(number):
        factors = []
        i = 2
        while number > 1:
            if number % i == 0:
                number /= i
                factors.append(i)
            else:
                i += 1
        return factors

    def diff_factors(new_number, factors):
        """
        Find factors from new_number that aren't already present in
        the old_factors.
        """
        different_factors = []
        old_factors = factors[:] # Copied so that factors variable isn't changed
        new_factors = factor(new_number)
        while len(new_factors) > 0:
            if new_factors[-1] in old_factors:
                old_factors.remove(new_factors.pop())
            else:
                different_factors.append(new_factors.pop())
        return different_factors

    factors = []
    for i in range(1, 20):
        factors = factors + diff_factors(i, factors)
        total = 1
        for i in factors:
            total *= i
    return total


def e6():
    """Find the difference between the square of the sum and
    the sum of the squares of the numbers from 1 to 100."""
    def sq(x):
        return x * x
    return sq(sum(range(1, 101))) - sum([sq(x) for x in range(1, 101)])


def e7():
    """Find the 10,001st prime number."""
    def isPrime(number):
        i = 2
        while i * i <= number:
            if number % i == 0:
                return False
            i += 1
        return True

    prime_count = 1 # counts the number 2 as the first prime
    i = 1 # the number 3 is the first iteration, after check odds
    while prime_count < 10001:
        i += 2
        if isPrime(i):
            prime_count += 1
    return i


def e8():
    """Find the largest 13 digit product in the 1000-digit number."""
    with open("problem8.txt", "r") as file:
        text_list = file.read()
    text_list = text_list.split('\n')
    text = ""
    for line in text_list:
        text = text + line
    max = 0
    for i in range(0, len(text) - 13):
        total = 1
        for x in text[i:i + 13]:
            total = total * int(x)
            if total > max:
                max = total
    return max

