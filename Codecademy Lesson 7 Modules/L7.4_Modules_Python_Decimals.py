# Let’s say you are writing software that handles monetary transactions. If you used Python’s built-in floating-point arithmetic to calculate a sum, it would result in a weirdly formatted number.

# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
# Decimal has to be applied to each float value
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)
