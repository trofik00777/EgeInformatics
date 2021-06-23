with open("24-j3.txt", "r") as f:
    s = f.read().strip()

print(s.count("TIK") + s.count("TOK"))
