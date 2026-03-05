def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]

text = "Python"
print("Reversed String:", reverse_string(text))
