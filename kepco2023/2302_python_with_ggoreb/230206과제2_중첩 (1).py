# 정순
# for i in range(1,6):
#     for j in range(0,i):
#         print("*",end='')
#     print()
#
#
# 역순
# for i in range(6,1,-1):
#     for j in range(0,i):
#         print("*", end='')
#     print()

# #과제2
# for i in range(1,6):
#     for j in range(1,i):
#         print("ㅇ", end='')
#     print("*")

#올바른 트리
for i in range(0,14,2):
    for j in range(0,i,1):
        print("*",end='')
    for k in range(13-i,0,-2):
        print(" ",end='')
    print()

#엎어진 트리
# for i in range(0,14,2): #0부터 13까지 2칸씩 건너뜀(1,3,5,7,...)
#     for j in range(0,i,2): #빈칸은 0부터 최대 6개까지니까 2칸씩 건너뛰어준다.
#         print(" ",end='')
#     for k in range(13-i,0,-1):#별표는 한 칸씩 더해준다.
#         print("*",end='')
#     print()

