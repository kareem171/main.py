from room import Room
#    file        class


kitchen = Room("Kitchen")
kitchen.set_description("A desk and dirty room buzzing with flies.")


dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")


ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny floor. Huge candlesticks guard the entrance.")


kitchen.link_room(dining_hall, "south")


#
#    K
#    I
#  B-D


dining_hall.link_room
