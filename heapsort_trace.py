def swap(arr, i, j):
    """Міняє місцями два елементи масиву."""
    arr[i], arr[j] = arr[j], arr[i]
    return 3

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

    print(f"Починаємо 'занурювати' елемент: {arr[k]} "
          f"з індексу {k}")

    while True:
        j = 2 * k + 1  # Індекс лівого дочірнього елемента

        if j >= n:
            print(f"Елемент {arr[k]} на індексі {k} "
                  f"досяг кінця купи. Завершуємо.")
            break

        # Знаходимо найбільший дочірній елемент
        if j + 1 < n:
            comparisons += 1
            if arr[j + 1] > arr[j]:
                print(f"  Порівнюємо {arr[j]} (лівий) та "
                      f"{arr[j + 1]} (правий). "
                      f"Обираємо {arr[j + 1]}")
                j += 1
            else:
                print(f"  Порівнюємо {arr[j]} (лівий) та "
                      f"{arr[j + 1]} (правий). "
                      f"Обираємо {arr[j]}")
        else:
            print(f"  Обираємо лівий дочірній елемент: "
                  f"{arr[j]} на індексі {j}")

        # Порівнюємо батьківський та дочірній елементи
        comparisons += 1
        if arr[k] >= arr[j]:
            print(f"  {arr[k]} (батько) >= {arr[j]} "
                  f"(найбільший дочірній). "
                  f"Елемент на своєму місці.")
            break

        # Обмінюємо елементи
        print(f"  Міняємо місцями {arr[k]} (батько) "
              f"та {arr[j]} (дочірній)")

        assignments += swap(arr, k, j)
        print(f"  Масив після обміну: {arr}")

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
        c, a = sink(arr, i, n)
        comparisons += c
        assignments += a
        print("---------------------------------")

    print("\n Масив після побудови купи:", arr)

    # Фаза 2: Сортування
    print("\n--- Фаза 2: Сортування ---")

    for i in range(n - 1, 0, -1):
        print(f"\nМіняємо місцями корінь ({arr[0]}) "
              f"та останній елемент ({arr[i]})")

        assignments += swap(arr, 0, i)

        print(f"Розмір купи зменшився до {i}. "
              f"Відновлюємо властивості купи.")

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
