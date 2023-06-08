# print("Tell me your age?")  #if문
# myage = int(input())
# if myage <30:
#     print("Welcome to the Club.")
# else:
#     print("Oh! No. You are not accepted.")

# print("숫자를 입력해주세요")   #홀수짝수
# user_num = int(input())
# if user_num%2 == 0:
#     print("짝수입니다.")
# else :
#     print("홀수입니다.")

# print("숫자를 하나 입력해주세요")   #두수비교
# num1 = int(input())
# print("숫자를 또 하나 입력해주세요")
# num2 = int(input())
#
# if num1>num2:
#     print(num1,"가(이)", num2, "보다 더 크다")
# else:
#     print(num2,"가(이)", num1, "보다 더 크다")

# num1 = 5   #또 다른 두수 비교
# num2 = 6
# bignum = 0
# if num1> num2:
#     bignum = num1
# else:
#     bignum = num2
# print(f"더 큰수는 {bignum} 입니다.")

#목욕탕 7세미만은 어린이 요금 5000
#7세이상은 성인 요금 7000
#60세 이상은 어르신 요금 6000

# user_input = input("나이를 만으로 입력해주세요")
# age = int(user_input)
# payment = 0
#
# if age < 7:
#     payment = 5000
# elif age > 60:    # age < 60  payment = 7000 이라 해도됨
#     payment = 6000
# else :
#     payment = 7000
#
# print(f"dyrmadms {payment} 원 입니다.")

# 영어 점수를 입력 받는다
# 영어 점수가 60점 미만이면 혼남
# 60점 이상 이면 아무일도 없었다
# 70점 이상 이면 만화책
# 80점 이상 이면 용돈 10만원
# 90점 이상 이면 노트북

# print("영어 점수를 입력해주세요")
# eng_score = int(input())
# result = ""
#
# if eng_score>=90:    #범위 잘 보기!!! 이상 이하!
#     result = "노트북"
# elif eng_score>=80:
#     result = "용돈 10만원"
# elif eng_score >=70:
#     result = "만화책"
# elif eng_score>=60:
#     result = "아무일도 없다"
# else :
#     result = "혼난다"
#
# print(f"내 영어점수는 {eng_score}, 결과는 {result}")

# 세수비교
# print("수를 입력해주세요")
# num1 = input()
# print("또 다른 수를 입력해주세요")
# num2 = input()
# print("마지막 수를 입력해주세요")
# num3 = input()

# if num1>num2:
#     if num2>num3:
#         print ("제일 큰 수는",num1,"이다")
#     elif num1>num3:
#         print("제일 큰 수는",num1,"이다")
# elif num2>num3:
#     if num2>num1:
#         print("제일 큰 수는",num2,"이다")
#     elif num2>num1:
#         print("제일 큰 수는",num2,"이다")
# elif num3>num1:
#     if num1>num2:
#         print("제일 큰 수는",num3,"이다")
#     elif num3>num2:
#         print("제일 큰 수는",num3,"이다")

# num1 = 5    #강사님 세 수 비교
# num2 = 6
# num3 = 3
# bignum1 = 0
# maxnum = 0
# if num1>num2:
#     bignum1=num1
# else:
#     bignum1 = num2
#
# if bignum1>num3:
#     maxnum = bignum1
# else:
#     maxnum = num3
# print(maxnum)

# print("당신이 태어난 연도를 입력하세요.")
# birth_year = input()
# age = 2020-int(birth_year)+1
#
# if age <= 26 and age >=20:
#     print("대학생입니다")
# elif age < 20 and age >=17:
#     print("고등학생입니다")
# elif age < 17 and age >=14:
#     print("중학생입니다")
# elif age < 14 and age >=8:
#     print("초등학생입니다")
# else:
#     print("학생이 아닙니다.")

# print("주민번호 7자리를 입력해주세요")        #주민등록 번호로 나이와 성별구분
# user_input = input()
# if 2>= int(user_input[0]):
#     age = 23 - int(user_input[0:2]) + 1
# else:
#     age = 123 - int(user_input[0:2]) + 1
#
#
# if int(user_input[6])%2 == 1:
#     print(f"나이는 {age}살이고 남자입니다.")
# else:
#     print(f"나이는 {age}살이고, 여자입니다.")


# treehit = 0               #while 반복문
# while treehit < 10:
#     # treehit = treehit + 1
#     treehit +=1
#     print(f"나무를 {treehit}번 찍었습니다.")
# if treehit == 10:
#     print("나무가 쓰러집니다.")

# num = 0
# promt = """
# 1.이체
# 2.통장정리
# 3.입급
# 4.종료
#
# Enter number
# """
# while num != 4:
#     print(promt)
#     num = int(input())

# #숫자 범위를 지정해서 반복하는 for 문
# for i in range (1, 10):
#     print(i)

#list같은 순서가 있는 자료구조에서 요소를 꺼내면서 반복
# num_list = [1, 3, 5, 7, 9]
# kor_score = [49, 70, 20, 100, 80]
# math_score = [43, 59, 85, 30, 90]
# eng_score = [49, 79, 48, 60, 100]
# # for num in num_list:
# #     print(num)
# score_sum = 0
# count = 0
# for score in kor_score:
#     score_sum += score
#     print(score_sum)
#     count += 1
#
# print(f"길이{len(kor_score)}")
# print(score_sum, count, score_sum/count)

