#입력값을 받는 부분
a=int(input()) #정수형 받기
b=input() #문자열 받기

i= len(b)-1 #i값 초기화 (b의 끝에서부터 시작)//len():문자열 길이

while i>= 0: 
    c=a*int(b[i]) #각 자리수 곱하기
    print(c) #값 먼저 보여주기

    i -=1
    
# for i in range(3,0,-1):
#     print(a*int(b[i-1]))

print(a*int(b))

