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
