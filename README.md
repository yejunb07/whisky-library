# Whisky Library

위스키 관리 프로그램

## Features

* 위스키 컬렉션 추가
* 위스키 컬렉션 삭제
* 위스키 국가별 검색
* 평균 도수 계산
* 총 가격 계산
* 가장 비싼 위스키 검색

## Installation

Clone the repository:

```bash
git clone https://github.com/yejunb07/whisky-library.git
```

Move to the project directory:

```bash
cd whisky_library_project
```

Install dependencies:

```bash
pip install -r requirements.txt
pip install .
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
12 passed
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
