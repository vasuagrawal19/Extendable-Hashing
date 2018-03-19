a = int(raw_input("Enter the capacity of Bucket\n"))

class Bucket(object):
    def __init__(self):
        self.buc = {}
        self.degree = 2

    def full(self):
        return len(self.buc) >= a

    def put(self, key, value):
        self.buc[key] = value

class Hashing(object):

    def __init__(self):
        self.num=0
        self.global_deg = 2
        self.dic =[]
        while self.num<4:
            p = Bucket()
            self.num+=1
            self.dic.append(p)

    def put(self, key, value):
        p = self.dic[key & ((1 << self.global_deg) - 1)]
        if p.full() and p.degree == self.global_deg:
            self.dic *= 2
            self.global_deg += 1


        if p.full() and p.degree < self.global_deg:
            p.put(key, value)
            p1 = Bucket()
            self.num+=1
            p2 = Bucket()
            for k2, v2 in p.buc.items():
                h = k2 & ((1 << self.global_deg) - 1)
                if (h >> p.degree) == 1:
                    p2.put(k2, v2)
                else:
                    p1.put(k2, v2)

            for i, x in enumerate(self.dic):
                if x == p:
                    if (i >> p.degree) == 1:
                        self.dic[i] = p2
                    else:
                        self.dic[i] = p1

            p2.degree = p1.degree = p.degree + 1
        else:
            p.put(key, value)


s = map(int,raw_input("Enter the numbers to be added \n").split())
for t in s:
    t=t%16
exhash = Hashing()
for x in s:
    exhash.put(x,x)
num=0
l=len(exhash.dic)
f=len(str(bin(l))[2:])-1
for p in exhash.dic:
    print str(bin(num)[2:]).zfill(f)+" -",
    for t in p.buc.values():
        print t,
    print
    num+=1
    