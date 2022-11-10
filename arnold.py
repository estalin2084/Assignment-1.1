class Meal(object):
    def __init__(self, id, name, price): 
        self.id = id
        self.name = name 
        self.price = price
        self.quantity = 1

class Address(object):
    street_number = ''
    street_name = ''
    unit = ''
    city = ''
    province = ''
    postal_code = ''
    special_instruccions = ''
    
    def __str__(self) -> str:
        return " ".join([self.street_number + ", ",
                        self.street_name + ", ",
                        self.unit + ", ",
                        self.city + ", ",
                        self.province + ", ",
                        self.postal_code + ", ",
                        self.special_instruccions])

class Customer(object):
    
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.address = Address()
        self.meals = ''
        self.meals = dict()
        
    def update_shopping_cart(self, item):
        if item.id not in self.meals:
            self.meals.update({item.id: item})
        else :
            self.meals.get(item.id).quantity += 1;
        
    
    def get_total(self):
        return sum([v.price * v.quantity for _, v in self.meals.iteritems()])

    def get_num_items(self):
        return sum([v.quantity for _, v in self.meals.iteritems()])

    def remove_item(self, key):
        self.meals.pop(key)
    
    def __str__(self) -> str:
        return " ".join([self.first_name,
                        self.last_name]) + "/n" + self.address



customer = Customer();
available_meals = []
available_meals.append(Meal(1, "papa con huevo", 3))
available_meals.append(Meal(2, "arroz con carne", 2))
available_meals.append(Meal(3, "arroz con pollo", 5))
available_meals.append(Meal(4, "cereal con lech", 1))
available_meals.append(Meal(5, "Mofongo", 4.50))

#customer.first_name  = input("Customer First Name: ")
#customer.last_name = input("Customer Last Name: ")
#customer.address.street_number = input("Customer Street Number: ")
#customer.address.street_name = input("Customer Street Name: ")
#customer.address.unit = input("Customer Unit #: ")
#customer.address.city = input("Customer City: ")
#customer.address.province = input("Customer Province: ")
#customer.address.postal_code = input("Customer Postal Code: ")
#customer.address.special_instruccions =  input("Customer address Special Instructions:")

customer.first_name = "Adolf"
customer.last_name = "Hittler"

run = True

while run == True:
        
    for x, meal in enumerate(available_meals):
        print(str(x + 1) + " - " + meal.name)
        
    option_meal = input("Elija un plato :")
    
    current_meal = available_meals[(int(option_meal) - 1)]
    
    customer.update_shopping_cart(current_meal)

    print("customer order :")
    for x, item in customer.meals.items():
        print("nombre: " + customer.meals.get(item.id).name + " Quantity: " + str(customer.meals.get(item.id).quantity))