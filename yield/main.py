#!/cygdrive/c/Python37/python
#!/usr/bin/python3

# when using cygwin with msvcrt, then make shortcut Cygwin Console instead of Cygwin Terminal
# mkshortcut -D -n "Cygwin Console" -i /Cygwin.ico /bin/bash -a --login

import msvcrt
import sys, time

print(sys.executable)
print(sys.version)

def wait(timeout=3):
    t0 = time.time()
    while time.time() < t0 + timeout:
        time.sleep(0.1*timeout)
        if msvcrt.kbhit():
            key = msvcrt.getch()
            return key
    return None

###############################################################

def f():
    print("1")
    x1 = (yield "a")    # returns "a" and blocks on x1 assignment
    print("2", x1)
    x2 = yield "b"      # returns "b" and blocks on x2 assignment
    print("3", x2)
    x3 = yield "c"      # returns "c" and blocks on x3 assignment
    print("4", x3)

# g = f()
# print(".")
# y1 = next(g)        # returns "a" and blocks until send
# print("..")
# y2 = g.send(10)     # unblocks, 10 gets assigned to x1 ... print("2", x1) executed ... returns "b" and blocks on x2
# y3 = g.send(20)     # unblocks, 20 gets assigned to x2 ... print("3", x2) executed ... returns "c" and blocks on x3
# try: g.send(30)     # unblocks, 30 gets assigned to x2 ... print("4", x3) executed ... throws StopIteration exception
# except: pass
# print(y1,y2,y3)
# sys.exit()

###############################################################

def gen123(timeout=3):
    t0 = time.time()
    while True:
        yield 1
        yield 2
        yield 3
        if time.time() >= t0 + timeout:
            break

# g = gen123(1)
# for i in g:
#     print(i)
# sys.exit()

###############################################################

def gen():
    cnt = 0
    while True:
        cnt += 1
        yield cnt
        if cnt == 10:
            break

# g = gen()
# for i in g:
#     print(i)
# sys.exit()

###############################################################

def xxx():
    x_ = 0  # initial value
    while True:
        x = yield x_
        x_ = x
        if x == 100:
            break

# steps
g = xxx()
print(next(g))  # returns initial value
print(g.send(10))
print(g.send(20))
print(g.send(30))
print(g.send(40))
print(g.send(50))
print(g.send(60))
print(g.send(70))
print(g.send(80))
print(g.send(90))
try: print(g.send(100))  # StopIterator exception
except: pass

# loop
g = xxx()
cnt = 1
x = next(g)
print(x)    # returns initial value first and blocks
while True:
    try:
        x = g.send(cnt*10)
        print(x)
        cnt += 1
    except:
        break

sys.exit()

###############################################################

def cycle():
    # values = [1,3,5,7]
    values = [0,0,0,0]
    while True:
        for v in values:
            x = yield               # returns None and blocks on x assignment
            print("received:", x)
            yield x + v

if __name__ == "__main__":
    idx = 0
    gen = cycle()
    # next(gen)     # run upto first yield
    # while gen:    # explicit call next(gen) required
    for i in gen:   # run upto first yield
        print("got", i)
        idx += 1
        print("sending", idx)
        gen.send(idx)               # unblocks and send idx to x
        if wait(0.1) != None:
            print("exiting ...")
            sys.exit()


