n,m=raw_input().split()
arr= [int(x)  for x in raw_input().split()]
a=set([int(y) for y in raw_input().split()])
b=set([int(z) for z in raw_input().split()])
count = [0 + 1 if x in a else 0-1 if x in b else 0 + 0 for x in arr]
print(sum(count)) 