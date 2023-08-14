# 1) '.' matches any character except a newline
# 2) '^' matches the start of the string
# 3) '$' matches the end of the string or just before the newline at the end of the string
# 4) '*' matches 0 or more (greedy)
# 5) '+' matches 1 or more (greedy)
# 6) '?' matches 0 or 1 (greedy)
# 7) '{n}' matches exactly n times
# 8) '{min, max}' matches between min and max (greedy)
# 9) '\d' matches a digit (0-9)
# 10) '\w' matches a word character (a-z, A-Z, 0-9, _)
# 11) '\s' matches a whitespace character (space, tab, newline, return)
# 12) '\b' matches a word boundary (between \w and \W)


import re

# text = "The price of the item is $20.99. Hurry, sale ends soon!"
# pattern = r'\$\d+\.\d+'
# matches = re.findall(pattern, text)
# print(matches)  # ['$20.99']

# text2 = "John Smith, Alice Johnson, Bob Brown"
# pattern2 = r'(\w+) (\w+)'
# matches2 = re.findall(pattern2, text2)
# for match in matches2:
#     print(match)

# text3 = "Please contact us at contact@example.com or support@company.net for assistance."
# pattern3 = r'\w+@\w+\.\w+'
# matches3 = re.findall(pattern3, text3)
# print(matches3)

# text4 = "Apples are amazing and apricots are also awesome."
# pattern4 = r'\ba\w+'
# matches4 = re.findall(pattern4, text4)
# print(matches4)

# text5 = "The event will take place on 25-12-2023 and 05-06-2023."
# pattern5 = r'\d{2}-\d{2}-\d{4}'
# matches5 = re.findall(pattern5, text5)
# print(matches5)
