class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return (self.width+self.height)*2
    

    def add (self):
        print(f"面積是{(self.width*self.height)}")
        print(f"周長是{(self.width+self.height)*2}")

    def resize(self,scale):
        self.width *=scale
        self.height*=scale
        print(f"已縮放，新的面積是 {self.area()}")
        print(f"已縮放，新的周長是 {self.perimeter()}")
    

A1=Rectangle(5,4)
A1.add()
A1.resize(2)