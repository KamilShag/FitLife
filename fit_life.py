print('Привет! Добро пожаловать в фитнес-бота!')
print('=' * 80)
WATER_PER_KG = 30
ML_IN_LITER = 1000


user_name = input('Подскажите, пожалуйста, как вас зовут?: ')


try:
    user_age = int(input('Подскажите, пожалуйста, сколько вам лет?: '))
except ValueError:
    print('Введите значение возраста числом, например: 20')
    user_age = int(input('Подскажите, пожалуйста, сколько вам лет?: '))

try:
    user_weight = float(
        input(
            'Подскажите, пожалуйста, ваш вес в килограммах. '
            'Например: 74 или 74.5: '))
except ValueError:
    print('Введите значение веса числом как в примере')
    user_weight = float(
        input(
            'Подскажите, пожалуйста, ваш вес в килограммах. '
            'Например: 74 или 74.5: '))

try:
    user_height = float(
        input('Подскажите, пожалуйста, ваш рост в метрах. Например: 1.84: '))
except ValueError:
    print('Введите значение роста числом как в примере')
    user_height = float(
        input('Подскажите, пожалуйста, ваш рост в метрах. Например: 1.84: '))

# расчёт индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)
# расчёт нормы воды
water_ml = user_weight * WATER_PER_KG
water_l = round(water_ml / ML_IN_LITER, 1)


print('=' * 80)
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')


print('Расчет окончен. Будьте здоровы!')
