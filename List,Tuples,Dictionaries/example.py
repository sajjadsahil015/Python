sentence = "apple banana apple mango banana apple"
words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word] = 1
print(word_count)

sent: str = "Hello World"
ch_count = {}
for i in sent:
    if i == " ":
        continue
    if i in ch_count:
        ch_count[i] += 1 
    else:
        ch_count[i] = 1
print(ch_count)


vowels = 0
consonants = 0

vowel = "aeiou"
for i in sentence.lower():
    if i == " ":
        continue
    if i.isalpha():
        if i in vowel:
            vowels += 1
        else:
            consonants +=1
print(vowels)
print(consonants)