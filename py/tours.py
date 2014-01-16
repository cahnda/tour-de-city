class Tour():
    def __init__(self, a1, a2, a3, rate):
        self.address1 = a1
        self.address2 = a2
        self.address3 = a3
        self.rate = rate
        
    def __str__(self):
        return "%s, %s, %s: %.1f"%(t.address1, t.address2, t.address3, t.rate)

def form(t):
    return "%s, %s, %s: %.1f"%(t.address1, t.address2, t.address3, t.rate)

def average(tours): 
    temp = list(tours)
    for x in range(0,len(temp)):
        if x < len(temp):
            ratesum = temp[x].rate
            counter = 1
            for t in range(x+1,len(temp)):
                if t < len(temp):
                    if ((temp[x].address1 == temp[t].address1 or temp[x].address1 == temp[t].address2 or temp[x].address1 == temp[t].address3) and (temp[x].address2 == temp[t].address1 or temp[x].address2 == temp[t].address2 or temp[x].address2 == temp[t].address3) and (temp[x].address3 == temp[t].address1 or temp[x].address3 == temp[t].address2 or temp[x].address3 == temp[t].address3)):
                        ratesum += temp[t].rate
                        counter += 1
                        temp.pop(t)
                else:
                    break
            temp[x].rate = ratesum/counter
        else:
            break
    return temp


def organize(tours):
    tours = sorted(tours, key=lambda t: t.rate, reverse=True)
    return tours

t = Tour("address 1", "address 2", "address 3", 4.5)

t1 = Tour("this", "that", "the other", 3.0)

t2 = Tour("good", "hello", "bye", 3.79230493048302)

t3 = Tour("hello", "good", "bye", 5.0)

t4 = Tour("that", "the other", "this", 2.0)

tours = [t,t1,t2,t3,t4]

tours = average(tours)
                                                 
tours = organize(tours)

for one in tours:
    print form(one)
