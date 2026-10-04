WATER_PER_KG = 30
ML_IN_LITER = 1000
SEPARATOR_LENGTH = 80


def calculate_fitness_metrics(user_weight, user_height):
    # расчёт индекса массы тела
    bmi = round(user_weight / (user_height ** 2), 1)
    # расчёт нормы воды
    water_ml = user_weight * WATER_PER_KG
    water_l = round(water_ml / ML_IN_LITER, 1)
    return bmi, water_l


def main():
    print('=' * SEPARATOR_LENGTH)
    user_name = input('Подскажите, пожалуйста, как вас зовут?: ')
    
    while True:
        try:
            user_age = int(input('Подскажите, пожалуйста, сколько вам лет?: '))
            break
        except ValueError:
            print('Введите значение возраста числом, например: 20')


    while True:
        try:
            user_weight = input(
                    'Подскажите, пожалуйста, ваш вес в килограммах. '
                    'Например: 74 или 74.5: '
                    ).replace(',', '.')
            user_weight = float(user_weight)
            break
        except ValueError:
            print('Введите значение веса числом как в примере')


    while True:        
        try:
            user_height = input('Подскажите, пожалуйста, ваш рост в метрах. Например: 1.84: ').replace(',', '.')
            user_height = float(user_height)
            break
        except ValueError:
            print('Введите значение роста числом как в примере')


    bmi, water_l = calculate_fitness_metrics(user_weight, user_height)

    return user_name, user_age, user_height, user_weight, bmi, water_l

if __name__ == '__main__':
    user_name, user_age, user_height, user_weight, bmi, water_l = main()
    print(
        f'{"=" * SEPARATOR_LENGTH}\n'
        f'Отчет для пользователя: {user_name} ({user_age} г.)\n'
        f'Твой Индекс Массы Тела: {bmi}\n'
        f'Рекомендуемая норма воды: {water_l} л. в день\n'
        f'Расчет окончен. Будьте здоровы!'
        )
