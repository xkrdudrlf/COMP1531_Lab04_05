from abc import ABC , abstractmethod

class car(ABC):
    def __init__(self,name,rego_num,manufacturer,hirecost):
        self._name = name
        self._rego_num = rego_num
        self._manufacturer = manufacturer
        self._hirecost = hirecost
    def __str__(self):
        return "Car name: {0} Rego number: {1} Manufacturer: {2}  Hirecost: {3}".format(self._name,self._rego_num,self._manufacturer,self._hirecost) 
    def get_rego_num(self):
        return self._rego_num
    def get_name(self):
        return self._name
    def get_manufacturer(self):
        return self._manufacturer
    def get_hirecost(self):
        return self._hirecost  
    
    def set_rego_num(rego_num):
        self._rego_num = rego_num
    def set_name(name):
        self._name = name
    def set_manufacturer(manufacturer):
        self._manufacturer = manufacturer
    def set_hirecost(hirecost):
        self._hirecost = hirecost   
# do get and set for every car type class          
class small(car):
    def __init__(self,name,rego_num,manufacturer,hirecost):
        super().__init__(name,rego_num,manufacturer,hirecost)    
class large(car):
     def __init__(self,name,rego_num,manufacturer,hirecost):
        super().__init__(name,rego_num,manufacturer,hirecost)
class medium(car):
     def __init__(self,name,rego_num,manufacturer,hirecost):
        super().__init__(name,rego_num,manufacturer,hirecost)
class premium(car):
     def __init__(self,name,rego_num,manufacturer,hirecost):
        super().__init__(name,rego_num,manufacturer,hirecost)

class customer(object):
    def __init__(self,name,age,license_num,email):
        self._name = name
        self._age = age
        self._license_num = license_num
        self._email = email
    def __str__(self):
        return "name: {0} age: {1} license_num: {2}  email: {3}".format(self._name,self._age,self._license_num,self._email) 
    
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def get_license_num(self):
        return self._license_num
    def get_email(self):
        return self._email
    
    def set_name(name):
        self._name = name
    def set_age(age):
        self._age = age 
    def set_license_num(license_num):
        self._license_num = license_num
    def set_email(email):
        self._email =email  
              
class admin(object):
    def __init__(self,userID,password,manager):
        self._userID = userID
        self._password = password
        self._manager = manager
    def __str__(self):
        return "userID: {0} password: {1} Are you Manager? : {2}".format(self._userID,self._password,self._manager) 
    def get_userID(self):
        return self._userID
    def get_password(self):
        return self._password
    def get_manager(self):
        return self._manager
    
    def set_userID(userID):
        self._userID = userID 
    def set_password(password):
        self._password = password 
    def set_manager(manager):
        self._manager = manager
    
class booking(object):
    def __init__(self,car_name,customer_name,license_num,rental_period,p_location,d_location,total_fee):
        self._car_name = car_name
        self._customer_name = customer_name
        self._license_num = license_num
        self._rental_period = rental_period
        self._p_location = p_location
        self._d_location= d_location
        self._total_fee = total_fee
    def __str__(self):
        return """car_name: {0} customer_name : {1} license_num : {2}
        rental_period : {3} p_location : {4} d_location : {5} total_fee : {6} """.format(self._car_name,self._customer_name,self._license_num,self._rental_period,self._p_location,self._d_location,self._total_fee)
    def get_car_name(self):
        return self._car_name
    def get_customer_name(self):
        return self._customer_name
    def get_license_num(self):
        return self._license_num
    def get_rental_period(self):
        return self._rental_period
    def get_p_location(self):
        return self._p_location
    def get_d_location(self):
        return self._d_location
    def get_total_fee(self):
        return self._total_fee
    
    def set_car_name(car_name):
        self._car_name = car_name 
    def set_customer_name(customer_name):
        self._customer_name = customer_name 
    def set_license_num(license_num):
        self._license_num = license_num 
    def set_rental_period(rental_period):
        self._rental_period = rental_period 
    def set_p_location(p_location):
        self._p_location = p_location 
    def set_d_location(d_location):
        self._d_location = d_location 
    def set_total_fee(total_fee):
        self._total_fee = total_fee 
        
        
"""car1 = small("mazda",123,"mazda",10)
car2 = large("jeep",345,"jeep",20)

sam = customer("sam",18,777,"abc@gmail.com")
pawanjot = admin(52222,"abcd1234",True)

booking1 = booking("jeep","jeep","sam",777,14,"UNSW","UNSW",280) 

print(car1)
print(car2)
print(sam)
print(pawanjot)
print(booking1)

#car.get_name(car2)
print(car2.get_name())


"""
############### PART 2 #############

name = input("Enter your name: ")
age = input("Enter your age: ")
license_num = input("Enter your license_num: ")
email = input("Enter your email: ")
chosen_car = input("Enter the name of the car you want: ")
car.set_name(chosen_car)
a1 = car.get_name(car)
rental_period = input("Enter your rental period: ")
p_location = input("Enter your pickup location: ")
d_location = input("Enter your drop-off location: ")

cust1 = customer(name, age, license_num, email)
car1 = small("mazda",123,"mazda",10)
car2 = large("jeep",345,"jeep",20)

#Calculating total fee

def calc_fee(rental_period,hirecost):
    return hirecost*rental_period
    
total_fee = calc_fee(rental_period,car1.get_hirecost
#ar_name,manufacturer,customer_name,license_num,rental_period,p_location,d_location,total_fee
booking1 = booking(chosen_car,name,license_num,rental_period,p_location,d_location,total_fee)





