import re
stringExpression='''
Harry is 13 years old and his brother Sam is 12 years old. Joseph is 19 and Jessica is 22.
'''

ages=re.findall(r'\d{1,3}',stringExpression)
names=re.findall(r'[A-Z][a-z]*',stringExpression)
print(ages)
print(names)