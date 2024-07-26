my_dikt ={'Ira' :2000, 'Misha' :2001, 'Masha' :2002}
print(my_dikt)
print(my_dikt['Ira'])
print(my_dikt.get('Anton'))
my_dikt.update({'Anton' : 2003,
                'Sergei' : 2004})
my_dikt.pop('Anton')
print(my_dikt)
my_set ={123, 'Ira',124,123, 'Ira','String', False, (4,5,6)}
print(my_set)
my_set.add(456)
my_set.add('Anton')
my_set.discard('Anton')
print(my_set)
