'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

numbers = int(input('숫자를 입력하세요: '))

# 아래에 코드를 작성해 주세요.
for num in range(numbers+1):
    print(num)

# 정답
for i in range(numbers+1):
    print(i+1)