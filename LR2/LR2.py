import array
import os


def cls():
    os.system("cls")


def PrintRelations(m, n):
    print("R1:")
    for line in m:
        print(*line)

    print("R2:")
    for line in n:
        print(*line)


def Reflectivity(m):
    flag = True
    for i in range(len(m)):
        if m[i][i] != 1:
            flag = False
    return flag


def AntiReflectivity(m):
    flag = True
    for i in range(len(m)):
        if m[i][i] != 0:
            flag = False
    return flag


def Symmetry(m):
    flag = True
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                if m[i][j] != m[j][i]:
                    flag = False
    return flag


def AntiSymmetry(m):
    n = len(m)
    nm = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nm[i][j] = m[i][j] * m[j][i]

    flag = True
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                if nm[i][j] != 0:
                    flag = False
    return flag


def Transitivity(m):
    length = len(m)
    tr = [[0 for i in range(0, length)] for j in range(0, length)]
    flag = True

    for i in range(len(m)):
        for j in range(len(m)):
            for k in range(len(m)):
                tr[i][j] = (tr[i][j] | (m[i][k] & m[k][j]))

    print("Транзитивная матрица tr:")
    for line in tr:
        print(*line)

    if (m != tr):
        flag = False
    return flag


def Composition(m, n):
    length = len(m)
    comp = [[0 for i in range(0, length)] for j in range(0, length)]

    for i in range(len(m)):
        for j in range(len(m)):
            for k in range(len(m)):
                comp[i][j] = comp[i][j] + m[i][k] * n[k][j]
            if comp[i][j] != 0:
                comp[i][j] = 1

    print("Composition R1 and R2:")
    for line in comp:
        print(*line)


def ReflictiveClosure(m):
    print("Рефлексивные замыкания, которые есть:")
    print([(i, i) for i in range(len(m)) if m[i][i] == 1])
    print("Рефлексивные замыкания, которых нет:")
    print([(i, i) for i in range(len(m)) if m[i][i] == 0])


def TransitiveClosure_1(m):
    length = len(m)
    tr_1 = [[0 for i in range(0, length)] for j in range(0, length)]

    for i in range(len(m)):
        for j in range(len(m)):
            for k in range(len(m)):
                tr_1[i][j] = (tr_1[i][j] | (m[i][k] & m[k][j]))

    print("Матрица tr_1:")
    for line in tr_1:
        print(*line)

    tr_2 = [[0 for i in range(0, length)] for j in range(0, length)]

    for i in range(len(m)):
        for j in range(len(m)):
            tr_2[i][j] = m[i][j] | tr_1[i][j]

    print("Матрица tr_2:")
    for line in tr_2:
        print(*line)

    tr = [[0 for i in range(0, length)] for j in range(0, length)]

    for i in range(len(m)):
        for j in range(len(m)):
            for k in range(len(m)):
                tr[i][j] = (tr[i][j] | (tr_2[i][k] & tr_2[k][j]))

    print("Матрица tr:")
    for line in tr:
        print(*line)


def TransitiveClosure_2(m):
    def sum_string(m, a, b):
        n = len(m)
        for i in range(n):
            m[a][i] |= m[b][i]
        return m

    length = len(m)
    tr = [[0 for i in range(0, length)] for j in range(0, length)]

    pre_arr = None
    max_count = 3
    count = 0
    while True:
        for i in range(length):
            for j in range(length):
                if (i != j):
                    m = sum_string(m, i, j)
                    if m == pre_arr:
                        count += 1
                    else:
                        count = 0
                    pre_arr = [a[:] for a in m]
                    if count >= max_count:
                        return m


def first():
    cls()

    global n
    n = int(input('Введите мощность множества (1 <= n <= 100): '))

    global R1
    R1 = []
    for i in range(n):
        print('Введите ' + str(i + 1) + '-й элемент 1-го бинарного отношения (R1): ', end='')
        R1.append(list(map(int, input().split())))

    print()
    global R2
    R2 = []
    for i in range(n):
        print('Введите ' + str(i + 1) + '-й элемент 2-го бинарного отношения (R2): ', end='')
        R2.append(list(map(int, input().split())))

    PrintRelations(R1, R2)

    go_back()


