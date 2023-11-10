def int_to_roman(numbers):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    

    res = []
    for num in numbers:
        i = 0
        roman_numeral = ''
        while  num > 0:
            for _ in range(num // val[i]):
                roman_numeral += syms[i]
                num -= val[i]
            i += 1
        res.append(roman_numeral) 
    return res


numbers = [75, 80, 99, 100, 50]
res = int_to_roman(numbers)
print(res)
# n = int(input())
# arr = []
# for i in range(n):
#     num = int(input())
#     roman_numeral = int_to_roman(num)
#     print(roman_numeral)




# # Example usage:
# decimal_number = 100
# roman_numeral = int_to_roman(decimal_number)
# print(f"The Roman numeral representation of {decimal_number} is {roman_numeral}")
