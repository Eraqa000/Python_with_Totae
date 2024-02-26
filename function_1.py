def season(a):
    if a>0 and a<3 or a==12:
        return "zima"
    elif a>2 and a<6:
        return "vesna"
    elif a>5 and a<9:
        return "leto"
    elif a>8 and a<12:
        return "osen"

a = int(input("число месяца: "))
b = season(a)
print(b)