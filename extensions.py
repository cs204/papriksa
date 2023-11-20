a = input("File name: ")
b = ".gif"
c = ".jpg"
d = ".jpeg"
e = ".png"
f = ".pdf"
j = ".txt"
g = ".zip"
if b in a:
                print("image/gif")
elif c in a:
                print("image/jpeg")
elif d in a:
                print("image/jpeg")
elif e in a:
                print("image/png")
elif f in a:
                print("application/pdf")
elif j in a:
                print("text/plain")
elif g in a:
                print("application/zip")
else:
                print("application/octet-stream")
