# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.


def average(scores):
    cnt = 0
    sum_ = 0

    for i in scores:
        cnt += 1 
        sum_ += i

    return sum_ / cnt
    # 여기에 코드를 작성하여 함수를 완성합니다.
"""
total = 0
length = 0

def average(scores):
    for score in scores:
        total += score
        length += 1
    return total / length



"""

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(average(scores))    # 82.5