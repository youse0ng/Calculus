# 3개의 입력 변수를 받고 
# 최대 최소 구하기
def get_max(x:int,y:int,z:int) -> int:
    maximum = 0
    if x < y: maximum = y
    else: maximum = x
    if maximum < z: return z
    else: return maximum
     
def get_min(x:int,y:int,z:int) -> int:
    minimum = 0
    if x < y: minumum = x
    else: minimum = y
    if minumum < z: return minumum
    else: return z

if __name__ == '__main__':
    x,y,z=input('3개의 입력 변수를 입력하시오: ').split(' ')
    print(f'최대 값은: {get_max(int(x),int(y),int(z))}입니다.')
    print(f'최소 값은: {get_min(int(x),int(y),int(z))}입니다.')