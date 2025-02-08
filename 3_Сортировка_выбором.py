# Сортировка выбором работает путем поиска минимального элемента в неотсортированной части массива
# и его обмена с первым элементом этой части. Затем процесс повторяется для оставшейся части массива.

def selection_sort(arr):                # cоздание функции сортировки выбором
   for i in range(len(arr)):            # Проходим по всему списку
       min_index = i                    # Предполагаем, что первый элемент в неотсортированной части - это минимальный
       for j in range(i+1, len(arr)):   # Ищем минимальный элемент в оставшейся части списка
           if arr[j] < arr[min_index]:  # Если он меньше минимального
               min_index = j            # Запоминаем его индекс
       arr[i], arr[min_index] = arr[min_index], arr[i] # Меняем местами найденный минимальный элемент с первым элементом в неотсортированной части

# Пример использования
numbers = [64, 25, 12, 22, -11]          # создаем массив
selection_sort(numbers)                 # вызываем функцию сортировки выбором
print(numbers)
