n=int(raw_input())
width = len("{0:b}".format(n))
for i in xrange(1,n+1):
    a="{0:{width}d}".format(i,width=width)
    b="{0:{width}b}".format(i,width=width)
    c="{0:{width}o}".format(i,width=width)
    d= "{0:{width}x}".format(i,width=width)
    print a,c,d,b       