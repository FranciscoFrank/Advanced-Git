"""
    Testing Git Hooks 
"""
def find_common_elements(seq1, seq2):
    """
        Check if there are identical elements in two given sequences
    """
    common_elements = set(seq1).intersection(seq2)
    if common_elements:
        print(" ".join(map(str, common_elements)))
    else:
        print("Спільні елементи не знайдено")
seq1 = [1, 2, 3, 4]
seq2 = [3, 4 5, 6]
find_common_elements(seq1, seq2)

def classify_triangle(a, b, c):
    # Перевіряємо, чи трикутник може існувати
    if a + b <= c or a + c <= b or b + c <= a:
        return "Трикутник не може існувати"

    # Визначаємо тип трикутника за сторонами
    if a == b == c:
        triangle_type = "рівносторонній"
    elif a == b or b == c or a == c:
        triangle_type = "рівнобедрений"
    else:
        triangle_type = "різносторонній"

    # Визначаємо тип трикутника за кутами
    sides_squared = sorted([a**2, b**2, c**2])
    if sides_squared[0] + sides_squared[1] > sides_squared[2]:
        angle_type = "гострокутний"
    elif sides_squared[0] + sides_squared[1] == sides_squared[2]:
        angle_type = "прямокутний"
    else:
        angle_type = "тупокутний"

    return f"Трикутник має сторони: {a}, {b}, {c}\nТрикутник є {triangle_type} і {angle_type}"

# Приклад використання
a = float(input("Введіть сторону a: "))
b = float(input("Введіть сторону b: "))
c = float(input("Введіть сторону c: "))

result = classify_triangle(a, b, c)
print(result)

from geopy.geocoders import Nominatim

def get_location_info(latitude, longitude):
    # Створення об'єкта геокодера
    geolocator = Nominatim(user_agent="geoapiExercises")
    
    # Отримання адреси за координатами
    location = geolocator.reverse((latitude, longitude), language='uk')
    
    if location:
        return f"Місце: {location.address}"
    else:
        return "Не вдалося знайти місце за заданими координатами."

# Приклад використання
latitude = float(input("Введіть широту: "))
longitude = float(input("Введіть довготу: "))

result = get_location_info(latitude, longitude)
print(result)
