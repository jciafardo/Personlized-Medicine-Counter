lists = ['jacks list', 'bobs list']
todo = ['walk dog', 'chores']


items = {
             'jacks list': ['walk dog', 'chores', 'do sum'],
             'bobs list': ['beat dick',  'slow roll',  'something else']
}

other_items = {

}

for i, char in enumerate(lists):
    other_items.update({char: [todo[i]]})

print(other_items)
print(items)
'''
for i, char in enumerate(items):
    print(items[char])
'''

