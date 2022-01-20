from StoreClass import Item


# Inheritance

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(
            name, price, quantity
        )

        # validation
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to Zero(0)"

        self.broken_phones = broken_phones
