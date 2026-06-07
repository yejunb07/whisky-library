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

    """
    Initialize an alcohol object.
    """

    def get_info(self):
        return (
            f"{self.name} "
            f"({self.abv}% ABV)"
        )
    """
    Return information about the beverage.
    """

    def alcohol_content(self):
        return (
            self.volume *
            self.abv /
            100
        )
    """
    Calculate pure alcohol content.
    """

    def price_per_ml(self):
        return (
            self.price /
            self.volume
        )
    """
    Calculate price per milliliter.
    """
    