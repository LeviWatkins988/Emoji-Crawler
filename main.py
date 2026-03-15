"""
Emoji Crawler
By Levi Watkins
3/11/2026


Program to play a dungeon crawler type of game, using the terminal as an interface.
"""

import classes as c
import random as r
import keyboard
import time
import os


def display_tutorial():
    """Displays the tutorial information then waits for input"""
    print("You have been trapped in a endless maze of wheat, try to find the door out of this place.")
    print("Move and navigate menus using w,a,s,d, or the arrow buttons")
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

def get_nav_input():
    """Gets the input when choosing buffs"""
    while True:
        if keyboard.is_pressed("a") or keyboard.is_pressed("left"):
            return "left"
        elif keyboard.is_pressed("d") or keyboard.is_pressed("right"):
            return "right"
        elif keyboard.is_pressed(" "):
            return "space"

def select_buff(player: c.Player):
    """Gives the player a choice between a few options of buffs then returns the buffed player"""
    health_buff = r.randint(round(player.health * .5), player.health)
    dmg_buff = r.randint(1, (round(player.melee_dmg * .5)))
    current_selcetion = [">", " "]
    while True:
        os.system("cls")
        print(f" {current_selcetion[0]}{health_buff} more health       or      {current_selcetion[1]}{dmg_buff} more damge")
        print("Press space to confirm")
        cmd = get_nav_input()
        if cmd == "left":
            current_selcetion = [">", " "]
        elif cmd == "right":
            current_selcetion = [" ", ">"]
        elif cmd == "space":
            if current_selcetion == [">", " "]:
                player.health = player.health + health_buff
            elif current_selcetion == [" ", ">"]:
                player.melee_dmg = player.melee_dmg + dmg_buff
            return player


def main():
    """Code that gets run when main.py gets run"""
    display_tutorial()
    player = c.Player(100, 20, "🤠") 
    room = c.Room("down", player)
    while True:
        room.display()
        user_inp = get_user_input()
        room_cmd = room.process_player_cmd(user_inp)
        if room_cmd == "end":
            player = select_buff(player)
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
        