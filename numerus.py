def to_arabic_num(roman_num):
    roman_to_arabic_dictionary = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
    return roman_to_arabic_dictionary[roman_num];


def numerus(roman_numeral):
    result = 0;
    prev = 0
    for num in roman_numeral:
        arabic_num = to_arabic_num(num)
        if prev < arabic_num:
            arabic_num = arabic_num - 2 * prev
        result += arabic_num
        prev = arabic_num
    return result


print(numerus('xiv'))  # 14
print(numerus('mmxlix'))  # 2049
print(numerus('mmmmmmmmmmmmmmmmmmmmmmmmmdclxxiv'))  # 25674
