import numpy as np


def make_set(a):
    print([[(i + 1, j + 1) for j in range(len(a[i])) if a[i][j]] for i in range(len(a))])


def print_matrix(a):
    for elems in a:
        print(*elems)


def get_ones(a):
    print_matrix([[1 if a[i][j] else 0 for j in range(len(a[i]))] for i in range(len(a))])


def get_matrix():
    n, m = input('Введите размерность матрицы: ').split()
    n, m = int(n),  int(m)
    print('Введите значения элементов матрицы построчно: ')
    matrix = [list(map(int, input().split())) for _ in range(n)]
    return matrix


def is_idempotent(st, a):
    for i in range(len(st)):
        if a[i][i] != st[i]:
            print('Операция не является идемпотентной.')
            return
    print('Операция является идемпонентной.')
    return


def is_commutative(st, a):
    for i in range(len(st)):
        for j in range(len(st)):
            if a[i][j] != a[j][i]:
                print('Операция не является коммутативной.')
                return
    print('Операция является коммутативной.')
    return


def is_associative(st, a):
    for i in range(len(st)):
        for j in range(len(st)):
            for k in range(len(st)):
                if a[i][st.index(a[j][k])] != a[st.index(a[i][j])][k]:
                    print('Операция не является ассоциативной.')
                    return
    print('Операция является ассоцитивной.')
    return


def is_invertible(st, a):
    res = []
    for i in range(len(st)):
        flag = True
        for j in range(len(st)):
            if not(a[i][j] == a[j][i] == 1):
                flag = False
                break
        if flag:
            res.append(st[i])
    if res:
        print(f'Обратимость операции выполняется. Список обратных элементов {res}')
        return
    else:
        print('Обратимость операции не выполняется.')
        return


def is_distributive(st, a):
    print('Для проверки дистрибутивности введите значения второй таблицы Кэли операции. ')
    # b = [[int(val) for val in input().split()] for _ in range(len(st))]
    print('  ', *st)
    b = [input(f'{st[i]}  ').split() for i in range(len(st))]
    for i in range(len(st)):
        for j in range(len(st)):
            for k in range(len(st)):
                if (a[i][st.index(b[j][k])] != b[st.index(a[i][j])][st.index(a[i][k])]) \
                        or (a[st.index(b[j][k])][i] != b[st.index(a[j][i])][st.index(a[k][i])]):
                    print('Операция * не является дистрибутивной относительно операции +')
                    return
    print('Операция * на матрице a является дистрибутивной относительно операции + на матрице b')
    return


def relation_properties():
    n = int(input('Введите размер множества элементов: '))
    # st = list(map(int, input().split()))
    st = input(f'Введите множество длины {n}: ').split()
    print("Введите значения таблицы Кэли некоторой операции: ")
    # a = [list(map(int, input().split())) for i in range(n)]
    print('  ', *st)
    a = [input(f'{st[i]}  ').split() for i in range(len(st))]
    print("Введите 1, чтобы проверить идемпотентность.\nВведите 2, чтобы проверить коммутативность.\n",
          "Введите 3, чтобы проверить ассоциативность.\nВведите 4, чтобы проверить обратимость.\n",
          "Введите 5, чтобы проверить дистрибутивность.")
    yes_or_no = 1
    while yes_or_no:
        bl = int(input('Введите число: '))
        if bl == 1:
            is_idempotent(st, a)
        elif bl == 2:
            is_commutative(st, a)
        elif bl == 3:
            is_associative(st, a)
        elif bl == 4:
            is_invertible(st, a)
        elif bl == 5:
            is_distributive(st, a)
        yes_or_no = int(input('Вы желаете продолжить? 1 - Да, 0 - Нет.'))


