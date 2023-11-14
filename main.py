def main():
    print(exponentiation(11, 1000))


def exponentiation(base, power):
    power_in_binary = bin(power)[2:]
    print(f'{power_in_binary}')
    lenght_of_power_in_binary = len(power_in_binary)
    squares_of_base = [base]
    for _ in range(lenght_of_power_in_binary - 1):
        squares_of_base.append(squares_of_base[-1] * squares_of_base[-1])
    print(squares_of_base)
    result = 1
    for i, current_bit in enumerate(power_in_binary[::-1]):
        print(f'i {i}, bit {current_bit}')
        if current_bit == '1':
            result = result * squares_of_base[i]
    return result


if __name__ == '__main__':
    main()
