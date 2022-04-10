# to import the entire module
import converter
# to import function from the module
from converter import kg_to_lbs

from converter import find_max


print(converter.lbs_to_kg(50))
print(kg_to_lbs(90))

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(maximum(numbers))