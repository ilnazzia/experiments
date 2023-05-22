def split_list(data, N):
    n = len(data)
    k = n // N  # минимальный размер одной партиции
    m = n % N   # количество партиций, размер которых нужно увеличить на 1
    parts_sizes = [k+1 if i < m else k for i in range(N)]  # список с итоговыми размерами партиций
    parts = []
    # создадим окно и по размерам этого окна будем брать срез списка
    start_i = 0  # начальный индекс окна
    for size in parts_sizes:
        end_i = start_i + size  # конечный индекс окна
        part = data[start_i:end_i]  # берём срез из списка
        parts.append(part)
        start_i = end_i  # начальный индекс следующего окна = конечный индекс предыдущего
    return parts

data = [1, -2, 3, None, 5, {6, 7}, 8, 'a', 10, (11, 12), '13']
N = 5
print(split_list(data, N))