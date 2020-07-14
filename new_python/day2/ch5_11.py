young = age < 45
heavy = bmi >= 22.0
if young and not heavy:
 risk = 'low'
elif young and heavy:
 risk = 'medium'
elif not young and not heavy:
 risk = 'medium'
elif not young and heavy:
 risk = 'high'