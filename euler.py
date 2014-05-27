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


def e9():
    """Find the product of the pythagorean triplet that satisfies these
    constraint: a < b < c and a + b + c == 1000"""
    def isTriangle(a, b, c):
        return a*a + b*b == c*c

    for a in range(1, 333):
        for b in range(1, 500):
            c = 1000 - b - a
            if isTriangle(a, b, c):
                return a*b*c
    return "No match"


def e10():
    """Find the sum of all the primes below 2,000,000"""
    def isPrime(number):
        """A faster prime finder that only iterates for odd numbers."""
        if number % 2 == 0 and number != 2:
            return False
        elif number in [1, 4, 6, 8, 9]:
            return False
        i = 3
        while i*i <= number:
            if number % i == 0:
                return False
            i += 2
        return True

    primes_sum = sum([i for i in range(2, 2000000) if isPrime(i)])
    return primes_sum


def e11():
    """In a 20 by 20 grid, find the largest product of 4 adjacent numbers."""
    def text_to_matrix(text):
        """Function assumes the text is separated with spaces and \n's.
        Returns a list of integers."""
        array = ' '.join(text.split('\n')).split()
        array = [int(element) for element in array]
        return array

    def get_max_horiz(matrix):
        max = 0
        for row in range(20):
            for col in range(17):
                first_element = row*20 + col
                product = 1
                for i in range(4):
                    product *= matrix[first_element + i]
                if product > max:
                    max = product
        return max

    def get_max_vert(matrix):
        max = 0
        for row in range(17):
            for col in range(20):
                first_entry = row*20 + col
                product = 1
                for i in range(4):
                    product *= matrix[first_entry + i*20]
                if product > max:
                    max = product
        return max

    def get_max_diag1(matrix):
        """Top left to bottom right diagonal."""
        max = 0
        for row in range(17):
            for col in range(17):
                first_entry = row*20 + col
                product = 1
                for i in range(4):
                    product *= matrix[first_entry + i*20 + i]
                if product > max:
                    max = product
        return max

    def get_max_diag2(matrix):
        """Top right to bottom left diagonal."""
        max = 0
        for row in range(17):
            for col in range(3, 20):
                first_entry = row*20 + col
                product = 1
                for i in range(4):
                    product *= matrix[first_entry + i*20 - i]
                if product > max:
                    max = product
        return max

    def get_max_product(matrix):
        return max(get_max_horiz(matrix), get_max_vert(matrix),
                   get_max_diag1(matrix), get_max_diag2(matrix))

    with open('problem11.txt') as file:
        text = file.read()
    matrix = text_to_matrix(text)
    return get_max_product(matrix)


def e12():
    """The nth triangle number would be: 1 + 2 + ... + (n-1) + n.
    Find the first triangle number with over 500 divisors."""
    class Adder(object):
        """Used to generate the next triangle number."""
        def __init__(self):
            self.triangle_number = 1
            self.incrementer = 2

        def next_triangle_number(self):
            self.triangle_number += self.incrementer
            self.incrementer += 1
            return self.triangle_number

    def number_of_divisors(number):
        divisors = []
        i = 1
        while i*i <= number:
            if number % i == 0:
                divisors.append(i)
                divisors.append(number // i)
            i += 1
        return len(divisors)

    adder = Adder()
    while True:
        if number_of_divisors(adder.next_triangle_number()) > 500:
            return adder.triangle_number


def e13():
    """Find the largest sum of the first 10 digits for 100 50-digit numbers."""
    with open('problem13.txt') as file:
        text = file.read()
    return max([int(line[:11])for line in text.split('\n')])


def e14():
    """If n is even, n -> n // 2.
    If n is odd, n -> 3*n + 1.
    If we start with 5, the chain is 5 -> 16 -> 8 -> 4 -> 2 -> 1.
    Find the starting number under 1,000,000 that yields the longest chain."""
    def chain_length(number):
        chain_size = 1
        while number > 1:
            if number % 2 == 0:
                number /= 2
            else:
                number = 3 * number + 1
            chain_size += 1
        return chain_size

    max_chain = 1
    for i in range(800000, 1000000):
        if chain_length(i) > max_chain:
            max_chain = chain_length(i)
            max_starting_number = i
    return max_starting_number


# I need to think of a more efficient way to solve this problem
# Gets too slow on grids bigger than 10 by 10
def e15():
    """Find how many paths exist in a 20 by 20 grid."""
    def get_paths(x, y, width):
        if x == width or y == width:
            return 1
        else:
            return get_paths(x+1, y, width) + get_paths(x, y+1, width)
    return get_paths(1, 1, 21)


def e16():
    """Find the sum of the digits of 2^1000."""
    return sum([int(i) for i in str(2 ** 1000)])


def e20():
    """Find the sum of the digits of 100! (100 factorial)."""
    def factorial(n):
        total = 1
        for i in range(1, n+1):
            total *= i
        return total

    return sum([int(i) for i in str(factorial(100))])


def e21():
    """Let d(n) be the sum of the divisors of n.
    If d(b) = a and d(a) = b, where a != b,
    then a and b are an amicable pair.
    Find the sum of all amicable numbers under 10,000."""
    def divisors(n):
        divs = [1]
        i = 2
        while i*i <= n:
            if n % i == 0:
                divs.append(i)
                # Gets rid of the possibility of adding the same number twice
                # since i and n // i are the same number when i*i == n
                if i*i != n:
                    divs.append(n // i)
            i += 1
        return divs

    def d(n):
        return sum(divisors(n))

    def is_amicable(n, d_list):
        # d(n) == m and d(m) == n and n != m
        if d_list[n] < len(d_list):
            m = d_list[n]
        if n == d_list[m]:
            return True
        return False

    d_list = [d(n) for n in range(1, 10000)]
    print(len(d_list))
    return sum([i for i in d_list if is_amicable(i, d_list)])


def e22():
    with open('names.txt') as file:
        names = sorted(file.read().split('","'))
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 0
    name_number = 0
    for name in names:
        name_number += 1
        for letter in name:
            total = total + ( name_number * (alphabet.index(letter) + 1) )
    return total


def e48():
    """Find the last 10 digits of the sum of 1**1, 2**2, ... 1000**1000."""
    return str(sum([i**i for i in range(1, 1001)]))[-10:]


def e92():
    """A number chain is created by adding the sum of the squares of each
    digit in a number. All number chains converge to either 1 or 89.
    Find how many numbers below 10,000,000 arrive at 89."""
    def sum_sq_digits(n):
        return sum([int(i)*int(i) for i in str(n)])

    def find_converge_89(lower, upper, arrive1, arrive89):
        """Returns amount of numbers who converge in the lower to upper
        range specified."""
        for i in range(lower, upper):
            n = i
            if n in arrive1:
                i += 1
            elif n in arrive89:
                convergence_89 += 1
                i += 1
            else:
                n = sum_sq_digits(n)
        return convergence_89

    def create_arrive_lists():
        arrive1 = [1]
        arrive89 = [89, 145, 42, 20, 4, 16, 37, 58]
        for i in range(2, 100000):
            chain = []
            if i in arrive1:
                arrive1 = arrive1 + chain
                return False
            elif i in arrive89:
                arrive89 = arrive89 + chain
                return True
            else:
                chain.append(i)
                i = sum_sq_digits(i)
        return arrive1, arrive89

    arrive1, arrive89 = create_arrive_lists()
    return find_converge_89(10000, 10000000, arrive1, arrive89) + len(arrive89)

