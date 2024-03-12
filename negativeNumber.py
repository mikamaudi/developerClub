def Binary_conversions():
    num = int(input("enter a num"))
    bit_size = int(input("enter a bit size"))

    num = bin(num)[2:].zfill(bit_size)

    inverse_number = ''

    for bit in num:
        if bit == '0':
            inverse_number += '1'
        else:
            inverse_number += '0'

    negative_number = bin(int(inverse_number, 2) + 1)[2:].zfill(bit_size)
    print(negative_number)



if __name__ == '__main__':
    Binary_conversions()
