# The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form
# 2^6972593 - 1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p - 1, have
# been found which contain more digits.
#
# However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433 x 2^7830457 + 1.
#
# Find the last ten digits of this prime number.
#
# Answer: 8739992577

import time


def main():
    start = time.time()

    i = 28433
    for j in range(1, 7830457 + 1):
        i *= 2
        i = i % 10_000_000_000
    i += 1

    print(str(i)[-10:])

    print("\ntook " + str(time.time() - start) + " seconds")


if __name__ == '__main__':
    main()
