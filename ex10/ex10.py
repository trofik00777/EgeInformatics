import sys

text = ""
for i in sys.stdin:
    text += i.lower()
print(text.count("свет"))
