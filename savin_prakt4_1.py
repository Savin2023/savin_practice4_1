print("Введите количество чисел, которые Вы хотите проанализировать")
n=int(input())
kolvo=0
for i in range(n):
    print("Введите",i+1,"-е целое число")
    if (int(input()))==0:
        kolvo+=1

print("Вы ввели",kolvo,"нулевых чисел")
