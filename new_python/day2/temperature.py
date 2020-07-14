# temperature.py
def convert_to_celisius(fahrenheit: float) -> float:
    result = (fahrenheit - 32) * 5 / 9 
    print('result=', result)

    return result

def above_freezing(celsius: float) -> bool:
    return celsius > 0