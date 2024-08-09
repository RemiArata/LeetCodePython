def roman_to_int(s: str) -> int:
    num = 0
    possibilities = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    for k, v in possibilities.items():
        num += s.count(k) * v
        s = s.replace(k, "")
    return num

# string = "III"
# print(roman_to_int(string))

# string = "LVIII"
# print(roman_to_int(string))

string = "MCMXCIV"
print(roman_to_int(string))