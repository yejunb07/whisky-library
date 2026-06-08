# Whisky Library

A Python package for managing whisky collections.

## Features

* Add whisky to collection
* Remove whisky from collection
* Search whisky by country
* Calculate average ABV
* Calculate total collection value
* Find the most expensive whisky

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move to the project directory:

```bash
cd whisky_library_project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```python
from whisky_library import Whisky
from whisky_library import WhiskyLibrary

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

print(library.total_value())
```

Output:

```text
68000
```

## Running Tests

Run the following command:

```bash
pytest
```

Expected result:

```text
9 passed
```

## Project Structure

```text
whisky_library_project
│
├── whisky_library
│   ├── __init__.py
│   ├── alcohol.py
│   ├── whisky.py
│   └── utils.py
│
├── tests
│   ├── test_whisky.py
│   └── test_library.py
│
├── README.md
├── requirements.txt
└── setup.py
```

## Author

- 이름: 김예준
- 학번: 202620849
- 이메일: firebird0301@gmail.com
- 과목: Python 프로그래밍
