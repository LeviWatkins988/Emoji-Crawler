import classes as c
import random as r
import keyboard
import time


def display_tutorial():
    """Displays the tutorial information then waits for input"""
    print("Move using w,a,s,d, or the arrow buttons")
    input("Press enter to continue")

def get_user_input():
    """Listens for key actions then returns a string of the command"""
    while True:
        if keyboard.is_pressed("w"):
            return "up"
        elif keyboard.is_pressed("s"):
            return "down"
        elif keyboard.is_pressed("a"):
            return "left"
        elif keyboard.is_pressed("d"):
            return "right"


def main():
    """Code that gets run when main.py gets run"""
    display_tutorial()
    room = c.Room("down")
    while True:
        room.display()
        print(room.room)
        print(room.player_pos)
        user_inp = get_user_input()
        print(f"user_inp: {user_inp}")
        room.process_player_cmd(user_inp)
        time.sleep(.1)



if __name__ == '__main__':
    main()
        