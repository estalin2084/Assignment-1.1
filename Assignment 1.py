# Name: Arnold Store II.py
# Author: Estalin Peña
# Date Created: october 06, 2022
# Date Last Modified: october 06, 2022
# Purpose: To take the order of the clients and print the receipt

from re import T


print("")



def total( ): #This funcion calculates the total of price and meal quantity
    return price * float(meal_quantity)



def subtotal(): #this function ses a list to print the subtotal
    print(list(order.keys())[0] ,"$",price , "*" , list(order.values())[0] , "=" ,"$",total())

def discount(): #this function calculates all the discounts and returns the percentages and quantiy in money.

    global percentage #this variable is set to be used globally
    global applied_disc #this variable is set to be used globally
    student_discount = .9 #this takes the .9% of the total
    global applied_student_disc #this applies the 10% to the student


    if total() < 100: #this calculates the 5% plus a 10% more in case the customer is a student
        total_w_disc = total() * 0.95
        percentage = "5%"
        applied_disc = total() *0.05 
        if student: 
            applied_student_disc = total_w_disc * .1
            total_w_disc *= student_discount
        return total_w_disc
    
    elif total() >= 100 and total () <500: #this calculates the 10% plus a 10% more in case the customer is a student
        total_w_disc = total() * 0.90
        percentage = "10%"
        applied_disc = total() *0.10
        if student:
            applied_student_disc = total_w_disc * .1
            total_w_disc *= student_discount
        return total_w_disc
    elif total() > 500: #this calculates the 15% plus a 10% more in case the customer is a student
        total_w_disc = total() * 0.85
        percentage = "15%"
        applied_disc = total() *0.15
        if student:
            applied_student_disc = total_w_disc * .1
            total_w_disc *= student_discount
        return total_w_disc
 
print("Calculating the Cost of Amazing Eats II!") #this is the name of the program
print(" ")
print(" ")
print("Welcome to Arnold's Amazing Eats II!") #this welcomes the client to the store
print("")

customer_name = input("Please enter customer's name: ") #this input takes the customer's name
customer_last_name = input("Please enter customer's last name: ") #this input takes the customer' last name
customer_street_number = input("Please enter customer's street number: ") #this input takes the customer's street number
customer_street_name = input("Please enter customer's street name: ") #this input takes the customer's street name
customer_unit = input("Please enter customer's unit #: ") #this input takes the unit # of the customer
customer_city = input("Please enter customer's city: ") #this input takes the customer's city
customer_province = input("Please enter customer's province: ") #this input takes the customer's province
customer_postal_code = input("Please enter customer's postal code: ") #this input takes the customer's postal code
customer_special_delivery_instruccions = input("Please enter customer's special delivery instructions: ") #this input takes the delivery instructions
customer_phone_number = input("Please enter customer's phone number: ") #this input takes the customer's phone number
student = False #this variable sets the student status false
print(" ") #this creaes a space beteween the customer data and the data for the order
print("What do you wish to order? ") #this aks what is to be ordered
print(" ") #this creates a speace between the order and the menu

meal_menu = ["1) Poutine", "2) French Fries"] #this variable stores the menu in a list
print(*meal_menu, sep = "\n") #this print the meal menu separated from the meal you choose
print(" ") #this create a spece between menu and the chosen meal

order = {} #this dictionary takes the order values

run = True #this is to set the while
while run == True: #this while is to repeat the order in case the client is not sure of what to order
    meal_choose = input("Choose your meal: ") #this input takes one of the 2 options
    
   
    if meal_choose == "1" or meal_choose == "2": #this decides what of the 2 plates
        meal_quantity = input("how many do you wish? ") #this input takes the quantity   
        
        meal_name = "Poutine" if meal_choose == "1" else "French Fries" #this assigns the name of the food to the varibale Meal Name
        print(meal_quantity + " " + meal_name) #this prints the quantity and the name of the food
        order.update({meal_name: meal_quantity}) #this updates the order dictionary
        
        confirmation = input("Please confirm your order [Yes/No]: ") #this confirms the order
        if confirmation.upper() == "NO" or confirmation.upper() == "N":
            continue
        elif confirmation.upper() == "YES" or confirmation.upper =="Y":
            break

        student_confirmation = input("Are you a student? [Y/N] ") #this asks if the customer is a student or no
    
        if student_confirmation.upper() == "YES" or student_confirmation.upper() == "Y": #this confirms if the customer is a student or no
            student = True
            print("You have a ten percent discount")
            break
        elif student_confirmation.upper() == "NO" or student_confirmation.upper() == "N": #this confirms if the customer is a student or no    
            break
                         
price = input("Price of the meal is: ") #this input takes the price of the meal
price = float(price) #this converts the varibale price into a float.

subtotal() #this calls the function subtotal
print("") #this creates an space 
print("") #this creates an space 
discount() #this calls the function discount  

print("{0} {1}." .format(customer_name, customer_last_name)) #this prints the customer first and last name before the receipt
print("{0} {1} {2}." .format(customer_street_number, customer_street_name, customer_unit)) #this print the address of the customer
print("{0}, {1}, {2}. " .format(customer_city, customer_province, customer_postal_code)) #this prints the city, province and postal code of the customer
print("{0}." .format(customer_special_delivery_instruccions)) #this prints the instructions in case of needing them
print(" ") #this creates an space between the customer info and the recepit

print("-" *75) #this creates the format of my recepit and the first line between the information in it
print("Order \t \t Quantity \t Item Price \t \t " " Total\t ")#this adds the headings of the recepit
print("-" *75) #this creates the format of my recepit and the second line 
print(("{}").format(meal_name), "\t" ," ",("{}").format(meal_quantity), "\t" "\t",("${:.2f}").format(price), "\t" "\t",("${:.2f}").format(total())) #this prints the name, quantity, the price and the total
print("Discount",percentage,"\t" "\t" "\t" "\t" "\t" "\t",("${}").format(applied_disc)) #this prints the percentage discounted of the order
if student == True: #if the student status is true it will print the 10% aditional discount
    print("10%" " Student savings","\t" "\t" "\t"  "\t", " ", " ", " ", ("- ${:.2f}").format(applied_student_disc))  #if the student status is true it will print the 10% aditional discount
print("\t" "\t" "\t" "\t","Subtotal" ," ", "\t", "\t", ("${:.2f}").format(total()-applied_disc)) #this prints the subtotal of the recepit
print("\t" "\t" "\t" "\t", "HST 13% ","\t" "\t",("${:.2f}").format(discount() * .13)) #this prints the tax
print("\t" "\t" "\t" "\t" " " "Total",  " \t"  "\t", ("${:.2f}").format(discount() * 1.13), "CAD") #this prints the grand total of the recepit
print("-" *75) #this creates the format of my recepit and is the last line 

run = False