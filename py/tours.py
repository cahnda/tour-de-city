import pymongo

#client = pymongo.MongoClient()
#db = client.SSSD

connection = pymongo.MongoClient ("dbh74.mongolab.com", 27747)
db = connection ["heroku_app23236736"]
db.authenticate("softdev", "softdev")
class Tour():
    def __init__(self, names, addresses, pictures, rate):
        self.names = names
        self.addresses = addresses
        self.pictures = pictures
        self.rate = rate
        
    def __str__(self):
        return "%s: %.1f"%(t.names, t.rate)

def form(t):
    return "%s: %.1f"%(t.names, t.rate)


def average(tours):   #averages the rates of the tours with the same addresses (regardless of the order) and pops the duplicates 
    temp = list(tours)
    for x in range(0,len(temp)):
        if x < len(temp):
            ratesum = temp[x].rate
            counter = 1
            for t in range(x+1,len(temp)):
                if t < len(temp):
                    if set(temp[x].names) == set(temp[t].names):
                        ratesum += temp[t].rate
                        counter += 1
                        temp.pop(t)
                else:
                    break
            temp[x].rate = ratesum/counter
        else:
            break
    return temp

def organize(tours):  #sorts tours in descending order by rating
    tours = sorted(tours, key=lambda t: t.rate, reverse=True)
    return tours

def addTour(tour): 
    db.tours.insert({'names':tour.names, 'addresses':tour.addresses, 'pictures':tour.pictures, 'rate':tour.rate})

def _tours(res):
    res = list(res)
    ret = [Tour(t['names'], t['addresses'], t['pictures'], t['rate']) for t in res]
    # preserve ids
    for i in range(len(res)):
        ret[i]._id = str(res[i]['_id'])
    return ret
    
def getSorted():
    res = _tours(db.tours.find())
    res = average(res)
    return organize(res)[:10] if len(res) > 10 else organize(res)

#-----------------------------Tests-----------------------------------

"""t = Tour(["address 1", "address 2", "address 3"], 4.5)

t1 = Tour(["this", "that", "the other"], 3.0)

t2 = Tour(["good", "hello", "bye"], 3.79230493048302)

t3 = Tour(["hello", "good", "bye"], 5.0)

t4 = Tour(["that", "the other", "this"], 2.0)

tours = [t,t1,t2,t3,t4]

tours = average(tours)
                                                 
tours = organize(tours)

for one in tours:
    print form(one)"""
