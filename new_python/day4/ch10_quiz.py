#1.
filename = input('백업할 파일명을 입력하세요 -> ')
new_filename = filename + '.bak'
backup = open(new_filename, 'w')
for line in open(filename):
 backup.write(line)
backup.close()

#2.
alkaline_metals = []
for line in open('alkaline_metals.txt'):
 alkaline_metals.append(line.strip().split(' '))