def calcrooms(freeroom, room_length, intwallthick, split_gap):
    outwallthick = 2  # External wall thickness
    freeroom = int(freeroom)  # Ensure free space is an integer
    room_length = int(room_length)  # Ensure room length is an integer
    intwallthick = int(intwallthick)  # Internal wall thickness
    split_gap = int(split_gap)  # The number of rooms before a split gap

    # Calculate the available space for rooms (excluding external walls)
    available_space = freeroom - outwallthick * 2  # Subtracting the external walls on both ends

    # Initialize variables to count rooms
    total_rooms = 0
    remaining_space = available_space

    # Loop to place rooms with internal walls and split gaps
    while remaining_space >= room_length:
        rooms_in_group = 0
        group_space = 0
        
        # Add rooms to the group, considering internal walls and split gaps
        while group_space + room_length + (rooms_in_group * intwallthick) + (rooms_in_group > 0) * split_gap <= remaining_space:
            rooms_in_group += 1
            group_space = rooms_in_group * room_length + (rooms_in_group - 1) * intwallthick
            if rooms_in_group > split_gap:
                group_space += split_gap  # Add the external split gap when necessary
        
        # Update the remaining space
        remaining_space -= group_space

        total_rooms += rooms_in_group
        
    # Display the result
    print(f"You can fit {total_rooms} rooms of {room_length} tiles, considering internal walls and split gaps.")

# Sample usage
calcrooms(input("How many tiles long is the available space? "), 7, 1, 2)