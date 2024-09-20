H,M = map(int,input().split())
#M에서 45분 빼고 마이너스일 경우엔 H에서 -1해준다.
#M < 45 이면 시간 출력 : H-1 / 분 출력 : 60+M-45 = 15+M 
if M< 45 :
    #H가 0인 경우를 생각하자
    if H==0:
        H = 23 #23으로교체
    else:
        H -=1
    print(H,15+M) 
#M >=45 이면 시간 출력 : H / 분 출력 : M-45
else:
    print(H,M-45)