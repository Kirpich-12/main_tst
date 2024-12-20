#convert num from 10-system to base-system 
#=========================================


def notation(N: int, T: int) -> str: #converte
    if N == 0:
        return '0'

    number = ''
    while N > 0:
        N, r = divmod(N, T)
        if r > 9:
            r = chr(ord('A') + r - 10)
        number = str(r) + number
    return number


def main(): #main function
    num = int(input('Введите десятичное число: '))
    base = int(input('Введите основание системы счисления: '))
    print(f'Число {num} в системе счисления с основанием {base}: {notation(num, base)}')


if __name__ == '__main__':
   main()