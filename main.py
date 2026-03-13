"""
Emoji Crawler
By Levi Watkins
3/11/2026


Program to play a dungeon crawler type of game. 
"""

import classes as c
import random as r
import keyboard
import time
"""👹"""

def display_tutorial():
    """Displays the tutorial information then waits for input"""
    print("Move using w,a,s,d, or the arrow buttons")
    print("Press q to quit")
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
        elif keyboard.is_pressed("q"):
            quit()


def main():
    """Code that gets run when main.py gets run"""
    display_tutorial()
    player = c.Player(100, 50, "🤠")
    room = c.Room("down", player)
    while True:
        room.display()
        #print(room.room)
        #print(room.player_pos)
        user_inp = get_user_input()
        print(f"user_inp: {user_inp}")
        room_cmd = room.process_player_cmd(user_inp)
        if room_cmd == "end":
            room = c.Room("down", player , width=(room.width+r.randint(0,2)), height=(room.height+r.randint(0,2)))
        time.sleep(.1)



if __name__ == '__main__':
    main()
        