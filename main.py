import classes as c
import random as r
import keyboard as k

def main():
    """Code that gets run when main.py gets run"""
    display_tutorial()
    while True:
        room = c.Room("up")
        room.display()

if __name__ == '__main__':
    main()



def display_tutorial():
    print("Move using w,a,s,d, or the arrow buttons")
    input("Press enter to continue")