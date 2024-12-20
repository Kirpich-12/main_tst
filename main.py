#Main
#====

#import files 
import Euclid as ec 
import Pascal as pc
import notation as con 

def main():
    usr = input('Если вы хотите выбрать поиск НОД по алгоритму Евклида, то напишите 1 \nЕсли вы хотите вывести треугольник Паскаля с n рядов, то напишите 2 \nЕсли хотите перевести с 10 в лругую сиситему любого числа, то напишите 3\n')
    if usr == '1':  # take two numbers and calculate gcd
        inp1 = int(input('Введите первое число: '))
        inp2 = int(input('Введите второе число: '))
        print(f'НОД этих чисел: {ec.gcd(inp1, inp2)}')
    elif usr == '2':#take a amount of row and write it
        inp = int(input("Введите число рядов треугольника Паскаля: "))
        print(f'Треугольник:\n {pc.pascal(inp)}')
    elif usr == '3':#convert num from 10-system to base-system
        num = int(input('Введите десятичное число: '))
        base = int(input('Введите основание системы счисления: '))
        print(f'Число {num} в системе счисления с основанием {base}: {con.notation(num, base)}')
    else:
        print(f'Эй, чурчхела просили же нормальный ввод 1, 2 и 3, а это - {usr} что такое') #output in case of incorrect input




if __name__ == '__main__':
    main()