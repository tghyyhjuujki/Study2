age = int(input('나이를 입력하세요:'))
bmi = int(input('BMI를 입력하세요:'))
risk = '-'
if age < 45:
    if bmi < 22.0:
        risk = 'low'
    else:
        risk = 'medium'
else:
    if bmi < 22.0:
        risk = 'medium'
    else:
        risk = 'high'

print('나이:{},BMI:{} => RISK는 {}입니다'.format(age, bmi, risk))