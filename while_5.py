user_input = int(input("введите число: "))
s=0
while user_input:
    if user_input%10 == 0 and user_input != 0:
        s+=user_input
        user_input = int(input("введите число: "))
    elif user_input == 0:
        break
    else:
        user_input = int(input("введите число: "))
print(f"это 0, сумма чисел заканчивающиеся нулем {s}")