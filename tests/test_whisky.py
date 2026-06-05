from whisky_library import Whisky


def test_create_whisky():

    whisky = Whisky(
        "Woodford Reserve",
        43.2,
        750,
        68000,
        "USA",
        "Bourbon"
    )

    assert whisky.name == \
        "Woodford Reserve"


def test_bourbon():

    whisky = Whisky(
        "Woodford Reserve",
        43.2,
        750,
        68000,
        "USA",
        "Bourbon"
    )

    assert whisky.is_bourbon()