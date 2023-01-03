A, B = input().split()
C = input()
A = int(A)
B = int(B)
C = int(C)
# 만약 분이랑 타이머 더한게 60분이 넘으면 
if B + C >= 60 :
    if A+((B+C)/60) > 24 :
        print(int((A+((B+C)/60))%24), (B+C)%60)
    else :
        print(int(A+((B+C)/60)), (B+C)%60)
else :
    print(A, B+C)
