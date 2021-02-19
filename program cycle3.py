main.py

from program3.package.TDgraphics import cuboid
from program3.package.TDgraphics import sphere
from program3.package.graphics import rectangle
from program3.package.graphics import circle
# import program3.package.graphics  as ci
l=int(input("enter length of rectangle:"))
b=int(input("enter bredth of rectangle:"))
rectangle.rarea(l,b)
rectangle.rperi(l,b)
r=int(input("enter the radius of the circle:"))
circle.carea(r)
circle.cperi(r)

s=int(input("enter radius of sphere:"))
sphere.s_sphere_A(s)
sphere.s_sphere_P(s)
le=int(input("enter length of cuboid:"))
br=int(input("enter bredth of cuboid:"))
he=int(input("enter height of cuboid:"))
cuboid.c_cuboid_A(le,br,he)
cuboid.c_cuboid_P(le,br,he)



rectangle.py

def rarea(l,b):
    area=l*b
    print("area of rectangle :",area)
def rperi(l,b):
    peri=2*(l+b)
    print("perimeter of rectangle:" , peri)
    

circle.py

def carea(r):
    area2=3.14*r*r
    print("area of circle:",area2)
def cperi(r):
    peri2=2*3.14*r
    print("perimeter of circle:",peri2)


sphere.py

def s_sphere_A(r):
    sarea=4*3.14*r
    print("surface area of sphere:",sarea)
def s_sphere_P(r):
    speri=2*3.14*r
    print("circumfereance of sphere:",speri)


cuboid.py

def c_cuboid_A(l2,b2,h2):
    careaa=2*((l2*b2)+(b2*h2)+(l2*h2))
    print("area of cuboid:",careaa)
def c_cuboid_P(l2,b2,h2):
    cperii=4*(l2+b2+h2)
    print("perimeter of cuboid:",cperii)

