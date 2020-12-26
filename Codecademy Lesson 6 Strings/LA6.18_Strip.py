# Python provides a great method for cleaning strings: .strip(). Stripping a string removes all whitespace characters from the beginning and end. Consider the following example:
# featuring = "           rob thomas                 "
# print(featuring.strip())
# => 'rob thomas'

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []

for lines in love_maybe_lines:
  love_maybe_lines_stripped.append(lines.strip())
  # appends the lines stripped

love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)
