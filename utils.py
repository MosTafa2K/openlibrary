import csv
from pathlib import Path
from typing import Any

import requests


def fetch_books(
    api_url: str,
    max_results: int,
    fields: list[str],
    timeout: int,
    book_name: str,
) -> list[dict[str, Any]]:
    """Fetch books matching ``book_name`` from Open Library."""
    response = requests.get(
        api_url,
        params={
            "q": book_name,
            "limit": max_results,
            "fields": ",".join(fields),
        },
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()["docs"] or []


def filter_books(
    books: list[dict[str, Any]], publish_year: int
) -> list[dict[str, Any]]:
    """Keep books published after the configured minimum year."""
    return [
        book
        for book in books
        if (
            book.get("first_publish_year") is not None
            and book["first_publish_year"] > publish_year
        )
    ]


def format_csv_value(value: Any) -> str:
    """Convert Open Library values, including lists, to CSV-friendly text."""
    if isinstance(value, list):
        return ",".join(str(item) for item in value)
    return str(value) if value is not None else "-"


def write_books_to_csv(
    books: list[dict[str, Any]], output_path: Path, fields: list[str]
) -> None:
    """Write books to a CSV file using the configured columns."""
    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(fields)

        for book in books:
            writer.writerow(format_csv_value(book.get(field)) for field in fields)
