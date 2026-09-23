from pathlib import Path

from utils import fetch_books, filter_books, write_books_to_csv

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


def main():
    book_name = input("Enter a book name: ").strip()
    if not book_name:
        print("Book name cannot be empty.")
        return

    print("Making request to fetch book data...")
    books = filter_books(
        fetch_books(
            BASE_API_URL,
            MAX_RESULTS,
            CSV_FIELDS,
            TIMEOUT,
            book_name,
        ),
        MIN_PUBLISH_YEAR,
    )

    output_path = Path(f"{book_name}.csv")
    print("Creating CSV file...")
    write_books_to_csv(books, output_path, CSV_FIELDS)
    print(f"Done! Saved {len(books)} books to {output_path}.")


if __name__ == "__main__":
    main()
