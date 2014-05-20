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


