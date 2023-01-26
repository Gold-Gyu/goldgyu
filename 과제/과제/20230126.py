entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']



set_ = set(entry_record)

lst = []

dic_ = {}
for entry in set_:
    lst.append(entry) # 7명의 명단 완성

for i in range(len(lst)):
    dic_[lst[i]] = entry_record.count(lst[i])# 7명 각각의 이름 = key, 반복수 = value로 딕셔너리 생성

a = dic_.items() #리스트로 만들어서 정렬하기
answer1 = sorted(a, key = lambda x: x[1], reverse = True)# 반복 수가 많은 순서로 정렬

print('입장 기록 많은 Top3')
for k in range(3):
    print(f"{answer1[k][0]} {answer1[k][1]}회")

print('\n출입 기록이 수상한 사람')

# exit record 반복횟수 찾기

set_2 = set(exit_record)

lst2 = []

dic2_ = {}
for exit in set_2:
    lst2.append(exit) # 7명의 명단 완성

for i in range(len(lst2)):
    dic2_[lst2[i]] = exit_record.count(lst2[i])# 7명 각각의 이름 = key, 반복수 = value로 딕셔너리 생성

b = dic2_.items() #리스트로 만들어서 정렬하기

# answer2 = sorted(b, key = lambda x: x[1], reverse = True)

A = sorted(a)
B = sorted(b)


final = []

#exit 한 반복수와 entry한 반복횟수를 뺴야하는데 키값이 값을 때 조건을 어떻게 주지?
for num in range(len(answer1)):

    if A[num][0] == B[num][0] and A[num][1] < B[num][1]:
        final.append(A[num][0])
        final.append(A[num][1]-B[num][1])
    elif A[num][0] == B[num][0] and A[num][1] > B[num][1]:
        final.append(A[num][0])
        final.append(A[num][1]-B[num][1])


print(f"{final[2]}은 입장 기록이 {final[3]}회 더 많아 수상합니다.")
print(f"{final[0]}은 퇴장 기록이 {-final[1]}회 더 많아 수상합니다.")       


