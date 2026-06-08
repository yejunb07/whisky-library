import pytest
from whisky_library import Whisky
from whisky_library.utils import WhiskyLibrary


def test_add_whisky():

    library = WhiskyLibrary()

    whisky = Whisky(
        "Woodford Reserve",
        43.2,
        750,
        68000,
        "USA",
        "Bourbon"
    )

    library.add_whisky(whisky)

    assert len(library.whiskies) == 1


def test_remove_whisky():

    library = WhiskyLibrary()

    whisky = Whisky(
        "Woodford Reserve",
        43.2,
        750,
        68000,
        "USA",
        "Bourbon"
    )

    library.add_whisky(whisky)

    library.remove_whisky(
        "Woodford Reserve"
    )

    assert len(
        library.whiskies
    ) == 0


def test_average_abv():

    library = WhiskyLibrary()

    library.add_whisky(
        Whisky(
            "A",
            40,
            700,
            50000,
            "USA",
            "Bourbon"
        )
    )

    library.add_whisky(
        Whisky(
            "B",
            50,
            700,
            50000,
            "Japan",
            "Scotch"
        )
    )

    assert library.average_abv() == 45


def test_total_value():

    library = WhiskyLibrary()

    library.add_whisky(
        Whisky(
            "A",
            40,
            700,
            50000,
            "USA",
            "Bourbon"
        )
    )

    library.add_whisky(
        Whisky(
            "B",
            50,
            700,
            70000,
            "Japan",
            "Scotch"
        )
    )

    assert library.total_value() == 120000

def test_invalid_abv():
    """ABV가 100 초과일 때 ValueError가 발생해야 한다."""
    with pytest.raises(ValueError):
        Whisky("Bad Whisky", 150, 700, 50000, "USA", "Bourbon")

def test_empty_library():

    library = WhiskyLibrary()

    assert (
        library.average_abv()
        == 0
    )

def test_most_expensive_empty():

    library = WhiskyLibrary()

    assert (
        library.most_expensive()
        is None
    )

def test_invalid_abv_negative():
    """ABV가 음수일 때도 ValueError가 발생해야 한다."""
    with pytest.raises(ValueError):
        Whisky("Bad", -5, 700, 50000, "USA", "Bourbon")

def test_search_by_country_no_result():
    """없는 국가로 검색하면 빈 리스트를 반환해야 한다."""
    library = WhiskyLibrary()
    library.add_whisky(Whisky("A", 43.0, 700, 50000, "USA", "Bourbon"))
    assert library.search_by_country("Japan") == []

def test_remove_nonexistent_whisky():
    """없는 위스키 삭제 시 컬렉션이 변경되지 않아야 한다."""
    library = WhiskyLibrary()
    library.add_whisky(Whisky("A", 43.0, 700, 50000, "USA", "Bourbon"))
    library.remove_whisky("없는위스키")
    assert len(library.whiskies) == 1