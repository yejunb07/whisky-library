from .alcohol import Alcohol


class Whisky(Alcohol):
    """위스키를 나타내는 클래스. Alcohol을 상속한다.

    :ivar country: 원산지 국가 (str)
    :ivar whisky_type: 위스키 종류 (str)
    """

    def __init__(self, name, abv, volume, price, country, whisky_type):
        """위스키 객체를 초기화한다.

        :param name: 위스키 이름 (str)
        :param abv: 도수 % (float)
        :param volume: 용량 ml (int)
        :param price: 가격 원 (int)
        :param country: 원산지 국가 (str)
        :param whisky_type: 위스키 종류 (str)
        :raises ValueError: ABV가 0~100 범위를 벗어날 경우
        """
        super().__init__(name, abv, volume, price)
        self.country = country
        self.whisky_type = whisky_type

        if not self._validate_abv():
            raise ValueError("ABV must be between 0 and 100.")

    def _validate_abv(self):
        """ABV가 유효한 범위(0~100)인지 검증한다.

        :return: 유효하면 True, 아니면 False (bool)
        """
        return 0 <= self.abv <= 100

    def is_type(self, whisky_type):
        """위스키 종류를 확인한다 (대소문자 무관).

        :param whisky_type: 확인할 종류 문자열 (str)
        :return: 일치 여부 (bool)

        >>> w = Whisky("A", 43.0, 700, 50000, "USA", "Bourbon")
        >>> w.is_type("bourbon")
        True
        >>> w.is_type("single malt")
        False
        """
        return self.whisky_type.lower() == whisky_type.lower()

    def get_info(self):
        """위스키 상세 정보를 반환한다.

        :return: 이름, ABV, 국가, 종류를 포함한 문자열 (str)

        >>> w = Whisky("Macallan", 43.0, 700, 150000, "Scotland", "Single Malt")
        >>> "Scotland" in w.get_info()
        True
        """
        base = super().get_info()
        return f"{base} | {self.country} | {self.whisky_type}"
