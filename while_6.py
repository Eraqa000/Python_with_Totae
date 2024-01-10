x = int(input("vklad v bank: "))
p = int(input(f'ezhegodnyi procent: '))
y = int(input('до скольки должен дойти вклад: '))
s=0
while x<y:
    x+=round(x*(p/100),0)
    s+=1
print(f'что бы ваш вклад дошел до {y} вам понадобиться {s} лет/год ')