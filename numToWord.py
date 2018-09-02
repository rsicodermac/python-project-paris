import n2w
from colorama import init, Fore, Back

init()

print(Back.YELLOW + Fore.RED + "Enter your number:")
y=input()
print(n2w.convert(y))