
class Room():
    def __init__(self, entered_dir, end_pos=(-1,-1), width=3, height=3, player_display="🤠", floor_display="🌾", end_display="🚪"):
        """create instance variables on intization"""
        # Entered_dir in left, right, up, or down
        # end_dir is by default -1,-1 which will be the oppsite of the player location
        self.__entered_dir = entered_dir
        self.__height = height
        self.__width = width
        self.__player_display = player_display
        self.__end_display = end_display
        self.__end_pos = self.find_intial_end_position(end_pos)
        self.__floor_display = floor_display
        self.__player_pos = self.find_intial_player_position()
        self.__room = self.make_room()
        

    #Player Pos
    @property
    def player_pos(self):
        return self.__player_pos
    @player_pos.setter
    def player_pos(self, new_pos):
        if abs(new_pos[0] - self.__player_pos[0]) > 1 or abs(new_pos[1] - self.__player_pos[1]):
            print("Player can only move one spot")
        elif new_pos[0] > self.__width-1 or new_pos[1] > self.__width-1:
            print("Cannot move out of bounds")
        else:
            self.__player_pos = new_pos
            self.__room = self.make_room()
    
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
        """Displays the room"""
        for row in range(len(self.__room)):
            for colomn in self.__room[row]:
                if colomn == 0:
                    print(self.__floor_display, end="")
                elif colomn == 1:
                    print(self.__player_display, end="")
                elif colomn == 2:
                    print(self.__end_display, end="")
            print("")

    def make_room(self):
        """makes room. current key: 0=floor, 1=player, 2=end"""
        bin_room = []
        for y in range(self.__height):
            row = []
            for x in range(self.__width):
                if (x, y) == self.__player_pos:
                    row.append(1)
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
        if len(self.room) >= cords[1] and len(self.room[1]) >= cords[0]:
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

