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

# 구구단 출력
'''
2*1=2 3*1=3 4*1=4
2,3,4단 전부 출력
5*1=5 6*1=6 7*1=7
5,6,7단 전부 출력
8*1=8 9*1=9
8,9단 전부 출력 
'''
