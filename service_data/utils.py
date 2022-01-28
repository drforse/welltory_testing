
def is_even(number: float | int):
    if isinstance(number, int):
        return number % 2 == 0

    # float numbers are even if the last digit is even,
    # so we are cutting off zeros from end and getting the last digit or the integer number
    weight_str = str(number)
    current_char_number = -1
    check_digit = weight_str[current_char_number]
    while check_digit == "0":
        current_char_number -= 1
        check_digit = weight_str[current_char_number]
        if check_digit == ".":
            check_digit = weight_str[:current_char_number]
            break

    return int(check_digit) % 2 == 0
