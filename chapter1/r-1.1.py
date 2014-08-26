def is_multiple(n,m):
    return n % m == 0

n = 10
m = 3
if is_multiple(n,m):
    print "%s is multiple of %s" % (n,m)
else:
    print "%s is not multiple of %s" % (n,m)
    
