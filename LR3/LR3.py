n = int(input("Введите мощность множества:\n"))
list = []


def NextPermutation(list, n):
    i = n - 2
    while (i >= 0):
        if (list[i] < list[i + 1]):
            min_val = list[i + 1]
            min_id = i + 1
            for j in range(i + 2, n):
                if (list[j] > list[i] and list[j] < min_val):
                    min_val = list[j]
                    min_id = j
            list[i], list[min_id] = list[min_id], list[i]
            sorted(list[i + 1:-1])
            return True
        i -= 1
    return False

while NextPermutation(list, n):
    for i in range(0, n):
        print(list[i])