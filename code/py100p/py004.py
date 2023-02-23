# 区间内所有的素数


# 是否素数
def is_primes(num):
    # 1是素数
    if num in (1, 2):
        return True
    for idx in range(2, num):
        if num % idx==0:
            return False
    return True


def print_primes(begin, end):
    # range [0,10) 不包括10的
    for num in range(begin, end + 1):
        if is_primes(num):
            print(f"{num} is a primes")


print_primes(11,25)