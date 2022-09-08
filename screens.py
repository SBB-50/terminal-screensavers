import time
import os

c = input("choose screensaver: ") 

while c == ("oline"):        
    print(" o")
    time.sleep(0.05)
    print("  o")
    time.sleep(0.05)
    print("   o")
    time.sleep(0.05)
    print("    o")
    time.sleep(0.05)
    print("     o")
    time.sleep(0.05)
    print("      o")
    time.sleep(0.05)
    print("     o")
    time.sleep(0.05)
    print("    o")
    time.sleep(0.05)
    print("   o")
    time.sleep(0.05)
    print("  o")
    time.sleep(0.05)
    print(" o")
    time.sleep(0.05)
    print("o")
    time.sleep(0.05)

if c == ("cmatrix"):
    os.system("cmatrix")


if c == ("pipes"):
    os.system("pipes.sh")

if c == ("tree"):
    print("það kemur hljóð lækkaðu rn")
    time.sleep(1)
    os.system("wisdom-tree")
