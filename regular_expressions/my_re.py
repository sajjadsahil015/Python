import re

text = "My number is 03239374738"

match = re.search(r'\d+',text)
print(match.group())

text1 = "I have 3 books and 5 pens"

match = re.search(r"\d+",text1)

if match:
    print(f"First number: {match.group()}")
else:
    print("Number not found")