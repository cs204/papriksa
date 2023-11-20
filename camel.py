a = input("Верблюжий стиль: ")
b = ""
for c in a:
        if c.istitle():
              c = c.lower()
              c = f"_{c}"
        b = b + c;
print(b)




