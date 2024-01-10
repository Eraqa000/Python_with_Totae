user_input = int(input("введите число: "))
s=0
while user_input:
    s+=1
    if user_input == 0:

        break
    else:
        user_input = int(input("введите число: "))
print(f"это 0 kalichestvo chisel {s}")


