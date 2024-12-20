# take two numbers and calculate gcd
#===================================


def gcd(a:int, b:int) -> int: #calculate gcd
    if a == 0 or b == 0: 
         return max(a, b)
    else:
        if a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)
        

def main(): #main function
    inp = input('Введите два числа через пробел ')
    inp_is = inp.split()
    inp_1 = int(inp_is[0])
    inp_2 = int(inp_is[1])
    print(f'Нод чисел {inp_1} и {inp_2}: {gcd(inp_1, inp_2)}')

        
if __name__ == '__main__':
    main()