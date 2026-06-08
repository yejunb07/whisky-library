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
        """
    Initialize an alcohol object.
    """
        self.name = name
        self.abv = abv
        self.volume = volume
        self.price = price

    def get_info(self):
        """
    Return information about the beverage.
    """
        return (
            f"{self.name} "
            f"({self.abv}% ABV)"
        )
    
    def alcohol_content(self):
        """
    Calculate pure alcohol content.
    """
        return (
            self.volume *
            self.abv /
            100
        )

    def price_per_ml(self):
        """
    Calculate price per milliliter.
    """
        return (
            self.price /
            self.volume
        )