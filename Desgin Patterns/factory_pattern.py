"""Demonstration of the factory pattern, which becomes very important
when trying to avoid multiple classes to create the same type of objects
Can be expanded a lot, for example with pizza sizes and customer input """


class iPizza:
    """Factory pattern for all Pizzas of an online shop
    Args:
        Toppings, Pizza Style
    returns:
        a Pizza object """

    def __init__(self, style='New York', topping="Margarita"):
        self.style = style
        self.topping = topping
        self.prizelist = {
            "Margharita": 18.99,
            "Salami": 21.25,
            "Toronto": 23.99,
            "Sampi": 29.99
        }

    def get_prize(self):
        """accesses the prizelist
        returns:
            price for the pizza"""
        return self.prizelist[self.topping]

    def __repr__(self):
        return f"This is a {self.topping} pizza!"


def main():
    """function to create a few instances of our factory function & print
    them for us to see """
    Margharita = iPizza()
    Salami = iPizza(topping="Salami")
    print(Margharita)
    print(Salami)
    print("A salami pizza will cost you $", Salami.get_prize())


if __name__ == "__main__":
    main()
