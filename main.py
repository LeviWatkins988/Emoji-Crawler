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
import os


def display_tutorial():
    """Displays the tutorial information then waits for input"""
    print("Move using w,a,s,d, or the arrow buttons")
    print("Press q or esc to quit")
    input("Press enter to continue")

def get_user_input():
    """Listens for key actions then returns a string of the command"""
    while True:
        if keyboard.is_pressed("w") or keyboard.is_pressed("up"):
            return "up"
        elif keyboard.is_pressed("s") or keyboard.is_pressed("down"):
            return "down"
        elif keyboard.is_pressed("a") or keyboard.is_pressed("left"):
            return "left"
        elif keyboard.is_pressed("d") or keyboard.is_pressed("right"):
            return "right"
        elif keyboard.is_pressed("q") or keyboard.is_pressed("esc"):
            quit()


def main():
    """Code that gets run when main.py gets run"""
    display_tutorial()
    player = c.Player(100, 20, "🤠") 
    room = c.Room("down", player)
    while True:
        room.display()
        print(f"Player pos: {room.player_pos}")
        print(room.room)
        user_inp = get_user_input()
        #print(f"user_inp: {user_inp}")
        room_cmd = room.process_player_cmd(user_inp)
        if room_cmd == "end":
            room = c.Room("down", player , width=(room.width+r.randint(0,2)), height=(room.height+r.randint(0,2)), number_of_ogres=((room.width * room.height)//18))
        elif room_cmd == "loss":
            os.system("cls")
            player = c.Player(100, 20, "🤠") 
            room = c.Room("down", player)
            print("You lost :(")
            while True:
                is_keep_playing = input("Restart(y/n): ").lower()
                if is_keep_playing == "y":
                    break
                elif is_keep_playing == "n":
                    quit()
                else:
                    print("invalid input please try again")


        time.sleep(.1)



if __name__ == '__main__':
    main()
        