def print_string_pairs(number):
    digits_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    if len(number) < 2:
        print("Number should have at least two digits.")
        return

    for char1 in digits_to_letters.get(number[0], ''):
        for char2 in digits_to_letters.get(number[1], ''):
            print(char1 + char2)


# Example usage
user_input = input("Enter a number: ")
print_string_pairs(user_input)
