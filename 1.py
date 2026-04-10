numbers = []
for i in range(10):
    num = int(input())
    numbers.append(num)
new_list = []
for i in range(8):
    summa = numbers[i] + numbers[i + 1]
    new_list.append(summa)
print(new_list)
