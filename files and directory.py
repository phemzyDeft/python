
from pathlib import Path

path = Path()
print(path.exists())

ecommerce = Path("email")
print(ecommerce.exists())

emails = Path("email")
print(emails.mkdir())

remove = Path("email")
print(remove.rmdir())

path = Path()
print(path.glob("*.py"))

path = Path()

for file in path.glob("*"):
    print(file)

print('\n')

for file in path.glob("*.py"):
    print(file)
