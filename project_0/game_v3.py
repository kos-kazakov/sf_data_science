"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np


def random_predict(number):
    """Рандомно угадываем число

    Args:
        number (int): Загаданное число.

    Returns:
        int: Число попыток
    """
    
    count = 0
    start = 1
    end = 100

    while True:
        count += 1
        predict_number =  (start + end)//2 # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        elif (number > predict_number):
            start = predict_number
        else:
            end = predict_number
    return count


def score_game(random_predict):
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

# RUN
score_game(random_predict)