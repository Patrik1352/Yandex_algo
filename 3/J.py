def simulate_update_process(n, k):
    # Инициализация информации об устройствах: какие части они имеют
    devices = [{i for i in range(k)} if device == 0 else set() for device in range(n)]

    # Инициализация матрицы "ценности" устройств
    value_matrix = [[0 for _ in range(n)] for __ in range(n)]

    # Счетчик таймслотов для каждого устройства
    time_slots = [0] * n

    while any(len(device) < k for device in devices):
        # Определение, на скольких устройствах есть каждая часть обновления
        part_presence = [{device for device, parts in enumerate(devices) if part in parts} for part in range(k)]

        # Определение, какую часть запросить каждым устройством
        requests = [None] * n
        for device in range(n):
            missing_parts = [part for part in range(k) if part not in devices[device]]
            if missing_parts:
                # Выбор части, присутствующей на наименьшем количестве устройств, с наименьшим номером
                requests[device] = min(missing_parts, key=lambda x: (len(part_presence[x]), x))

        # Формирование запросов к устройствам
        for device, part in enumerate(requests):
            if part is not None:
                possible_sources = sorted(part_presence[part], key=lambda x: (len(devices[x]), x))
                if possible_sources:
                    # Выбор устройства для запроса
                    chosen_source = possible_sources[0]
                    value_matrix[device][chosen_source] += 1
                    requests[device] = (part, chosen_source)

        # Обработка запросов
        for device in range(n):
            if requests[device] and requests[device][1] == device:
                part, _ = requests[device]
                # Проверка всех запросов к этому устройству
                candidates = [i for i, req in enumerate(requests) if req and req[0] == part and req[1] == device]
                # Выбор кандидата на основе "ценности", количества частей и номера устройства
                if candidates:
                    best_candidate = max(candidates, key=lambda x: (value_matrix[device][x], -len(devices[x]), x))
                    devices[best_candidate].add(part)
                    time_slots[best_candidate] += 1

        # Увеличение счетчика таймслотов для всех устройств, которые еще не получили все части
        for device in range(n):
            if len(devices[device]) < k:
                time_slots[device] += 1

    return time_slots[1:]

# Тестируем исправленную функцию с данными из примера задачи
print(simulate_update_process(3, 2))
