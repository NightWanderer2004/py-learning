# Задача 1: Проверить, является ли строка скобочной последовательностью. Дана строка, содержащая только символы (, ), {, }, [ и ]. Необходимо проверить, является ли данная строка правильной скобочной последовательностью. Правильная скобочная последовательность определяется следующим образом:

# Каждая открывающая скобка должна иметь соответствующую закрывающую скобку того же типа.
# Пары скобок должны быть правильно вложены.
# Например, строка "(){}[]" является правильной скобочной последовательностью, в то время как строка "{[()]}" также является правильной, а строка "{[)]}" является неправильной.

# Напишите функцию is_valid_parentheses(sequence), которая принимает строку sequence и возвращает True, если строка является правильной скобочной последовательностью, и False в противном случае.

sequence_correct = "({[]})"
sequence_incorrect = "({[}])"
sequence_incorrect_2 = "(()[[{{]}})"


def is_valid_parenthese(sequence):
    stack = []
    for i in sequence:
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
        elif i == ")" and stack[-1] == "(":
            stack.pop()
        elif i == "]" and stack[-1] == "[":
            stack.pop()
        elif i == "}" and stack[-1] == "{":
            stack.pop()
        else:
            return False
    return True


print(is_valid_parenthese(sequence_correct))
print(is_valid_parenthese(sequence_incorrect))
print(is_valid_parenthese(sequence_incorrect_2))
