def sum_digits(user_input):
    nums_list = [int(i) for i in user_input]
    sum_of_nums = sum(nums_list)

    if sum_of_nums > 9:
        return sum_digits(str(sum_of_nums))
    else:
        return sum_of_nums


user_input = input("Enter your birthday in format DDMMYYYY: ")

try:
    print(sum_digits(user_input))
except ValueError:
    print("Please enter a valid date in format DDMMYYYY!")
