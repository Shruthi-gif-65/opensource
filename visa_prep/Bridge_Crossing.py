a,b,c = list(map(int, input().split()))
if c>b:
    max_mangoes = (c - b)//a
else:
    max_mangoes=0
print(max_mangoes)
