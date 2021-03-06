# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1,
# it is called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
#
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that there are 21 elements in this set.
#
# How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
#
# Answer:

import time


def main():
    start = time.time()
    file = open('../data/Problem102Triangles.txt')
    lines = file.read().split("\n")

    triangles = get_triangles(lines)
    triangles_containing_origin = 0

    for triangle in triangles:
        print(triangle)

    print("\nanswer: " + str(triangles_containing_origin))
    print("\ntook " + str(time.time() - start) + " seconds")


def get_triangles(lines):
    triangles = []

    for line in lines:
        if line == "":
            break

        triangle = [int(n) for n in line.split(",")]
        triangles.append(triangle)

    return triangles
 

if __name__ == '__main__':
    main()
