n=int(raw_input())


a=map(int,raw_input().split(" "))
b=set(a)
b=list(b)
print sum(b)/float(len(b))