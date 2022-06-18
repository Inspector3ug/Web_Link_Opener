import webbrowser as wb
import sys
import time

time.sleep(2.5)
print(f"Welcome to Python {sys.version_info.major}.{sys.version_info.minor}!")
time.sleep(1)
web = input("Type a website here: https://")

print("Opening https://"+web+"...")
time.sleep(1.5)
wb.open("https://"+web+"")

if web == "exit":
    print("Goodbye!")
    time.sleep(3)
    sys.exit()