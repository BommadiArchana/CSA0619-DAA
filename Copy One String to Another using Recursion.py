def copy_string(s):
    if s == "":
        return ""
    return s[0] + copy_string(s[1:])

text = "Hello"
new_text = copy_string(text)

print("Copied String:", new_text)
