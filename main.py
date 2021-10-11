'''
 Returneaza true daca n este prim si false daca nu.
'''


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


'''
Returneaza produsul numerelor din lista lst.
'''


def get_product(lst):
    product = 1
    for x in lst:
        product = product * x
    return product


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''


def get_cmmdc_v1(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''


def get_cmmdc_v2(x, y):
    while y != 0:
        z = x % y
        x = y
        y = z
    return x


def main():
    print(is_prime(7))
    print(get_product([2, 3, 4, 5, 1]))
    print(get_cmmdc_v1(24, 60))
    print(get_cmmdc_v2(24, 60))


if __name__ == '__main__':
    main()
