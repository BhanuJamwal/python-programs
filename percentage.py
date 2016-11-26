n=int(raw_input())
dict={}
for line in range(n):
    info = raw_input().split(" ")
    score = list(map(float, info[1:]))
    dict[info[0]] = sum(score)/float(len(score))
print "%.2f" %round(dict[raw_input()],2)