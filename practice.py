car = input("enter the car model:")
carprice = float(input("enter the car price:"))
manuyear = float(input("enter the manufacturing year"))
year = float(input("enter the present year"))
kms = float(input("enter the kms driven:"))
dents = float(input("enter the no of dents :"))
accident = float(input("enter the no accidents :"))

finalyears= (year-manuyear)
price1 = ((finalyears*0.06)*carprice)
price2 = (dents*0.00002)*carprice
price3 = ((accident*0.2)*carprice)
price4 = ((kms/10000)*0.01)
finalprice = (carprice-(price1+price2+price3+price4))
print ("final price of car:",finalprice)

