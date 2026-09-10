preise = [5, 8, 12, 4, 3, 15, 7]

preise2 = preise.copy()

for p in preise2:
    if p < 10:
        preise.remove(p)

print(f"Gefilterte Preise: {preise}")