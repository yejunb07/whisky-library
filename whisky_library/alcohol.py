class Alcohol:
    """알코올 음료를 나타내는 기본 클래스.

    :ivar name: 음료 이름 (str)
    :ivar abv: 도수 % (float)
    :ivar volume: 용량 ml (int)
    :ivar price: 가격 원 (int)
    """

    def __init__(self, name, abv, volume, price):
        """알코올 객체를 초기화한다.

        :param name: 음료 이름 (str)
        :param abv: 도수 % (float)
        :param volume: 용량 ml (int)
        :param price: 가격 원 (int)
        """
        self.name = name
        self.abv = abv
        self.volume = volume
        self.price = price

    def get_info(self):
        """음료 기본 정보를 반환한다.

        :return: 이름과 ABV를 포함한 문자열 (str)

        >>> a = Alcohol("Macallan", 40.0, 700, 100000)
        >>> a.get_info()
        'Macallan (40.0% ABV)'
        """
        return f"{self.name} ({self.abv}% ABV)"

    def alcohol_content(self):
        """순수 알코올 함량(ml)을 계산한다.

        :return: 순수 알코올 ml (float)

        >>> a = Alcohol("Test", 40.0, 700, 50000)
        >>> a.alcohol_content()
        280.0
        """
        return self.volume * self.abv / 100

    def price_per_ml(self):
        """ml당 가격을 계산한다.

        :return: ml당 가격 (float)

        >>> a = Alcohol("Test", 40.0, 700, 70000)
        >>> a.price_per_ml()
        100.0
        """
        return self.price / self.volume
