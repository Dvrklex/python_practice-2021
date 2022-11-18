names = ['Khan', 'Omar', 'Sara', 'Ali', 'Mohammed', 'Sofia', 'Mateo']
ages = [60, 50, 55, 70, 25, 20, 40]
heights = [1.75, 1.90, 1.55, 1.80, 1.65, 1.71, 1.88]
sexs = ['M', 'M', 'F', 'M', 'M', 'F', 'M']

varones = []
mujeres = []
for e in range(len(names)):
    if sexs[e] == 'M':
        dic = {'name':names[e],'sex':sexs[e],'age':ages[e],'height':heights[e]}     
        varones.append(dic)
    else:
        dic = {'name':names[e],'sex':sexs[e],'age':ages[e],'height':heights[e]}
        mujeres.append(dic)
             
# print(varones)
# print(mujeres[0]['name'])

print('   > Mujeres menores a 55 años <')
for edad in range(len(mujeres)):
    if mujeres[edad]['age'] < 55:
        print('-',mujeres[edad]['name'])
print()
print('  > Varones mas altos que 1.85 mts <')
for altura in range(len(varones)):
    if varones[altura]['height'] > 1.85:
        print('-',varones[altura]['name'])
