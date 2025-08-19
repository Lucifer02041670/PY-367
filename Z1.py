fin_sum = 0
count = 0
number = int(input("Введите число (0 - выход): "))


while number != 0:
    fin_sum += number
    number = float(input("Введите число (0 - выход): "))
    count += 1

try:
    srZn = fin_sum / count
    print(f"Среднее значение введенных чисел: {srZn}")
except:
    print("error")