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

    try:
        Whisky(
            "Bad Whisky",
            150,
            700,
            50000,
            "USA",
            "Bourbon"
        )

        assert False

    except ValueError:
        assert True

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