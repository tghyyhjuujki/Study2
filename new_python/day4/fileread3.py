import urllib.request

total_pelts = 0
url = 'https://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
with urllib.request.urlopen(url) as webpage:
  for line in webpage:
    line = line.strip()
    line = line.decode('utf-8')
    print(line)

    if line.startswith('#'):
      continue
    
    try:
      total_pelts += int(line)
    except:
      continue

print("Total number of pelts :", total_pelts)