def esc(code):
    return f'\u001b[{code}m'


# 1
def flag_fr():
    for i in range(9):
        print(BLUE + '  ' * 6 + WHITE + '  ' * 6 + RED + '  ' * 6 + END)
    print(END)


RED = esc(41)
BLUE = esc(44)
WHITE = esc(47)
END = esc(0)
lightBLUE = esc(46)
PURPLE = esc(45)
flag_fr()

# 2
import time
import os


def clear_screen():
    os.system('clear')


def uzor():
    for j in range(3):
        if j % 2 == 0:
            for i in range(3):
                if i % 2 == 0:
                    print(WHITE + ' ' * 3 + BLUE + ' ' * 3 + WHITE + ' ' * 3 + END)
                else:
                    print(BLUE + ' ' * 3 + WHITE + ' ' * 3 + BLUE + ' ' * 3 + END)
        else:
            for i in range(3):
                if i % 2 == 0:
                    print(BLUE + ' ' * 3 + WHITE + ' ' * 3 + BLUE + ' ' * 3 + END)
                else:
                    print(WHITE + ' ' * 3 + BLUE + ' ' * 3 + WHITE + ' ' * 3 + END)
        time.sleep(0.2)
        clear_screen()


uzor()


# 3
def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(plot[i][j])
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '0   1 2 3 4 5 6 7 8 9' + END)


array_plot = [[0 for col in range(10)] for row in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i ** 2
print(result)

step = round(abs((result[9] - result[0])) / 9, 1)

array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)

# 4
import csv

cnt1 = 0  # кол-во книг до 2014 года
cnt2 = 0  # кол-во книг после 2014 года
with open("C:/Users/97411/Downloads/books.csv") as csvfile:
    table = csv.reader(csvfile, delimiter=";")
    cnt = 0
    for row in list(table):

        if (cnt != 0 and int(row[6][6:10]) <= 2014):
            cnt1 += 1
        else:
            cnt2 += 1
        cnt += 1

b_before2014 = round((cnt1 / cnt * 100))
b_after2014 = round((cnt2 / cnt * 100))


def diagr():
    for i in range(1):
        print(PURPLE + ' ' * int(b_before2014) + END + ' ' + str(b_before2014) + '%')
        print(lightBLUE + ' ' * int(b_after2014) + END + ' ' + str(b_after2014) + '%')
        print(' ')
        print(PURPLE + ' ' + END + 'Книги до 2014 года' + ' ' + lightBLUE + ' ' + END + 'Книги после 2014 года')


print('')
diagr()