import room as r


def main():
    room = r.Room("up")
    room.display()

    #Entered Direction
    print(room.entered_dir)
    new_dir = input("Input new dir: ")
    room.entered_dir = new_dir
    print(room.entered_dir)
    room.display()
    

    #Width
    print(room.width)
    new_width = int(input("Input new width: "))
    room.width = new_width
    print(room.width)
    room.display()
    

    #Height
    print(room.height)
    new_height = int(input("Input new height: "))
    room.height = new_height
    print(room.height)
    room.display()
    

    #Player position
    print(room.player_pos)
    new_pos = (int(input("Enter new x: ")), int(input("Enter new y: ")))
    room.player_pos = new_pos
    print(room.player_pos)
    room.display()
    

    #Room
    print(room.room)
    new_room = [[0,0,0],
                [0,1,0],
                [0,0,0]]
    input("Press enter to change the room to new room")
    room.room = new_room
    print(room.room)
    room.display()
    


if __name__ == '__main__':
    main()