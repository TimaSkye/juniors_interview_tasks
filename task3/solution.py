tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]


def appearance(intervals: dict[str, list[int]]) -> int:
    # Определение интервалов урока
    lesson_start, lesson_end = intervals['lesson']

    # Инициализация переменных для хранения общего времени присутствия
    pupil_total_time = 0
    tutor_total_time = 0

    # Обработка интервалов присутствия ученика
    pupil_intervals = intervals['pupil']
    if len(pupil_intervals) % 2 != 0:
        raise ValueError("Количество интервалов для ученика должно быть четным")
    for i in range(0, len(pupil_intervals), 2):
        pupil_entry, pupil_exit = pupil_intervals[i], pupil_intervals[i + 1]

        # Корректировка интервала, если он выходит за пределы урока
        entry = max(pupil_entry, lesson_start)
        exit = min(pupil_exit, lesson_end)

        # Добавляем корректированный интервал, если он внутри урока
        if entry < exit:
            pupil_total_time += exit - entry

    # Обработка интервалов присутствия учителя
    tutor_intervals = intervals['tutor']
    if len(tutor_intervals) % 2 != 0:
        raise ValueError("Количество интервалов для учителя должно быть четным")
    for i in range(0, len(tutor_intervals), 2):
        tutor_entry, tutor_exit = tutor_intervals[i], tutor_intervals[i + 1]

        # Корректировка интервала, если он выходит за пределы урока
        entry = max(tutor_entry, lesson_start)
        exit = min(tutor_exit, lesson_end)

        # Добавляем корректированный интервал, если он внутри урока
        if entry < exit:
            tutor_total_time += exit - entry

    # Возвращаем общее время присутствия ученика и учителя
    return pupil_total_time + tutor_total_time


if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'