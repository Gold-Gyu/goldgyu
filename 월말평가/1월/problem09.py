# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.
def dec_to_bin(number):
    #재귀함수 만들 시 무한반복을 금지할 조건을 필수로 넣어야한다.

    if number < 2:
        #재귀호출중단
        return str(number)

    else:
        # 자기 자신을 계속 호출(재귀호출)
        return dec_to_bin(number // 2) + dec_to_bin(number % 2)
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010
