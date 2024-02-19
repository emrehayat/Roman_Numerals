roman_values = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

def valid_roman(rom):
    invalid_patterns = ["IIII", "VV", "XXXX", "LL", "CCCC", "DD", "IIV"]
    for pattern in invalid_patterns:
        if pattern in rom:
            return False
    return True

def roman_to_integer(rom):
    rom = rom.upper()

    if not valid_roman(rom):
        raise ValueError(f"{rom} geçersiz bir Roma rakamidir!")
    
    integer_value = 0
    for i in range(len(rom)):
        if i+1 < len(rom) and roman_values[rom[i]] < roman_values[rom[i+1]]:
            integer_value -= roman_values[rom[i]]
        else:
            integer_value += roman_values[rom[i]]
    return integer_value
    
while True:
    rom = input("Roma rakamlariyla bir sayi giriniz (veya q tuşuna basarak çikiniz): ")
    if rom.lower() == "q":
        break

    try:
        integer_value = roman_to_integer(rom)
        print(f"{rom} Romen rakamlariyla eşittir = {integer_value}")
    except ValueError as e:
        print(e)






