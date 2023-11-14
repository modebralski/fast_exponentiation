def main():
    base = 3
    power = 29
    print(f"{base}^{power} = {exponentiation(base, power)}")


def exponentiation(base, power):
    power_in_binary = bin(power)[2:]
    print(f'{power_in_binary}')
    lenght_of_power_in_binary = len(power_in_binary)
    squares_of_base = [base]
    for _ in range(lenght_of_power_in_binary - 1):
        squares_of_base.append(squares_of_base[-1] * squares_of_base[-1])
    print(squares_of_base)
    result = 1
    for square_of_base, current_bit in enumerate(power_in_binary[::-1]):
        if current_bit == '1':
            result = result * squares_of_base[square_of_base]
            print(f'{base}^{2 ** square_of_base} * {current_bit} = {squares_of_base[square_of_base]}, result = {result}')
        else:
            print(f'{base}^{2 ** square_of_base} * 0 = 1, result = {result}')
    return result


if __name__ == '__main__':
    main()