def relation_operation():
    print('Выберете операцию из списка:')
    print("Введите 1, чтобы получить объединение бинарных отношений.\n",
          "Введите 2, получить пересечение бинарных отношений.\n",
          "Введите 3, получить дополнение бинарного отношения.\n",
          "Введите 4, чтобы получить транспонированное бинарное отношение.\n",
          "Введите 5, чтобы получить композицию бинарных отношений.")
    yes_or_no = 1
    while yes_or_no:
        op = int(input('Введите число: '))
        if op == 1:
            a = np.array(get_matrix())
            b = np.array(get_matrix())
            print("Объединение бинарных отношений:")
            c = a + b
            make_set(c)
            get_ones(c)
        elif op == 2:
            a = np.array(get_matrix())
            b = np.array(get_matrix())
            c = a * b
            make_set(c)
            get_ones(c)
        elif op == 3:
            a = get_matrix()
            print("Дополнение бинарного отношения:")
            a_new = np.ones(np.array(a).shape) - a
            make_set(a_new)
            get_ones(a_new)
        elif op == 5:
            a = get_matrix()
            b = get_matrix()
            print("Композиция бинарных отношений:")
            c = np.matmul(np.array(a), np.array(b))
            make_set(c)
            get_ones(c)
        elif op == 4:
            a = get_matrix()
            print("Обращение бинарного отношения:")
            a_t = np.array(a).T
            make_set(a_t)
            print_matrix(a_t)
        yes_or_no = int(input('Вы желаете продолжить? 1 - Да, 0 - Нет. '))


def get_mod(a, lim):
    return [[a[i][j] % lim for j in range(len(a[i]))] for i in range(len(a))]


def matrix_operation():
    print('''Сумма матриц (1),\nРазность матриц (2),\nУмножение матрицы на число (3),\nПроизведение двух матриц (4),
Транспонирование матрицы (5),\nОбращение матрицы (6): ''')
    yes_or_no = 1
    lim = (int(input('Введите характеристику поля: ')))
    while yes_or_no:
        num = int(input('Введите число: '))
        if num == 1:
            a = get_matrix()
            b = get_matrix()
            print("Сумма матриц:")
            c = get_mod(np.array(a) + np.array(b), lim)
            print_matrix(c)
        elif num == 2:
            a = get_matrix()
            b = get_matrix()
            print("Разность матриц:")
            c = get_mod(np.array(a) - np.array(b), lim)
            print_matrix(c)
        elif num == 3:
            a = get_matrix()
            print("Введите число: ")
            alpha = int(input())
            print("Умножение матрицы на число:")
            a_alpha = get_mod((np.array(a) * alpha), lim)
            print_matrix(a_alpha)
        elif num == 4:
            a = get_matrix()
            b = get_matrix()
            print("Произведение матриц:")
            c = get_mod(np.matmul(np.array(a), np.array(b)), lim)
            print_matrix(c)
        elif num == 5:
            a = get_matrix()
            print("Транспонированная матрица:")
            a_t = np.array(a).T
            print_matrix(a_t)
        elif num == 6:
            import inverseMatrix as im
            a = get_matrix()
            print("Обращение матрицы:")
            a_inv = im.main()
        yes_or_no = int(input('Вы желаете продолжить? 1 - Да, 0 - Нет. '))


print('''Выберете действие:\nПроверить свойство алгебраической операции (1)
Выполнить операцию над бинарным отношением\отношениями (2)\nВыполнить операцию над матрицей/матрицами (3)''')
action = int(input())
if action == 1:
    relation_properties()
elif action == 2:
    relation_operation()
elif action == 3:
    matrix_operation()


# Задание 1
st = ['a', 'b', 'c', 'd']

a = [['a', 'a', 'a', 'a'],
     ['a', 'b', 'a', 'b'],
     ['a', 'a', 'c', 'c'],
     ['a', 'b', 'c', 'd']]

is_associative(st, a)

# Задание 2
a = np.array([[1, -2],
              [-3, 5]])

e = np.ones((2, 2))

for elems in np.matmul(a, a) + (10 - 5 / 2) * a + (5 / 2) * e:
    print(*elems)
print()

# Задание 3

a = np.array([[-1, 5, 3],
              [5 / 3, 2, 8 - 5 / 3]])

b = np.array([[-5, 2],
              [1, 10 - 5 / 2],
              [-3, 5]])

for elems in np.matmul(a, b):
    print(*elems)

# a b c d e
# b c d e a
# c d e a b
# d e a b c
# e a b c d
#
#
# a a a a a
# a b c d e
# a c e b d
# a d b e c
# a e d c b

#
# 0 1 1 0 1
# 1 0 0 0 0
# 0 1 0 1 1
# 0 0 1 1 0
# 1 1 0 0 0
# 0 1 0 1 0
#
#
# 1 0 0 1 0
# 0 1 1 1 1
# 1 0 1 0 0
# 1 1 0 0 1
# 0 0 1 1 1
# 1 0 1 0 1