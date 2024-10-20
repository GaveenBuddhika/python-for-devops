arn = "arn:aws:iam::12222222222:user/gaveen"

print(arn.split("/") [1])


name = "gaveen"

print(name.upper())

## find length
text = "Python is awesome"
length = len(text)
print("Length of the string:", length)


##replace
text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)

##cut words
text = "Python is awesome"
words = text.split()
print("Words:", words)


text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)


##find strings
text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")



import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
