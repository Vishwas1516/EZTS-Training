'''create a class car showroom in whch
1.Create a func name car company whch wll allow user to select a car company 
out of the displayed companies.if the user enters any random car company he 
or she shld be asked to re-enter 
2.acc to the car company selected the user shld be redirected to selecting 
the models of that company out of the given list.if any random then re-entered
3.After selecting model user should be redirected to selecting the varient
4.Acc to the car company model and varient a price should be calculated to which
sgst and cgst are added to make it the total price.
NOTE: SGST AND CGST ARE COMMON FOR ALL THE CARS''' 

class Showroom:
    def _init_(self,petrol,diesel,cgst,sgst):
        self.p1=petrol
        self.d1=diesel
        self.c1=cgst
        self.s1=sgst
    def varient(self):
        print("enter 1.petrol \n   2.Diesel")
        ch=int(input("enter you choice"))
        if ch==1:
            Total_price=self.p1+self.c1+self.s1+200000000
            print("Total price:",Total_price)
        else:
            Total_price=self.d1+self.c1+self.s1+200000000
            print("Total price:",Total_price)
    def mercedes_benz(self,varient):
        print("Select the models given below:")
        print("1.G WAGON \n 2.Maybach GLS")
        sel=int(input("enter your choice"))
        if sel==1:
            self.varient()
        elif sel==2:
            self.varient()
        else:
            print("invalid input")
    def bmw(self,varient):
        print("Select the models given below:")
        print("1.BMW X5 \n 2.BMW iX")
        sel=int(input("enter your choice"))
        if sel==1:
            self.varient()
        elif sel==2:
            self.varient()
        else:
            print("invalid input")
    def car_company(self):
        print("----ENTER A CAR COMPANY---")
        print("1.MERCEDES BENZ \n 2.BMW")
        ch=int(input("enter your choice"))
        if ch==1:
            self.mercedes_benz(self.varient)
        elif ch==2:
            self.bmw(self.varient)
        else:
            print("inavlid input.Re-enter the input")   

obj=Showroom(300000,250000,39099,27090)
obj.car_company()