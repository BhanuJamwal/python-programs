n = int(raw_input())
s=set(map(int,raw_input().split()))
x=int(raw_input())
for i in range(x):
        m=raw_input().split(" ")
        if (m[0]=="pop"):
                s.pop()
        elif (m[0]=="remove"):
                s.remove(int(m[1]))
        elif (m[0]=="discard"):
                s.discard(int(m[1]))
print sum(s)