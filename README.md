# OpenLibrary Book Search

A simple Python application for searching books on [Open Library](https://openlibrary.org/) and exporting the results to a CSV file.

## Installation

Install the project dependencies with:

```bash
pip install -r requirements.txt
```

Or, if you use `uv`:

```bash
uv sync
```

## Usage

Run the application with:

```bash
python main.py
```

Enter a book search phrase when prompted. The application retrieves up to 50 results from Open Library and keeps only books whose first publication year is after 2000.

## Output

The results are saved as a CSV file named after the search phrase in the current working directory.

The CSV file includes:

- Book title
- Authors
- First publication year
- Edition count
- Language

An example output file is available at [mobi-dick.csv](mobi-dick.csv).

## Project Structure

- `main.py` — Application entry point and configuration
- `utils.py` — API, filtering, and CSV export helper functions
- `mobi-dick.csv` — Sample output file