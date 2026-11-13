def f(text):
    if text == "":
        return ""
    if text[0].lower() in "aeiou":
        return f(text[1:]) + text[0].upper()
    return f(text[1:]) + text[0]

print(f("Halo"))







