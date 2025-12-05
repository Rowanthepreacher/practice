def calcrooms(freeroom, intwallthick):
    outwallthick = 2  # Thickness of external walls
    extraspace = outwallthick * 2  # Two external walls
    freeroom = int(freeroom)  # Ensure the free space is an integer
    intwallthick = int(intwallthick)  # Ensure the internal wall thickness is an integer
    
    # Calculate the available space for rooms (excluding external walls)
    available_space = freeroom - extraspace
    
    # Initialize a list to hold possible room configurations
    room_configs = []
    
    # Try all possible numbers of rooms
    for num_rooms in range(1, available_space + 1):
        # Calculate the total space needed for 'num_rooms' rooms
        room_length = available_space // num_rooms
        if room_length * num_rooms + (num_rooms - 1) * intwallthick == available_space:
            # Valid configuration found; add it to the list of room configurations
            room_configs.append((num_rooms, room_length))
    
    # Display the results
    if room_configs:
        print("Possible room configurations:")
        for num_rooms, room_length in room_configs:
            print(f"{num_rooms} rooms, each of length {room_length}")
    else:
        print("No valid room configurations found")

# Sample usage
calcrooms(input("How many tiles long is the available space? "), input("How thick would you like your internal walls? "))