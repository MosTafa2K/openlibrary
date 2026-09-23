# OpenLibrary Book Search

A simple script for searching books on [Open Library](https://openlibrary.org/) and saving their information to a CSV file.

## Installation

Install the project dependency:

```bash
pip install requests
```

Or, if you use `uv`:

```bash
uv sync
```

## Usage

```bash
python main.py
```

Enter a book title or search phrase when prompted. The application retrieves up to 50 results from Open Library and keeps only books whose first publication year is after 2000.

## Output

A CSV file named after the search phrase is created in the current working directory. It includes information such as:

- Book title
- Authors
- First publication year
- Edition count
- Language