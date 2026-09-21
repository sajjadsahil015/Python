import re

text = "Ali have 4 brothers and 2 sisters@"

match = re.search(r"\d+",text)
# print(match.group())
matches = re.findall(r"\d",text)
# print(matches)
sub_match = re.sub(r"\d+",'***',text)
# print(sub_match)
# print(re.findall(r"\D",text))
# print(re.findall(r"\w",text))
# print(re.findall(r"\W",text))
# print(re.findall(r"\s",text))
# print(re.findall(r"\S",text))
# print(re.findall(r"a.",text))
# print(re.findall(r"^Ali",text))
print(re.findall(r"@$",text))

