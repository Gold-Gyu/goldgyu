# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calc_lunch_cost(lunch_cost):
    
    sum_ = 0
    for cost in lunch_cost.values():
        sum_ += cost

    return sum_



    # sum_ = 0

    # # lunch.append(lunch_cost.values())
    
    # sum_ = lunch_cost["김싸피"] + lunch_cost["박싸피"] + lunch_cost["이싸피"] + lunch_cost["조싸피"] + lunch_cost["최싸피"]
    # return sum_
    # 여기에 코드를 작성하여 함수를 완성합니다.

    
"""
def calc_lunch_cost(lunch_cost):
total = 0
    for cost in lunch_cost.values():
        total += cost
    return total

"""

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    lunch_cost = {
        '이싸피' : 12000,
        '김싸피' : 30000,
        '박싸피' : 10000,
        '최싸피' : 15000,
        '조싸피' : 18000, 
    }

    print(calc_lunch_cost(lunch_cost))  # 85000