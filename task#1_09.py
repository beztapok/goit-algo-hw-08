import timeit

# Функція реалізує жадібний алгоритм для знаходження мінімальної кількості монет для заданої суми
def find_coins_greedy(sum, coins):
    coins_count = {}  # Ініціалізація словника для збереження кількості монет кожного номіналу
    for coin in coins:
        count = sum // coin  # Обчислення кількості монет даного номіналу
        if count > 0:
            coins_count[coin] = count  # Збереження кількості монет у словнику
        sum -= coin * count  # Зменшення залишкової суми
    return coins_count  # Повернення результату

# Функція реалізує алгоритм динамічного програмування для знаходження мінімальної кількості монет для заданої суми
def find_min_coins(sum, coins):
    # Ініціалізація масиву для збереження мінімальної кількості монет для кожної суми
    min_coins_required = [float('inf')] * (sum + 1)
    min_coins_required[0] = 0  # Базовий випадок: 0 монет для суми 0

    coin_used = [0] * (sum + 1)  # Ініціалізація масиву для збереження монет, що використовуються

    # Заповнення масиву мінімальної кількості монет для кожної суми
    for i in range(1, sum + 1):
        for coin in coins:
            if i >= coin:
                if min_coins_required[i - coin] + 1 < min_coins_required[i]:
                    min_coins_required[i] = min_coins_required[i - coin] + 1
                    coin_used[i] = coin

    coins_count = {}  # Ініціалізація словника для збереження кількості монет кожного номіналу
    current_sum = sum
    while current_sum > 0:
        coin = coin_used[current_sum]  # Отримання монети, що використовується для поточної суми
        coins_count[coin] = coins_count.get(coin, 0) + 1  # Збільшення кількості монет даного номіналу
        current_sum -= coin  # Зменшення залишкової суми

    return coins_count  # Повернення результату

# Функція для автоматичного створення файлу readme.md з результатами виконання алгоритмів
def generate_readme():
    sum_value = 113
    coins = [50, 25, 10, 5, 2, 1]

    greedy_result = find_coins_greedy(sum_value, coins)
    dp_result = find_min_coins(sum_value, coins)

    with open('readme.md', 'w') as f:
        f.write("# Домашнє завдання: Жадібні алгоритми та динамічне програмування\n\n")
        f.write("## Опис задачі\n")
        f.write("В цьому завданні ми реалізували два алгоритми для видачі решти касовою системою:\n")
        f.write("1. Жадібний алгоритм\n")
        f.write("2. Алгоритм динамічного програмування\n\n")
        
        f.write("## Результати виконання\n")
        f.write(f"### Жадібний алгоритм для суми {sum_value}\n")
        f.write(f"Номінали монет та їх кількість: {greedy_result}\n\n")
        
        f.write(f"### Алгоритм динамічного програмування для суми {sum_value}\n")
        f.write(f"Номінали монет та їх кількість: {dp_result}\n\n")
        
        f.write("## Висновки\n")
        f.write("Жадібний алгоритм працює швидко і підходить для наборів монет, де кожен номінал є кратним попередньому.\n")
        f.write("Алгоритм динамічного програмування гарантує знаходження мінімальної кількості монет для будь-якого набору, але його виконання може бути повільнішим, особливо для великих значень суми.\n")

if __name__ == '__main__':
    # Приклад використання та вимірювання часу виконання функцій
    sum_value = 113
    coins = [50, 25, 10, 5, 2, 1]

    print("Жадібний алгоритм:")
    print(find_coins_greedy(sum_value, coins))

    print("Алгоритм динамічного програмування:")
    print(find_min_coins(sum_value, coins))

    # Генерація файлу readme.md з результатами та висновками
    generate_readme()
