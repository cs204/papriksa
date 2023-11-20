c = False
while c != True:
    try:
        c = True
        d = input("Дробь: ")
        e = d.split("/")
        p = (float(e[0])/float(e[1]))*100
        if float(e[0])>float(e[1]) or len(e) > 2:
            raise ValueError
        if float(p) >= 99:
            print("F")
        elif int(p) <= 1:
            print("E")
        else:
            print(f"{int(p)}%")

    except ValueError:
        c = False

    except ZeroDivisionError:
        c = False
