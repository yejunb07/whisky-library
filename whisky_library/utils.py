class WhiskyLibrary:
    """위스키 컬렉션을 관리하는 클래스.

    :ivar whiskies: 위스키 객체 리스트
    """

    def __init__(self):
        """빈 위스키 컬렉션을 초기화한다."""
        self.whiskies = []

    def add_whisky(self, whisky):
        """위스키를 컬렉션에 추가한다.

        :param whisky: 추가할 Whisky 객체
        """
        self.whiskies.append(whisky)

    def remove_whisky(self, name):
        """이름으로 위스키를 컬렉션에서 제거한다.

        :param name: 제거할 위스키 이름 (str)
        """
        self.whiskies = [
            whisky
            for whisky in self.whiskies
            if whisky.name != name
        ]

    def search_by_country(self, country):
        """원산지 국가로 위스키를 검색한다 (대소문자 무관).

        :param country: 검색할 국가명 (str)
        :return: 해당 국가의 위스키 리스트 (list)

        >>> from whisky_library import Whisky
        >>> lib = WhiskyLibrary()
        >>> lib.add_whisky(Whisky("A", 43.0, 700, 50000, "USA", "Bourbon"))
        >>> len(lib.search_by_country("usa"))
        1
        """
        return [
            whisky
            for whisky in self.whiskies
            if whisky.country.lower() == country.lower()
        ]

    def average_abv(self):
        """컬렉션의 평균 ABV를 계산한다.

        :return: 평균 ABV (float), 컬렉션이 비어 있으면 0

        >>> lib = WhiskyLibrary()
        >>> lib.average_abv()
        0
        """
        if not self.whiskies:
            return 0
        return (
            sum(whisky.abv for whisky in self.whiskies)
            / len(self.whiskies)
        )

    def total_value(self):
        """컬렉션의 총 가치를 계산한다.

        :return: 총 가격 합계 원 (int)
        """
        return sum(whisky.price for whisky in self.whiskies)

    def most_expensive(self):
        """가장 비싼 위스키를 반환한다.

        :return: 가장 비싼 Whisky 객체, 비어 있으면 None

        >>> lib = WhiskyLibrary()
        >>> lib.most_expensive() is None
        True
        """
        if not self.whiskies:
            return None
        return max(self.whiskies, key=lambda whisky: whisky.price)
