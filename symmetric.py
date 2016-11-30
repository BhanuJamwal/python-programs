n=int(raw_input())
a=set(map(int,raw_input().split()))
x=int(raw_input())
b=set(map(int,raw_input().split()))
c=a.symmetric_difference(b)
d=sorted(list(c))
for i in d:
        print i