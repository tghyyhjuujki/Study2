def convert_to_celisius(fahrenheit):
    result = (fahrenheit - 32) * 5 / 9 
    print('result=', result)
    return result

def add(x, y):
    result = x + y
    return result

convert_to_celisius(212)
sum = add(100, 200)
print('100 + 200 = ', sum)
