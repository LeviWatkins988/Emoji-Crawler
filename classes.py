import os
import random
import copy

class Entity():
    def __init__(self, health, melee_dmg, emoji):
        self.__health = health
        self.__melee_dmg = melee_dmg
        self.__emoji = emoji
    
    
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, new_health):
        if type(new_health) == int:
            if new_health < 0:
                print("Health has to be positive, setting health to zero")
                self.__health = 0
            else:
                self.__health = new_health
        else:
            print("Health has to be int")
    
    @property
    def emoji(self):
        return self.__emoji
    @emoji.setter
    def emoji(self, new_emoji):
        if type(new_emoji) == str:
            self.__emoji = new_emoji
        else:
            print("New emoji has to be a string")

    @property
    def melee_dmg(self):
        return self.__melee_dmg
    @melee_dmg.setter
    def melee_dmg(self, new_dmg):
        if type(new_dmg) == int:
            if new_dmg < 0:
                print("Dmg has to be positive, setting dmg to 0")
            else:
                self.__melee_dmg = new_dmg
        else:
            print("Dmg has to be int")


class Player(Entity):
    def __init__(self, health, melee_dmg, emoji):
        super().__init__(health, melee_dmg, emoji)
    
    def __str__(self):
        return f"Your Health: {self.__health}"

class Ogre(Entity):
    def __init__(self, health, melee_dmg, emoji):
        super().__init__(health, melee_dmg, emoji)

    


