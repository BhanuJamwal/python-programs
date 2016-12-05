n=int(raw_input())
a=set(map(int,raw_input().split()))
m=int(raw_input())
for i in range(m):
        x=raw_input().split()
        if x[0]=="intersection_update":
                b=set(map(int,raw_input().split()))
                a.intersection_update(b)
        elif x[0]=="update":
                b=set(map(int,raw_input().split()))
                a.update(b)
        elif x[0]=="symmetric_difference_update":
                b=set(map(int,raw_input().split()))
                a.symmetric_difference_update(b)
        elif x[0]=="difference_update":
                b=set(map(int,raw_input().split()))
                a.difference_update(b)
print sum(list(a))