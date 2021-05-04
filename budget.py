class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
    
    def deposit(self):
        return "This is deposit operations"

    def withdrawal(self):
        return "This is withdrawal operations"

    def balance(self):
        return "Available balance"

    def transfer(self):
        return "Transfer Operations"


first_category = Budget("food", 500)
second_category = Budget("entertainment", 1000)
third_category = Budget("clothing", 200)

#print(first_category.withdrawal())