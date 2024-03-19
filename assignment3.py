# # 엘리베이터 프로그램을 완성하시오. 사용자로부터 가고자하는 층수를 입력받은 후 엘리베이터의 운영 상태를 화면에 출력하시오

# 조건:
# - 가고자하는 층수는 사용자로부터 입력받는다.
# - 현재 층수는 5층으로 고정한다.
# - 엘리베이터가 위 또는 아래로 움직일 때 층수의 변화를 화면에 출력

def elevator_function(x:int) -> None:
    print('현재 엘리베이터는 5층에 있습니다.')
    if x - 5 < 0: # 5층보다 낮을 때
        for i in range(5,x-1,-1):
            print(f'{i}층 입니다.')

    else: # 5층보다 높을 때 
        for i in range(5,x+1):
            print(f'{i}층 입니다.')

if __name__ == '__main__':
    x = int(input('가고자 하는 층수를 입력하시오: '))
    elevator_function(x)