#  A namespace isolates the functions, classes, and variables defined in the module from the code in the file doing the importing.
# Sometimes, the module’s name could also conflict with an object you have defined within your local namespace.
# Fortunately, this name can be altered by aliasing using the as keyword:
# import module_name as name_you_pick_for_the_module
# Aliasing is most often done if the name of the library is long and typing the full name every time you want to use one of its functions is laborious.
# You might also occasionally encounter import *. The * is known as a “wildcard” and matches anything and everything.

import codecademylib3_seaborn
from matplotlib import pyplot as plt
import random

# Add your code below:
numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)
plt.plot(numbers_a, numbers_b)
plt.show()
