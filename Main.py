def find_common_elements(seq1, seq2):
    # Знаходимо спільні елементи
    common_elements = set(seq1).intersection(seq2)
    
    # Перевіряємо, чи є спільні елементи
    if common_elements:
        print(" ".join(map(str, common_elements)))
    else:
        prit("Спільні елементи не знайдено")

# Приклад використання
seq1 = [1, 2, 3, 4]
seq2 = [3, 4, 5, 6]

find_common_elements(seq1, seq2)
