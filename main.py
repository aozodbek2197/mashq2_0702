# 6-mashq
try:
    a = int(input())
    b = int(input())
    print(a / b)

except ZeroDivisionError:
    print("Nolga bo‘lish xato")

except ValueError:
    print("Son kiritilmadi")

# 7-mashq
try:
    x = int(input())
    print(10 / x)
except:
    print("Xato")
finally:
    print("Dastur tugadi")

# 8-mashq
ismlar = ["Ali", "Vali"]

try:
    i = int(input("Index: "))
    print(ismlar[i])
except:
    print("Index xato")

# 9-mashq
try:
    print("Salom" + 5)
except:
    print("Tur mos emas")

# 10-mashq
d = {"a": 1}

try:
    print(d["b"])
except:
    print("Kalit topilmadi")
