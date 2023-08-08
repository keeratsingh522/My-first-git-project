class B:
    def __init__(self,aname,lname,aage):
        self.aname = aname
        self.lname = lname
        self.aage = aage

    def infor(self):
        return f"My name is {self.aname} {self.lname} \n I am {self.aage} years old."

b = B("Keeart","Singh",37)
print(b.infor())       