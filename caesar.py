ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar(text, k):
    text_verschluesselt = ""
    for zeichen in text.upper():
        if zeichen in ALPHABET:
            x = ord(zeichen) - ord("A")
            y = (x+k) % 26
            text_verschluesselt += chr(y + ord("A"))
        else:
            text_verschluesselt += zeichen

    return text_verschluesselt

print(caesar("universitaet marburg", 8))
print(caesar("CVQDMZAQBIMB UIZJCZO", -8))

def brute_force(geheimtext):
    for k in range(1,26):
        print(f"k = {k}: {caesar(geheimtext, -k)}")


geheimtext = "NSKTWRFYNP RFHMY XUFXX"
brute_force(geheimtext)


        
