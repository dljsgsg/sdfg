#1
shopping_list = []

# Функция для вывода списка покупок
def display_shopping_list():
    sorted_list = sorted(shopping_list, key=lambda x: x['куплено'])
    for item in sorted_list:
        print(f"{item['название']} - {item['количество']} {'(куплено)' if item['куплено'] else '(не куплено)'}")

# Функция для добавления покупки в список
def add_to_shopping_list(product, quantity):
    for item in shopping_list:
        if item['название'] == product:
            item['количество'] += quantity
            return
    shopping_list.append({'название': product, 'количество': quantity, 'куплено': False})

# Функция для отметки продукта как купленного
def buy_product(product):
    for item in shopping_list:
        if item['название'] == product:
            item['куплено'] = True

# Пример использования функций
add_to_shopping_list("Яблоки", 3)
add_to_shopping_list("Молоко", 1)
add_to_shopping_list("Хлеб", 2)
add_to_shopping_list("Яблоки", 2)  # Увеличиваем количество яблок

display_shopping_list()

buy_product("Молоко")
print("После покупки молока:")
display_shopping_list()
#2
shopping_receipt = [
    {"название": "Яблоки", "количество": 3, "цена": 10},
    {"название": "Молоко", "количество": 1, "цена": 20},
    {"название": "Хлеб", "количество": 2, "цена": 15}
]

# Функция для распечатки чека на экран
def print_shopping_receipt():
    for item in shopping_receipt:
        print(f"{item['название']} - {item['количество']} шт. по {item['цена']} грн")

# Функция для подсчета общей суммы покупки
def calculate_total():
    total = sum(item['количество'] * item['цена'] for item in shopping_receipt)
    return total

# Функция для получения самой дорогой покупки в чеке
def get_most_expensive_purchase():
    max_purchase = max(shopping_receipt, key=lambda x: x['цена'])
    return max_purchase

# Функция для подсчета средней стоимости одного товара в чеке
def calculate_average_price():
    total_items = sum(item['количество'] for item in shopping_receipt)
    total_cost = sum(item['количество'] * item['цена'] for item in shopping_receipt)
    average_price = total_cost / total_items
    return average_price

# Пример использования функций
print("Чек в магазине:")
print_shopping_receipt()

total_cost = calculate_total()
print(f"Общая сумма покупки: {total_cost} грн")

most_expensive = get_most_expensive_purchase()
print(f"Самая дорогая покупка: {most_expensive['название']} ({most_expensive['цена']} грн)")

average_price = calculate_average_price()
print(f"Средняя стоимость одного товара в чеке: {average_price} грн")
#3
# Массив CSS-стилей
styles = [
    {"название": "color", "значение": "red"},
    {"название": "font-size", "значение": "16px"},
    {"название": "text-align", "значение": "center"},
    {"название": "text-decoration", "значение": "underline"}
]

# Функция для вывода текста с применением стилей
def display_text_with_styles(styles, text):
    style_string = "; ".join([f"{style['название']}: {style['значение']}" for style in styles])
    print(f'<p style="{style_string}">{text}</p>')

# Пример использования функции
text = "Пример текста с примененными стилями"
display_text_with_styles(styles, text)
                         #4
auditoriums = [
    {"название": "101", "места": 15, "факультет": "Инженерный"},
    {"название": "102", "места": 20, "факультет": "Инженерный"},
    {"название": "201", "места": 12, "факультет": "Гуманитарный"},
    {"название": "202", "места": 18, "факультет": "Гуманитарный"},
    {"название": "301", "места": 10, "факультет": "Медицинский"}
]

# Функция для вывода всех аудиторий
def print_all_auditoriums(auditoriums):
    for auditorium in auditoriums:
        print(auditorium)

# Функция для вывода аудиторий для указанного факультета
def print_auditoriums_for_faculty(auditoriums, faculty):
    for auditorium in auditoriums:
        if auditorium["факультет"] == faculty:
            print(auditorium)

# Функция для вывода аудиторий, подходящих для переданной группы
def print_auditoriums_for_group(auditoriums, group):
    for auditorium in auditoriums:
        if auditorium["места"] >= group["количество студентов"] and auditorium["факультет"] == group["факультет"]:
            print(auditorium)

# Функция для сортировки аудиторий по количеству мест
def sort_auditoriums_by_seats(auditoriums):
    return sorted(auditoriums, key=lambda x: x["места"])

# Функция для сортировки аудиторий по названию
def sort_auditoriums_by_name(auditoriums):
    return sorted(auditoriums, key=lambda x: x["название"])

# Пример использования функций
print("Все аудитории:")
print_all_auditoriums(auditoriums)

print("\nАудитории для факультета 'Инженерный':")
print_auditoriums_for_faculty(auditoriums, "Инженерный")

group = {"название": "Группа 1", "количество студентов": 15, "факультет": "Инженерный"}
print("\nАудитории для группы:")
print_auditoriums_for_group(auditoriums, group)

print("\nАудитории отсортированные по количеству мест:")
sorted_by_seats = sort_auditoriums_by_seats(auditoriums)
print(sorted_by_seats)

print("\nАудитории отсортированные по названию:")
sorted_by_name = sort_auditoriums_by_name(auditoriums)
print(sorted_by_name)
