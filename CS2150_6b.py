import re
f = open("input.txt", "r")
s = f.read()

# s = s.replace("<", "/")

# print(s)

# exp = re.compile("\^\(\S*\)")

# exps = exp.findall(s)

# for st in exps:
#     replace_with = list(st)
#     replace_with[1] = "{"
#     replace_with[-1] = "}"
#     replace_with = "".join(replace_with)
#     s = s.replace(st, replace_with)
s = s.replace("θ", "\\theta")
s = s.replace("*", " \\cdot ")
s = s.replace("cos", "\\cos")
print(s)
