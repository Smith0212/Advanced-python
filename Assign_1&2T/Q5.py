class dist:
    def __init__(self,feet,inch):
        self.feet = feet
        self.inch = inch


def add(o1,o2,o3):
        totalInch = (o1.inch+o2.inch+o3.inch)
        fi = (totalInch)%12
        tf = (o1.feet+o2.feet+o3.feet) + int((totalInch)/12)

        print("Feet : " , tf , " Inch : " , fi)

d1 = dist(4,7)
d2 = dist(5,7)
d3 = dist(5,8)

add(d1,d2,d3)