def second():
    cls()

    PrintRelations(R1, R2)

    if (Reflectivity(R1)):
        print("(R1) Reflectivity (True) - 1")
    else:
        print("(R1) Ne Reflectivity (False) - 0")

    if (Reflectivity(R2)):
        print("(R2) Reflectivity (True) - 1")
    else:
        print("(R2) Ne Reflectivity (False) - 0")

    go_back()


def third():
    cls()

    PrintRelations(R1, R2)

    if (AntiReflectivity(R1)):
        print("(R1) AntiReflectivity (True) - 1")
    else:
        print("(R1) Ne antiReflectivity (False) - 0")

    if (AntiReflectivity(R2)):
        print("(R2) antiReflectivity (True) - 1")
    else:
        print("(R2) Ne antiReflectivity (False) - 0")

    go_back()


def fourth():
    cls()

    PrintRelations(R1, R2)

    if (Symmetry(R1)):
        print("(R1) Simmetry (True) - 1")
    else:
        print("(R1) Ne simmetry (False) - 0")

    if (Symmetry(R2)):
        print("(R2) Simmetry (True) - 1")
    else:
        print("(R2) Ne simmetry (False) - 0")

    go_back()


def fifth():
    cls()

    PrintRelations(R1, R2)

    if (AntiSymmetry(R1)):
        print("(R1) AntiSimmetry (True) - 1")
    else:
        print("(R1) Ne antiSimmetry (False) - 0")

    if (AntiSymmetry(R2)):
        print("(R2) AntiSimmetry (True) - 1")
    else:
        print("(R2) Ne antiSimmetry (False) - 0")

    go_back()


def sixth():
    cls()

    PrintRelations(R1, R2)

    if (Transitivity(R1)):
        print("(R1) Transitivity (True) - 1")
    else:
        print("(R1) Ne transitivity (False) - 0")

    if (Transitivity(R2)):
        print("(R2) Transitivity (True) - 1")
    else:
        print("(R2) Ne transitivity (False) - 0")

    go_back()


def seventh():
    cls()

    PrintRelations(R1, R2)

    Composition(R1, R2)

    go_back()


def eighth():
    cls()

    PrintRelations(R1, R2)

    print("Бинарное отношение R1:")
    ReflictiveClosure(R1)
    print("Бинарное отношение R2:")
    ReflictiveClosure(R2)

    go_back()


def ninth():
    cls()

    PrintRelations(R1, R2)

    print("Транзитивное замыкание для R1 (Методом уножения и сложения матриц):")
    TransitiveClosure_1(R1)
    print("Транзитивное замыкание для R2 (Методом умножения и сложения матриц):")
    TransitiveClosure_1(R2)

    go_back()


def tenth():
    cls()

    PrintRelations(R1, R2)

    print("Транзитивное замыкание для R1 (Методом Уоршолла):")
    TransitiveClosure_2(R1)
    for line in R1:
        print(*line)
    print("Транзитивное замыкание для R2 (Методом Уоршолла):")
    TransitiveClosure_2(R2)
    for line in R2:
        print(*line)

    go_back()


def menu():
    print('Выберите пункт меню')
    print(
        '1. Создать бинарные отношения\n' + '2. Проверка отношений на рефлексивность\n' + '3. Проверка отношений на антирефлексивность\n' +
        '4. Проверка отношений на симметричность\n' + '5. Проверка отношений на антисимметричность\n' + '6. Проверка отношений на транзитивность\n' +
        '7. Композиция отношений\n' + '8. Рефлексивное замыкание\n' + '9. Транзитивное замыкание (Метод умножения и сложения матриц)\n' +
        '10. Транзитивное замыкание (Метод Уоршолла)\n' + '0. Выход')

    command = int(input('Введите номер пункта: '))
    if command == 1:
        first()
    elif command == 2:
        second()
    elif command == 3:
        third()
    elif command == 4:
        fourth()
    elif command == 5:
        fifth()
    elif command == 6:
        sixth()
    elif command == 7:
        seventh()
    elif command == 8:
        eighth()
    elif command == 9:
        ninth()
    elif command == 10:
        tenth()
    elif command == 0:
        print('Выход из программы!')
        exit(0)
    else:
        print('Неверная команда')


def go_back():
    choise = input('Чтобы вернуться назад нажмите "z"\n')
    if choise == 'z':
        cls()
        menu()
    else:
        print('Неверная команда')
        go_back()


if __name__ == '__main__':
    menu()
