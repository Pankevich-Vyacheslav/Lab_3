def swap(arr, i, j):
    """Міняє місцями два елементи масиву."""
    arr[i], arr[j] = arr[j], arr[i]
    return 3  # Кількість присвоювань при обміні


def sink(arr, i, n):
    """
    Процедура занурення елемента вниз по купі.
    arr: масив
    i: індекс поточного елемента
    n: розмір купи
    """
    comparisons = 0
    assignments = 0
    k = i

    while True:
        j = 2 * k + 1  # Індекс лівого дочірнього елемента

        if j >= n:
            break

        # Знаходимо найбільший дочірній елемент
        if j + 1 < n:
            comparisons += 1
            if arr[j + 1] > arr[j]:
                j += 1

        # Порівнюємо батьківський елемент із дочірнім
        comparisons += 1
        if arr[k] >= arr[j]:
            break

        # Обмінюємо елементи та продовжуємо занурення
        assignments += swap(arr, k, j)
        k = j

    return comparisons, assignments


def heapsort(arr):
    """
    Алгоритм сортування купою (HeapSort).
    """
    n = len(arr)
    comparisons = 0
    assignments = 0

    print("Початковий масив:", arr)

    # Фаза 1: Побудова максимальної купи
    print("\n--- Фаза 1: Побудова максимальної купи ---")

    for i in range(n // 2 - 1, -1, -1):
        print(f"Занурюємо елемент з індексу {i}: {arr[i]}")

        c, a = sink(arr, i, n)
        comparisons += c
        assignments += a

    print("Масив після побудови купи:", arr)

    # Фаза 2: Сортування
    print("\n--- Фаза 2: Сортування ---")

    for i in range(n - 1, 0, -1):
        print(f"\nМіняємо місцями корінь ({arr[0]}) "
              f"та останній елемент ({arr[i]})")

        assignments += swap(arr, 0, i)

        # Відновлюємо властивості зменшеної купи
        print(f"Розмір купи зменшився до {i}.")

        c, a = sink(arr, 0, i)
        comparisons += c
        assignments += a

        print("Масив на поточному кроці:", arr)

    return arr, comparisons, assignments


# Моделювання для варіанта №15
A = [50, 80, 19, 86, 35, 7, 60, 48, 51]

sorted_A, comparisons, assignments = heapsort(A)

print("\n Відсортований масив:", sorted_A)
print("Загальна кількість порівнянь:", comparisons)
print("Загальна кількість присвоювань:", assignments)
