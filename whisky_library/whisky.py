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
        """ABV가 0~100 사이인지 검증한다.

    :return: 유효하면 True, 아니면 False (bool)
    """
        return (
            0 <= self.abv <= 100
        )

    def is_bourbon(self):
        """
    Check whether the whisky is bourbon.
    """
        return (
            self.whisky_type.lower()
            == "bourbon"
        )

    def is_single_malt(self):
        """
    Check whether the whisky is single malt.
    """
        return (
            self.whisky_type.lower()
            == "single malt"
        )

    def is_blended(self):
        """
    Check whether the whisky is blended.
    """
        return (
            self.whisky_type.lower()
            == "blended"
        )
