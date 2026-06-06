class Alcohol:
    """
    Base class for alcoholic beverages.

    Attributes:
        name (str): Beverage name
        abv (float): Alcohol by volume
        volume (int): Volume in ml
        price (int): Price in KRW
    """

    def __init__(
        self,
        name,
        abv,
        volume,
        price
    ):
        self.name = name
        self.abv = abv
        self.volume = volume
        self.price = price

    def get_info(self):
        return (
            f"{self.name} "
            f"({self.abv}% ABV)"
        )

    def alcohol_content(self):
        return (
            self.volume *
            self.abv /
            100
        )

    def price_per_ml(self):
        return (
            self.price /
            self.volume
        )
    