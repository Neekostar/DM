import os


def reflexivity(binary_relation):
    for x in range(len(binary_relation)):
        if not binary_relation[x][x]:
            return False
    return True


def irreflexivity(binary_relation):
    for x in range(len(binary_relation)):
        if binary_relation[x][x]:
            return False
    return True


def symmetry(binary_relation):
    for x in range(len(binary_relation)):
        for y in range(len(binary_relation)):
            if binary_relation[x][y] != binary_relation[y][x]:
                return False
    return True


def antisymmetry(binary_relation):
    for x in range(len(binary_relation)):
        for y in range(len(binary_relation)):
            if binary_relation[x][y] and binary_relation[y][x] and x != y:
                return False
    return True


def transitivity(binary_relation):
    for x in range(len(binary_relation)):
        for y in range(len(binary_relation)):
            for z in range(len(binary_relation)):
                if binary_relation[x][y] and binary_relation[y][z] and not binary_relation[x][z]:
                    return False
    return True


def binary_relation_properties(binary_relation):
    print(f'Рефлексивность: {int(reflexivity(binary_relation))}')
    print(f'Антирефлексивность: {int(irreflexivity(binary_relation))}')
    print(f'Симметричность: {int(symmetry(binary_relation))}')
    print(f'Антисимметричность: {int(antisymmetry(binary_relation))}')
    print(f'Транзитивность: {int(transitivity(binary_relation))}')


def composition(binary_relation1, binary_relation2):
    result = [[0 for i in range(len(binary_relation1))] for j in range(len(binary_relation1))]
    for x in range(len(binary_relation1)):
        for y in range(len(binary_relation1)):
            for z in range(len(binary_relation1)):
                if binary_relation1[x][z] and binary_relation2[z][y]:
                    result[x][y] = 1
    return result


def binary_relations_mul(binary_relation1, binary_relation2):
    result = [[0 for i in range(len(binary_relation1))] for j in range(len(binary_relation1))]
    for i in range(len(binary_relation1)):
        for j in range(len(binary_relation1)):
            for k in range(len(binary_relation1)):
                result[i][j] += binary_relation1[i][k] * binary_relation2[k][j]
        result[i][j] = (result[i][j] > 0)
    return result


def binary_relations_sum(binary_relation1, binary_relation2):
    result = [[0 for i in range(len(binary_relation1))] for j in range(len(binary_relation1))]
    for i in range(len(binary_relation1)):
        for j in range(len(binary_relation1)):
            result[i][j] = int(binary_relation1[i][j] + binary_relation2[i][j] >= 1)
    return result


def get_symmetry_closure(Q):
    for i in range(len(Q)):
        for j in range(len(Q)):
            Q[i][j] = max(Q[i][j], Q[j][i])
    return Q


def get_reflexivity_closure(Q):
    for i in range(len(Q)):
        Q[i][i] = 1
    return Q


def get_transitivity_closure(Q):
    Q1 = binary_relations_mul(Q, Q)
    Q2 = binary_relations_sum(Q, Q1)
    if Q2 == Q:
        return Q2
    return get_transitivity_closure(Q2)


def alg_warshall(Q):
    while not transitivity(Q):
        for i in range(len(Q)):
            for j in range(len(Q)):
                if i != j and Q[i][j]:
                    for k in range(len(Q)):
                        Q[i][k] = int(Q[i][k] + Q[j][k] >= 1)
    return Q


def input_binary_relation(n):
    binary_relation = []
    for i in range(n):
        string = list(map(int, input().split()))
        binary_relation.append(string)
    return binary_relation


def print_binary_relation(binary_relation):
    for i in range(len(binary_relation)):
        print(*binary_relation[i])


n = int(input('Введите мощность множества: '))

print('Опишите первое бинарное отношение:')
binary_relation1 = input_binary_relation(n)

print('Опишите второе бинарное отношение:')
binary_relation2 = input_binary_relation(n)

print('Свойства первого бинарного отношения:')
binary_relation_properties(binary_relation1)
print()

print('Свойства второго бинарного отношения:')
binary_relation_properties(binary_relation2)
print()

print('Композиция двух бинарных отношений:')
compos = composition(binary_relation1, binary_relation2)
print_binary_relation(compos)
print()

exit = False
while not exit:
    print('1. Выбрать первое бинарное отношение.')
    print('2. Выбрать второе бинарное отношение.')
    print('3. Выбрать композицию первого и второго бинарных отношений.')
    print('0. Выход.')
    br = []
    choice = int(input('Выберите бинарное отношение: '))
    match choice:
        case 0:
            exit = True
        case 1:
            br = binary_relation1
        case 2:
            br = binary_relation2
        case 3:
            br = compos
        case other:
            print('Неверная команда!')
    print('1. Выбрать рефлексивное замыкание.')
    print('2. Выбрать симметричное замыкание.')
    print('3. Выбрать транзитивное замыкание.')
    choice = int(input('Выберите тип замыкания: '))
    print('Бинарное отношение:')
    print_binary_relation(br)
    match choice:
        case 1:
            print('Рефлексивное замыкание:')
            print_binary_relation(get_reflexivity_closure(br))
        case 2:
            print('Симметричное замыкание:')
            print_binary_relation(get_symmetry_closure(br))
        case 3:
            print('Транзитивное замыкание с помощью умножения и сложения матриц:')
            print_binary_relation(get_transitivity_closure(br))
            print('Транзитивное замыкание с помощью алгоритма Уоршалла:')
            print_binary_relation(alg_warshall(br))
        case other:
            print('Неверная команда!')
    os.system('pause')
    os.system('clear')
