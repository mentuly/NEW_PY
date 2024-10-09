def user_temperature(temperature: float) -> str: # тут я використав temperature - це параметр з вигаданою назвою я просто її назвав температурою і до цього temperature я передав властивість float тобто щоб числа могли бути дробовими як: 1.2, 3.5 
    if temperature <= 0: # якщо більше дорівнює нулю то "A cold, isn't it?"
        return "A cold, isn't it?"
    elif 0 < temperature < 10: # якщо температура більше 0 і в одночас менше 10 то вивести "Cool."
        return "Cool."
    elif 58 < temperature: # якщо температура більше 58 це на 0.2 гардуса більше максимально зафіксованої температури то виведе "This is unreal"
        return "This is unreal"
    else: # до усіх інших випадків буде виводити "Nice weather we're having."
        return "Nice weather we're having."