from .alcohol import Alcohol


class Whisky(Alcohol):  
    
    
    def __init__(
        self,
        name,
        abv,
        volume,
        price,
        country,
        whisky_type
    ):
        super().__init__(
            name,
            abv,
            volume,
            price
        )

        self.country = country
        self.whisky_type = whisky_type

        if not self._validate_abv():
            raise ValueError(
                "ABV must be between 0 and 100."
            )

    def _validate_abv(self):
        return (
            0 <= self.abv <= 100
        )

    def is_bourbon(self):
        return (
            self.whisky_type.lower()
            == "bourbon"
        )
    
    def is_scotch(self):
        return (
            self.whisky_type.lower()
            == "scotch"
        )
    
    def is_japanese(self):
        return (
            self.country.lower()
            == "japan"
        )