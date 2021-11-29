def generate_check_digit(ISBN_9):

    check_digit = 0
    
    sum = 0
    x = 9
    while x > 0:
        sum += x * (ISBN_9 % 10)
        ISBN_9 //= 10
        x -= 1
    check_digit = sum % 11

    return check_digit


def check_ISBN(ISBN_10):
    ISBN_9 = ISBN_10 // 10
    check_digit = ISBN_10 % 10
    if generate_check_digit(ISBN_9) == check_digit:
        return True
    else:
        return False


if __name__ == "__main__":
    pass
