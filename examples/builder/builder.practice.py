class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def build_tomato(self,tomato):
        self.burger.tomato = tomato

    def build_meal(self,meal):
        self.burger.meal = meal
    
    def build_letuce(self,letuce):
        self.burger.letuce = letuce

    def build_bread(self,bread):
        self.burger.bread = bread

    def build_sauce(self,sauce):
        self.burger.sauce = sauce    

    def get_burger(self):
        return self.burger
    

class BurgerDirector:
    def __init__(self, burger_builder):
        self.burger_builder = burger_builder

    def construct_burger(self):
        self.burger_builder.build_tomato("Red")
        self.burger_builder.build_bread("Integral")
        self.burger_builder.build_meal("Big")
        self.burger_builder.build_sauce("Spicy")

    def construct_burger_vegie(self):
        self.burger_builder.build_tomato("Red")
        self.burger_builder.build_letuce("Fresh")
        self.burger_builder.build_bread("Integral")
        self.burger_builder.build_sauce("Spicy")    

class Burger:
    def display_burger_info(self):
        print("Burger info:")
        print(f"Tomato: {self.tomato}" )
        print(f"Bread: {self.bread}" )
        print(f"meal: {self.meal}" )
        print(f"sauce: {self.sauce}" )

    def display_burger_vegie_info(self):
        print("Burger vegie info:")
        print(f"Tomato: {self.tomato}" )
        print(f"Letuce: {self.letuce}" )
        print(f"Bread: {self.bread}" )
        print(f"sauce: {self.sauce}" )    

burger_builder = BurgerBuilder()
burger_director = BurgerDirector(burger_builder)

burger_director.construct_burger_vegie()
burger = burger_builder.get_burger()

burger.display_burger_vegie_info()

