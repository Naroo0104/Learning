#띄어쓰기 하는 법: print(i, end='')

for i in range(1, 10):
        print(i, end='')

for i in range(1, 10):
        print(i)


#구구단

for i in range(1,10):
    print(f"2 * {i} = {2*i}, ", end='')


for i in range(1,10):
    print('------', end='')


for i in range(1,10):
    if i % 2 == 0:
        print(i)


#더하기

sum=0
for i in range(1, 100):
    sum += i
    print(sum)


#짝수 더하기

sum=0
for i in range(1, 100):
    if i % 2==0:
        sum += i
print(sum)



