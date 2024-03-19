# 학번 입력하고 맨앞자리 숫자와 조건에 따라서 학과 분반 판별하기
# 조건 : 
# - 100 ~ 999 까지 입력가능

# - 맨 앞자리 숫자  == 학과 코드
#     3 == BT , 2 == IT, 1 == 정통 , 기타학과면 분반 표시 X
    

# - 00 ~ 30 == A반
# - 31 ~ 60 == B반
# - 61 ~ 99 == C반  

major = ['정통','IT','BT','ETC']

def classify_id(id_number : str) -> None:
    id_number = input("학번을 입력하시오 : ")
    if int(id_number) < 1000: # 학번이 1000이 넘지 않으면 프로그래밍 실행
        if int(id_number[0]) == 1: # 맨 앞 학번이 1 이면 정통과
            print(f'당신의 학과는 {major[0]}입니다.')
        elif int(id_number[0]) == 2: # 맨 앞 학번이 2 이면 IT과
            print(f'당신의 학과는 {major[1]}입니다.')
        elif int(id_number[0]) == 3: # 맨 앞 학번이 3 이면 BT과
            print(f'당신의 학과는 {major[2]}입니다.')
        else: # 모두 해당하지 않으면 기타학과로 분반 구별이 필요없어서 return 으로 함수문을 빠져나옴
            return print(f'당신의 학과는 {major[3]} 이므로 분반구별이 필요하지 않습니다.')
        
        # 맨 앞 학번이 1,2,3인 경우에만 해당
        if int(id_number[1:3]) < 31: # 10의자리수에 접근해서 0~30이면 A반
            print('A반 입니다')
        elif int(id_number[1:3]) < 61: # 10의 자리수가 30~60이면 B반
            print('B반 입니다.')
        else: # 10의 자리수가 60~99면 C반
            print('C반 입니다.')
    else: # 학번이 1000이 넘는다면 재귀 함수를 이용해서 다시 학번을 입력받게 넣어줌 
        classify_id(id_number) 
        
if __name__ == '__main__':
    id_number = input("학번을 입력하시오 : ")
    classify_id(id_number)