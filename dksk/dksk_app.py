# panda
# urllib3 request, error, parse, robotparser

# pip3 
# from PyQt5.QtWidgets import QApplication, Qlabel

# JSON:  {"Company_name": company_name, "Billing_address": billing_address, "Contact_name": contact_name, "Phone": Phone, "Fax": fax, "Properties": properties, 
# "Invoice_number": invoice_number, "Today_date": today_date, "Due_date": due_date, "Start_date": start_date, "End_date": enddate, "PO_number": po_number, 
# "Total_cost": total_cost}
# address = [house_number, street, city, zip_code, unit_number=null]
# properties = [address, address, address]
# contacts = [contact, contact]

import random
import hashlib
import datetime

master_list = []

class Customer:
    def __init__(self, company_name, contact_name, phone, fax, email, billing_address, properties=[]):
        self.company_name = company_name
        self.contact_name = contact_name
        self.phone = phone
        self.fax = fax
        self.email = email
        self.billing_address = billing_address
        self.properties = properties
    def total(self):
        return [self.company_name, self.contact_name, self.phone, self.fax, self.email, self.billing_address]

class Job:
    def __init__(self, company_name, property_address, po_number):
        self.company_name = company_name
        self.property_address = property_address
        self.po_number = po_number

 #   def Contact_name(self):
#        return self.contact["Contact_name"]

class Address:
    def __init__(self, house_number, street, city, zip_code, unit_number=0):
        self.house_number = house_number
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.unit_number = unit_number
    def address_list(self):
        return [self.house_number, self.street, self.city, self.zip_code, self.unit_number]

def Create_New_Client():
    c_company_name = input("What is your company name?  ")
    c_contact_name = input("Who is the contact person?  ")
    while True:
        c_phone = input("What is their phone number?  (no spaces or dashes)")
        if c_phone.isdigit():
            if len(c_phone) == 10:
                break
            else:
                print("That is not a proper phone number.")
        else:
            print("That is not a number.")
    while True:
        c_fax = input("What is their fax number?  (no spaces or dashes)")
        if c_fax.isdigit():
            if len(c_fax) == 10:
                break
            else:
                print("That is not a proper phone number.")
        else:
            print("That is not a number.")
    c_email = input("What is their e-mail address?  ")
    c_billing_address_house_number = input("What is their house number?  ")
    c_billing_address_street = input("What is their street?  ")
    c_billing_address_city = input("What is their city?  ")
    while True:
        c_billing_address_zip = input("What is their zip code?  ")
        if c_billing_address_zip.isdigit():
            if len(c_billing_address_zip) == 5:
                break
    c_billing_address_unit = input("What is the unit, if any?  ")
    billing_address = Address(c_billing_address_house_number, c_billing_address_street, c_billing_address_city, c_billing_address_zip, c_billing_address_unit)
    customer = Customer(c_company_name, c_contact_name, c_phone, c_fax, c_email, billing_address.address_list())
    master_list.append(customer.total())
    return customer

def Create_Job():
    company_name = input("What is the customer company name?  ")
    property_address = input("Which property is this?  ")
    po_number = input("Enter PO number.  (default is randomly generated)  ")
    if po_number == "":
        randnumber = random.randint(-10000, 10000)
        current_date = datetime.datetime.now()
        enco = str(randnumber) + str(current_date)
        enco_hex = hashlib.sha3_512(enco.encode())
        po_whole_number = enco_hex.hexdigest()
        po_number = po_whole_number[:10]
    return po_number

def Add_Adress():
    house_number = input("What is the house/street number?  ")
    street_number = input("What is the street name, including St, Ave, etc  ")
    city_name = input("What city is this?  ")
    zip_code = input("What is the zip code?  ")
    unit_number = input("What is the unit number?  (leave blank is a singe family home)  ")
    address = Address(house_number, street_number, city_name, zip_code, unit_number)
    print(address.address_list())
    return address

def Starter():
    while True:
        start = input("What do you want to do?  (1. create Customer, 2. Create Job, 3. Add Address)  ")
        try:
            int(start)
        except:
            print("please retry")
        else:
            if int(start) <= 3 and int(start) >=1:
                break
    if int(start) == 1:
        c = Create_New_Client()
    elif int(start) == 2:
        Create_Job()
    elif int(start) == 3:
        Add_Adress()
    else:
        print("You did something wrong in the Starter() function")


#Program starts here
Starter()

