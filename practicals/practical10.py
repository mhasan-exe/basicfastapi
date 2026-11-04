start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))
for i in range(end, start - 1, -1):
    if i % 2 == 0:
        print(i)
