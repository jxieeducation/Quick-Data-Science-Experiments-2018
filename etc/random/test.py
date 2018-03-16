import os, sys, time

r,w=os.pipe()
r,w=os.fdopen(r,'r',0), os.fdopen(w,'w',0)

pid = os.fork()
if pid:          # Parent
    w.close()
    while 1:
        data=r.readline()
        if not data: break
        print "parent read: " + data.strip()
else:           # Child
    r.close()
    for i in range(10):
        print >>w, "line %s" % i
        w.flush()
        time.sleep(1)
