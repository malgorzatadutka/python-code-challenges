# find number's prime factors

def get_prime_factors(num):
    factors = list()
    divisor = 2
    while divisor <= num:
        if (num % divisor) == 0:
            factors.append(divisor)
            num = num / divisor
        else:
            divisor += 1
    return factors


if __name__ == '__main__':
    print("Hello!")
    condition = True
    while condition:
        print("Pass a number:")
        n = int(input())
        factors_list = get_prime_factors(n)
        print(f"Factors' list: {factors_list}")
        print(f"Do you want to try again? y/n")
        again = str(input())
        if again == 'y':
            print(f"Ok")
        elif again == 'n':
            print(f"Bye!")
            condition = False
        else:
            print(f"Wrong answer!")
            condition = False