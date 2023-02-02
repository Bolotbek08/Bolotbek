a = input().lower()
s = ['b', 'c', 'd', 'f', 'g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
t = ['a', 'e', 'i', 'o', 'u','y']
print(len([1 for x in list(a) if x in t]),len([1 for x in list(a) if x in s]),sep=' ',end='\n')