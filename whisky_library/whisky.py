from .alcohol import Alcohol


class Whisky(Alcohol):
    """
    Represents a whisky object.
    """

    def __init__(
        self,
        name,
        abv,
        volume,
        price,
        country,
        whisky_type
    ):
        """
    Initialize a whisky object.
    """
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
    """
    Validate ABV range.
    """

    def is_bourbon(self):
        return (
            self.whisky_type.lower()
            == "bourbon"
        )
    """
    Check whether the whisky is bourbon.
    """

    def is_single_malt(self):
        return (
            self.whisky_type.lower()
            == "single malt"
        )
    """
    Check whether the whisky is single malt.
    """

    def is_blended(self):
        return (
            self.whisky_type.lower()
            == "blended"
        )
    """
    Check whether the whisky is blended.
    """
