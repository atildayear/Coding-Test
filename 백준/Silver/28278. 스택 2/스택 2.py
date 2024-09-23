import sys
input = sys.stdin.readline 
#입력을 빠르게 처리할 수 있음
#input()보다 속도가 빠름. 반복적으로 많은 입력 받기 가능
n = int(input()) #명령 개수 n 입력 #n번 만큼 명령 반복

stack = [] #스택 초기화

for _ in range(n):
    cmd = list(map(int,input().split()))
    #한줄에 입력된 명령을 정수로 변환 후 리스트에 저장
    
    #명령의 첫번째 값 cmd[0]
    if cmd[0]==1: 
        stack.append(cmd[1]) #스택에 넣기
    elif cmd[0]==2: #두번째 명령
        if stack: #스택이 비어있지 않으면
            print(stack.pop()) #맨위의 정수를 빼고 출력
        else:
            print(-1)
    elif cmd[0] ==3:
        print(len(stack))
    elif cmd[0] ==4:
        if stack:
            print(0)
        else:
            print(1)
    elif cmd[0] ==5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
                  


