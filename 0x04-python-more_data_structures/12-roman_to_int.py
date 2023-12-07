def roman_to_int(roman_string):
    
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,}    
    result = 0
    
    for i, char in enumerate(roman_string):
       value = roman_numerals[char]
       
       if i + 1 < len(roman_string) and value < roman_numerals[roman_string[i + 1]]:
          result -= value
        else:
           result += value
    return result