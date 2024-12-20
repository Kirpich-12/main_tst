#take a amount of row and write it
#=================================


def pascal(n, lol=None): #write a Pascal triangle
    if lol is None:
        lol = [[1]]
    if n == 1:
        return lol
    else:
        prev_row = lol[-1]
        new_row = [1] + [sum(i) for i in zip(prev_row, prev_row[1:])] + [1]
        return pascal(n - 1, lol + [new_row])


def main(): #main function
    inp = int(input())
    print(pascal(inp))


if __name__ == '__main__':
    main()