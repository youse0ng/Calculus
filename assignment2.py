# (1~100)까지의 수 중 짝수들의 합을 구하시오.
def even_sum_function() -> int:
    i = 0 
    even_sum=0
    while i < 100:
        i += 2
        even_sum += i
    return even_sum

if __name__ == "__main__":
    print(f'1부터 100까지 수 중 짝수들의 합은 {even_sum_function()}입니다.')