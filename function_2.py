def bank(a,years):

    for i in range(0,years):
        a+=(a*0.1)

    return a

a = int(input("взнос: "))
years = int(input("сколько лет: "))
b=bank(a, years)
print(b)