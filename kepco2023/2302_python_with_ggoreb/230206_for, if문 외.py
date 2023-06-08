# # # #띄어쓰기 하는 법: print(i, end='')
# #
# # # for i in range(1, 10):
# # #         print(i, end='')
# #
# # # for i in range(1, 10):
# # #         print(i)
# #
# #
# # # #구구단
# #
# # # for i in range(1,10):
# # #     print(f"2 * {i} = {2*i}, ", end='')
# #
# #
# # # for i in range(1,10):
# # #     print('------', end='')
# #
# #
# # # for i in range(1,10):
# # #     if i % 2 == 0:
# # #         print(i)
# #
# #
# # # #더하기
# #
# # # sum=0
# # # for i in range(1, 100):
# # #     sum += i
# # #     print(sum)
# #
# #
# # # #짝수 더하기
# #
# # # sum=0
# # # for i in range(1, 100):
# # #     if i % 2==0:
# # #         sum += i
# # # print(sum)
# #
# #
# # # #break문
# #
# # # print(sum)
# # # i=0
# # # while i < 10:
# # #     if i == 5:
# # #         break
# # #     print(i)
# # #     i += 1
# #
# #
# # # for i in range(10):
# # #     if i == 5:
# # #         break
# # #     print(i)
# # # print(i)
# #
# #
# # # #민지 찾기
# # # student_list=['연화','남호','민지', '상훈','소연']
# #
# # # count=0
# # # for student in student_list:
# # #     if student == '민지':
# # #         print(f"찾았다!{student}, {count}")
# # #         break
# # #     count += 1
# #
# #
# # # #countinue-띄어넘는다
# #
# # # for i in range(10):
# # #     if i == 5:
# # #         continue
# # #     print(i, end='')
# # # print("end of Program")
# #
# #
# # # #야간자습-민지빼고 다 남아~
# #
# # # student_list=['연화','남호','민지', '상훈','소연']
# #
# # # for student in student_list:
# # #     if student == '민지':
# # #         continue
# # #     print(f"{student}는 야간자습을 한다.")
# #
# #
# # # #else문
# #
# # # student_list=['연화','남호','민지', '상훈','소연']
# #
# # # for student in student_list:
# # #     if student == '영민':
# # #         print(f"찾았다!{student}")
# # #         break
# # # else:
# # #     print("영민이는 없었다...")
# #
# #
# # #예제-숫자찾기
# # #내가 쓴 거
# # print("숫자를 맞혀 보세요(1~100)")
# #
# # user_input=int(input())
# #
# # for user_input in range(1,100):
# #     if user_input<3:
# # print("숫자가 너무 작습니다.")
# #     elif user_input>3:
# # print("숫자가 너무 큽니다.")
# # else:
# #     "정답입니다. 입력한 숫자는 3입니다."
# #
# #답
# import random
# guess_number=random.randint(1,100)
# print("숫자를 맞혀 보세요.(1~100)")
# user_input=int(input())
#
# while (user_input is not guess_number):
#     if user_input>guess_number:
#         print("숫자가 너무 큽니다.")
#     else:
#         print("숫자가 너무 작습니다.")
#     user_input=int(input())
# else:
#     print("정답입니다.","입력한 숫자는", user_input,"입니다.")

# #이중 반복문-안팎(밖에 1일 때 안에 10번 돌고, 밖에 10 될 때까지 반복)
# for i in range(1,10):
#     print(i, "밖의 반복")
#     for j in range(1,10):
#         print(j, "안의 반복문")

#이중 반복문:구구단
# for i in range(1,10):
#     print(j)
#     for j in range(1, 10):
#         print(f"{i} x {j} = {i*j}", end='')
#     print() #줄 띄어주는 용도



# student_list = [['연화', '남호', '민지', '상훈', '소연'],
#                 ['수민', '수성', '영호', '재현', '준영'],
#                 ['창훈', '태진', '현수', '세원', '진영']]
#
# for students in student_list:
#     for student in students:
#         print(student)


#pass 절

# kr_sc=[49,70,20,100,80]
# mt_sc=[43,59,85,30,90]
# en_sc=[49,79,48,60,100]
# midterm_sc=[kr_sc,mt_sc,en_sc]
#
# i=0
# std_sc=[0,0,0,0,0]
#
# for scores in midterm_sc:
#     for score in scores:
#         std_sc[i] += score
#         i+=1
#   i=0
# else:
#     a,b,c,d,e=std_sc
#     std_avg=[a/3, b/3, c/3, d/3, e/3]
#     print(std_avg)

#증가하는 문자열 만들기->그림 그릴 수 있음
# for i in range(1,6):
#     for j in range(0,i):
#         print("*", end='')
#     print()



