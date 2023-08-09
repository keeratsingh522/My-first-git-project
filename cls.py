class B:
    def __init__(self,aname,lname,aage):
        self.aname = aname
        self.lname = lname
        self.aage = aage

    def infor(self):
        return f"My name is {self.aname} {self.lname} \n I am {self.aage} years old."
    
class C(B):
    def __init__(self,aname,lname,aage,agrade,apost ):
        super().__init__(aname, lname, aage)
        self.agrade = agrade
        self.apost = apost
    
    def fullinfo(self):
        return f"My name is {self.aname} {self.lname} \n I am {self.aage} years old .Gdare is {self.agrade} post is {self.apost}"
    


b = B("Keeart","Singh",37)
# print(b.infor()) 

c = C("Mukesh","Kaur",36,"4th Grade","Programer")

print(c.fullinfo())
print(c.infor())