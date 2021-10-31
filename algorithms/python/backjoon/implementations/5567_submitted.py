import collections 

total = int(input())
list_length = int(input())

relations = collections.defaultdict(set)
for _ in range(list_length):
    _from, to = input().split(' ')
    relations[_from].add(to)
    relations[to].add(_from)

invitees = set(relations['1'])
copied = set(relations['1'])        

for friend in copied:
    for frend_of_friend in relations[friend]:
        if frend_of_friend == '1':
            continue
        invitees.add(frend_of_friend)
print(len(invitees))