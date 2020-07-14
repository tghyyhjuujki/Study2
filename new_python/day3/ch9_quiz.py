# #1.
# for phenotype in celegans_phenotypes:
#      print(phenotype)
# #2.
# for value in half_lives:
#  print(value, end=' ')

# #3.
# more_whales = []
# for count in whales:
#  more_whales.append(count + 1)

# #7.
# total = 0
# for population in country_populations:
#  total += population

# #8.
# #    a.
# if rat_1[0] > rat_2[0]:
#  print("첫째날 생쥐1이 생쥐2보다 몸무게가 많이 나간다.")
# else:
#  print("첫째날 생쥐1이 생쥐2보다 몸무게가 적게 나간다.")
#    b.
# if rat_1[0] > rat_2[0] and rat_1[-1] > rat_2[-1]:
#  print("생쥐1이 생쥐2보다 여전히 무겁다.")
# else
#  print("생쥐2가 생쥐1보다 무거워졌다.")
# #    c.
# if rat_1[0] > rat_2[0]:
#  if rat_1[-1] > rat_2[-1]:
#      print("생쥐1이 생쥐2보다 여전히 무겁다.")
#  else:
#      print("생쥐2가 생쥐1보다 무거워졌다.")
# else
#  print("생쥐2가 생쥐1보다 무거워졌다.")

# #10.
# for number in range(10):
#      print(10 - number, end=' ')

# #11.
# sum = 0
# count = 0
# for number in range(2,23):
#  sum += number
#  count += 1
# average = sum / count

#13.
for width in range(1, 8):
     print('T' * width)
     
print()
#14.
for width in range(1, 8):
 print(' ' * (7 - width), 'T' * width, sep='')

print()
#15.
for width in range(1, 8):
 print(' ' * (7 - width), 'T' * (width * 2 - 1), sep='')