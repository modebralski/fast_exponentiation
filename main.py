def main():
    exponentiation(2, 10)


def exponentiation(base, power):
    power_in_binary = bin(power)
    for bit in power_in_binary[2:]:
        print(bit)


if __name__ == '__main__':
    main()
