user_input = input("Введите число: ")

while not user_input.isdigit() :
    print("Это не число типа int.")
    user_input = input("Введите число: ")

user_input = int(user_input)
s=''
if user_input%2==0:
    s='четный'
else:
    s='нечетный'
print(f'Вы ввели число типа int:, {user_input} этот число {s}')