class Room():
    def __init__(self, entered_dir, player: Entity, end_pos=(-1,-1), width=6, height=6, floor_display="🌾", end_display="🚪", number_of_ogres=2):
        """create instance variables on intization"""
        # Entered_dir in left, right, up, or down
        # end_dir is by default -1,-1 which will be the oppsite of the player location
        self.__entered_dir = entered_dir
        self.__height = height
        self.__width = width
        self.__player = player
        self.__end_display = end_display
        self.__end_pos = self.find_intial_end_position(end_pos)
        self.__floor_display = floor_display
        self.__player_pos = self.find_intial_player_position()
        self.__ogre_cords = self.create_ogre_cords(number_of_ogres, 3)
        self.__room = self.make_room()
        
        

    #Player Pos
    @property
    def player_pos(self):
        return self.__player_pos
    @player_pos.setter
    def player_pos(self, new_pos):
        if abs(new_pos[0] - self.__player_pos[0]) > 1 or abs(new_pos[1] - self.__player_pos[1]) > 1:
            print("Player can only move one spot")
        elif not self.check_cords(new_pos):
            print("Cannot move out of bounds")
        else:
            print("should move")
            self.move_to_valid_pos(self.__player_pos, new_pos)
            self.__player_pos = new_pos
            #self.__room = self.make_room()
    
    #Height
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, new_height):
        if new_height <= 0:
            print("Height can not be 0 or negative")
        elif new_height > 20:
            print("Height cannot exceed 20")
        else:
            self.__height = new_height
            self.__room = self.make_room()
    
    #Width
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, new_width):
        if new_width <= 0:
            print("Width can not be 0 or negative")
        elif new_width > 20:
            print("Width cannot exceed 20")
        else:
            self.__width = new_width
            self.__room = self.make_room()

    #Room
    @property
    def room(self):
        return self.__room
    @room.setter
    def room(self, new_room):
        """Remakes the room based on the keys given to it"""
        if isinstance(new_room, list) and isinstance(new_room[0], list):
            for y in range(len(new_room)):
                for x in range(len(new_room[y])):
                    if new_room[y][x] == 1:
                        self.__player_pos = (x, y)
            self.__height = len(new_room)
            self.__width = len(new_room[0])
            self.__room = self.make_room()
        else:
            print("Room has to be a list of list with numbers to represt items in room")
    
    #entered_dir
    @property
    def entered_dir(self):
        return self.__entered_dir
    @entered_dir.setter
    def entered_dir(self, new_dir):
        if new_dir == "up" or new_dir == "down" or new_dir == "left" or new_dir == "right":
            self.__entered_dir = new_dir
            self.__player_pos = self.find_intial_player_position()
            self.__room = self.make_room()
        else:
            print("Not valid direction")


    def display(self):
        """Displays the room and clears"""
        #os.system("cls")
        for row in range(len(self.__room)):
            for colomn in self.__room[row]:
                if colomn == 0:
                    print(self.__floor_display, end="")
                elif colomn == self.__player:
                    print(self.__player.emoji, end="")
                elif type(colomn) == Ogre:
                    print(colomn.emoji, end="")
                elif colomn == 2:
                    print(self.__end_display, end="")
            print("")
        print(self.__ogre_cords)
        #print(self.__player)

    def create_ogre_cords(self, number, distance):
        list_of_cords = []
        while len(list_of_cords) < number:
            (x, y) = (random.randint(0, self.__width-1), random.randint(0, self.__height-1))
            if self.close_to_player((x,y), distance) and (x, y) != self.__end_pos and (x,y) not in list_of_cords:
                list_of_cords.append((x,y))
        return list_of_cords

    def make_room(self):
        """makes room. current key: 0=floor, 2=end"""
        bin_room = []
        for y in range(self.__height):
            row = []
            for x in range(self.__width):
                if (x, y) == self.__player_pos:
                    row.append(self.__player)
                elif (x,y) in self.__ogre_cords:
                    row.append(Ogre(50, 10, "👹"))
                elif(x, y) == self.__end_pos:
                    row.append(2)
                else:
                    row.append(0)
            bin_room.append(row)  
        return bin_room
    
    def determine_middle_row(self):
        """Returns the width of the room interger divsion of 2"""
        if self.__width % 2 != 0:
            return self.__width // 2
        else:
            return (self.__width // 2) - 1
    
    def determine_middle_column(self):
        """Returns the height of the room interger divsion of 2"""
        if self.__height % 2 != 0:
            return self.__height // 2
        else:
            return (self.__height // 2) - 1
        
    def find_intial_player_position(self):
        """returns a cordnate plane like position staring from the top right (x,y)"""
        if self.__entered_dir == "up":
            return (self.determine_middle_row(), 0)
        elif self.__entered_dir == "down":
            return (self.determine_middle_row(), self.__height-1)
        elif self.__entered_dir == "left":
            return (0, self.determine_middle_column())
        elif self.__entered_dir == "right":
            return (self.__width-1, self.determine_middle_column())
    
    def check_cords(self, cords):
        """Checks if the entered cords are valid entered in ()"""
        if len(self.room)-1 >= cords[1] >= 0 and len(self.room[1])-1 >= cords[0] >= 0:
            return True
        else:
            return False
    
    def find_intial_end_position(self, end_pos):
        """Sets the end position to the opposite of the starting pos if (-1,-1) entered else checks if the end pos is on board"""
        if end_pos == (-1, -1):
            if self.__entered_dir == "up":
                return (self.determine_middle_row(), self.__height-1)
            elif self.__entered_dir == "down":
                return (self.determine_middle_row(), 0)
            elif self.__entered_dir == "left":
                return (self.__width-1, self.determine_middle_column())
            elif self.__entered_dir == "right":
                return (0, self.determine_middle_column())
        elif self.check_cords(end_pos):
            print("Cords out of bounds using (0,0)")
            return (0,0) 
        else:
            return end_pos

    def process_player_cmd(self, cmd):
        """Updates the room to match the player cmd"""
        print(f"player pos before moving {self.__player_pos}")
        
        print(f"player pos after moving {self.__player_pos}")
        match cmd:
            case "right":
                next_pos = (self.__player_pos[0]+1, self.__player_pos[1])
                if self.check_cords(next_pos):
                    if self.see_cords(next_pos) == 0:
                        self.player_pos = next_pos
                    elif self.see_cords(next_pos) == 2:
                        return "end"
                    elif type(self.see_cords(next_pos)) == Ogre:
                        self.calc_player_dmg(next_pos)
            case "left":
                next_pos = (self.__player_pos[0]-1, self.__player_pos[1])
                if self.check_cords(next_pos):
                    if self.see_cords(next_pos) == 0:
                        self.player_pos = next_pos
                    elif self.see_cords(next_pos) == 2:
                        return "end"
                    elif type(self.see_cords(next_pos)) == Ogre:
                        self.calc_player_dmg(next_pos)
            case "down":
                next_pos = (self.__player_pos[0], self.__player_pos[1]+1)
                if self.check_cords(next_pos):
                    if self.see_cords(next_pos) == 0 :
                        self.player_pos = next_pos
                    elif self.see_cords(next_pos) == 2:
                        return "end"
                    elif type(self.see_cords(next_pos)) == Ogre:
                        self.calc_player_dmg(next_pos)
            case "up":
                next_pos = (self.__player_pos[0], self.__player_pos[1]-1)
                if self.check_cords(next_pos):
                    if self.see_cords(next_pos) == 0:
                        self.player_pos = next_pos
                    elif self.see_cords(next_pos) == 2:
                        return "end"
                    elif type(self.see_cords(next_pos)) == Ogre:
                        self.calc_player_dmg(next_pos)
        self.ogre_turn()
        
    
    def see_cords(self, cords):
        """Method to check what is in the inputed cords"""
        if self.check_cords(cords):
            for y in range(len(self.__room)):
                for x in range(len(self.__room[y])):
                    if (x, y) == cords:
                        return self.__room[y][x]
        else:
            print("Out of bounds: returning -1")
            return -1
    
    def close_to_player(self, cord_to_check, distance):
        """Returns true or false based on weather the cord_to_check is with in distance to player"""
        if abs(cord_to_check[0] - self.player_pos[0]) > distance or abs(cord_to_check[1] - self.player_pos[1]) > distance:
            return True
        else:
            return False
    
    def calc_player_dmg(self, next_pos):
        """Damages the entity in the next_pos using player dmg"""
        self.room[next_pos[1]][next_pos[0]].health = self.room[next_pos[1]][next_pos[0]].health - self.__player.melee_dmg
        if self.room[next_pos[1]][next_pos[0]].health == 0:
            self.room[next_pos[1]][next_pos[0]] = 0
            self.__ogre_cords.remove(next_pos)
    
    def ogre_turn(self):
        before_turn_cords = copy.deepcopy(self.__ogre_cords)
        print(f"ogre cords before moving {self.__ogre_cords}")
        for ogre in before_turn_cords:
            if ogre[0] < self.player_pos[0] and self.see_cords((ogre[0]+1, ogre[1])) == 0:
                self.__ogre_cords.append((ogre[0]+1, ogre[1]))
                self.__ogre_cords.remove(ogre)
                self.move_to_valid_pos(ogre, (ogre[0]+1, ogre[1]))
            elif ogre[0] > self.player_pos[0] and self.see_cords((ogre[0]-1, ogre[1])) == 0:
                self.__ogre_cords.append((ogre[0]-1, ogre[1]))
                self.__ogre_cords.remove(ogre)
                self.move_to_valid_pos(ogre, (ogre[0]-1, ogre[1]))
            elif ogre[1] < self.player_pos[1] and self.see_cords((ogre[0], ogre[1]+1)) == 0:
                self.__ogre_cords.append((ogre[0], ogre[1]+1))
                self.__ogre_cords.remove(ogre)
                self.move_to_valid_pos(ogre, (ogre[0], ogre[1]+1))
            elif ogre[1] > self.player_pos[1] and self.see_cords((ogre[0], ogre[1]-1)) == 0:
                self.__ogre_cords.append((ogre[0], ogre[1]-1))
                self.__ogre_cords.remove(ogre)
                self.move_to_valid_pos(ogre, (ogre[0], ogre[1]-1))
    
    def move_to_valid_pos(self, current_pos, new_pos):
        if self.check_cords(current_pos) and self.check_cords(new_pos):
            if self.see_cords(new_pos) == 0:
                print("should move")
                self.__room[new_pos[1]][new_pos[0]] = self.__room[current_pos[1]][current_pos[0]]
                self.__room[current_pos[1]][current_pos[0]] = 0




before_turn_cords = [1, 2]

for i in range(len(before_turn_cords)):
    print(i)
"""
p = Player(100, 20, "🤠")
r = Room("up", p)
r.display()
print(r.see_cords((2,6)))
"""
