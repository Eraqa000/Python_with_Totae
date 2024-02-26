def arithmetic(a, b, c):
    if c=="+":
        return (a+b)
    elif c=="-":
        return (a-b)
    elif c=="*":
        return (a*b)
    elif c=="/":
        return a/b
    else:
        return "Неизвестная операция"

a,b = map(int, input("2 san engiz: "). split())
operation = input("операция: ")
b=arithmetic(a, b, operation)
print(b)
