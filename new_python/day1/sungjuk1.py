def sum(kor, eng, mat):
    result = kor + eng + mat
    return result

# 사용자1 데이터 입력
name1 = input('사용자1의 이름을 입력하세요:')
kor1 = input('사용자1의 국어 점수를 입력하세요:')
eng1 = input('사용자1의 영어 점수를 입력하세요:')
mat1 = input('사용자1의 수학 점수를 입력하세요:')

# 사용자2 데이터 입력
name2 = input('사용자2의 이름을 입력하세요:')
kor2 = input('사용자2의 국어 점수를 입력하세요:')
eng2 = input('사용자2의 영어 점수를 입력하세요:')
mat2 = input('사용자2의 수학 점수를 입력하세요:')

# 사용자3 데이터 입력
name3 = input('사용자3의 이름을 입력하세요:')
kor3 = input('사용자3의 국어 점수를 입력하세요:')
eng3 = input('사용자3의 영어 점수를 입력하세요:')
mat3 = input('사용자3의 수학 점수를 입력하세요:')

sum1 = sum(float(kor1), float(eng1), float(mat1))
sum2 = sum(float(kor2), float(eng2), float(mat2))
sum3 = sum(float(kor3), float(eng3), float(mat3))

top = max(sum1, sum2, sum3)

print('세명의 학생 중 제일 높은 총점은:{}'.format(top))
