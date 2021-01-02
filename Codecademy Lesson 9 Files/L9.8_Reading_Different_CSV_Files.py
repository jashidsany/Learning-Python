#  It’s true that CSV stands for that, but it’s also true that other ways of separating values are valid CSV files these days.
# So we call all files with a list of different values a CSV file and then use different delimiters (like a comma or tab) to indicate where the different values start and stop.

import csv

with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@'
  isbn_list = []
  isbn_list = [book['ISBN'] for book in books_reader]
