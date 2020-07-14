country_code = {}
country_code = {'America':'1', 'Austrailia':'61','Japan':'81','Korea':'82','China':'86'}
#print(country_code)

#print(country_code.keys())

country_code['German'] = '49'
print(country_code)
# print(country_code.values())
print(country_code.items())
print()

# method1
for item in country_code.items():
    k, v = item 
    print(item, k, v) # item -> (key, value)

print()

# method2
for k, v in country_code.items():
    print(k, v) 