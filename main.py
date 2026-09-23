import csv
from pathlib import Path
from typing import Any

import requests

BASE_API_URL = "https://openlibrary.org/search.json"
TIMEOUT = 10
MAX_RESULTS = 50
MIN_PUBLISH_YEAR = 2000
CSV_FIELDS = (
    "key",
    "title",
    "author_key",
    "author_name",
    "first_publish_year",
    "edition_count",
    "language",
)


def fetch_books(book_name: str) -> list[dict[str, Any]]:
    """Fetch books matching ``book_name`` from Open Library."""
    response = requests.get(
        BASE_API_URL,
        params={
            "q": book_name,
            "limit": MAX_RESULTS,
            "fields": ",".join(CSV_FIELDS),
        },
        timeout=TIMEOUT,
    )
    response.raise_for_status()
    return response.json()["docs"] or []


def filter_books(books: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Keep books published after the configured minimum year."""
    return [
        book
        for book in books
        if (
            book.get("first_publish_year") is not None
            and book["first_publish_year"] > MIN_PUBLISH_YEAR
        )
    ]


def format_csv_value(value: Any) -> str:
    """Convert Open Library values, including lists, to CSV-friendly text."""
    if isinstance(value, list):
        return ",".join(str(item) for item in value)
    return str(value) if value is not None else "-"


def write_books_to_csv(books: list[dict[str, Any]], output_path: Path) -> None:
    """Write books to a CSV file using the configured columns."""
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(CSV_FIELDS)

        for book in books:
            writer.writerow(
                format_csv_value(book.get(field)) for field in CSV_FIELDS
            )


def main():
    book_name = input("Enter a book name: ").strip()
    if not book_name:
        print("Book name cannot be empty.")
        return

    print("Making request to fetch book data...")
    books = filter_books(fetch_books(book_name))

    output_path = Path(f"{book_name}.csv")
    print("Creating CSV file...")
    write_books_to_csv(books, output_path)
    print(f"Done! Saved {len(books)} books to {output_path}.")


if __name__ == "__main__":
    main()
