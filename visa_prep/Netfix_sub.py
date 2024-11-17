a,b,c,s=map(int,input().split())
if a+b>=s or b+c>=s or a+c>=s:
    print("YES")
else:
    print("NO")
