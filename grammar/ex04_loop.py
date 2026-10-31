for i in range(1,11,2):
    print(i)

for i in range(1,11):
    if (i % 2) == 1:
        print(i, end=" ")
print()
tot = 0; num = 10
for i in range(1,11):
    tot += i
print(tot)