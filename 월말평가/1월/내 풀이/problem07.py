# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):
    


    if len(numbers) == 1: # 입력값 1개일 때
        return (numbers[0] ** 2) * 3.14



    
    elif len(numbers) > 2: # 입력값이 3개 이상일 때
        sum_ = 0
        A = list(numbers)
        for i in range(len(numbers)):
            sum_ += A[i]
        return (sum_, (sum_ / len(numbers)))
        
        
    elif len(numbers) == 2 and (numbers[0] + numbers[1]) % 2 == 1: # 홀수
        return (numbers[0] * numbers[1]) / 2
    elif len(numbers) == 2 and (numbers[0] + numbers[1]) % 2 == 0: # 짝수
        return (numbers[0] * numbers[1])

    else:
        return 0
"""
toatl = 0
length = 0

for num in numbers:
    length += 1
    total += num

if length == 2:
    temp = numbers[0] + numbers[1]
    if temp % 2:
        return numbers[0] * numbers[1] * 0.5
    else:
        return numbers[0] * numbers[1]

elif length == 1:
    return numbers[0] * numbers[0] * 3.14

elif length > 2:
    return total, total/length
else:
    return 0


"""
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 100,100))   # (100, 25.0)
    print(calculator())                 # 0