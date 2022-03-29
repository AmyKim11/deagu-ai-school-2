members = ['Amy','doctor']
for member in members:
   print('member',member)

members2 = [
   ['Amy','seoul','programmer'],
   ['doctor','london','dba']
]   
print(members2[0][0])
for member in members2:
   print(member[0],member[1])

Amy = {'name': 'Amy', 'city': 'seoul','job':'programmer'} #사전형
print(Amy['city'])
for name in Amy:
   print(Amy[name])

members3 = [
   {'name': 'Amy', 'city': 'seoul','job':'programmer'},
   {'name': 'doctor', 'city': 'london','job':'dba'}
]  
for member in members3:
#   print(member)
   print(member['city'])


