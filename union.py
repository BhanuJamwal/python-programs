n=int(raw_input())
e=set(map(int,raw_input().split()))
m=int(raw_input())
f=set(map(int,raw_input().split()))
q=e.union(f)
q=list(q)

print len(q)  