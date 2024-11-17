a,b,c=map(int,input().split())
time_req_to_complete = a*b
available_time = c*24*60
if time_req_to_complete<=available_time:
    print("YES")
else:
    print("NO")
