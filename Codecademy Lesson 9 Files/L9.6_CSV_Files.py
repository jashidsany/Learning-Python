# Text files aren’t the only thing that Python can read, but they’re the only thing that we don’t need any additional parsing library to understand.
# CSV files are an example of a text file that impose a structure to their data. # CSV stands for Comma-Separated Values and CSV files are usually the way that data from spreadsheet software (like Microsoft Excel or Google Sheets) is exported into a portable format.

with open('logger.csv') as log_csv_file:
  print(log_csv_file.read())
