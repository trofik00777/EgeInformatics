import sys

text = ""

for i in sys.stdin:
    text += " " + i.strip().lower()
print(text)
print(text.count("свет"))
