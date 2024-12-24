# Initialize the list of rooms with 'Available' status
rooms = ['Available'] * 10  # Assume the hotel has 10 rooms

def display_rooms():
    """Function to display the current room statuses."""
    print("\nRoom Statuses:")
    for i, room in enumerate(rooms, 1):
        print(f"Room {i}: {room}")

def check_availability():
    """Function to check room availability."""
    available_rooms = [i + 1 for i, room in enumerate(rooms) if room == 'Available']
    if available_rooms:
        print("\nAvailable rooms:", available_rooms)
    else:
        print("\nNo rooms available at the moment.")

def book_room():
    """Function to book a room."""
    room_number = int(input("\nEnter the room number you want to book: ")) - 1
    if 0 <= room_number < len(rooms):
        if rooms[room_number] == 'Available':
            rooms[room_number] = 'Booked'
            print(f"\nRoom {room_number + 1} has been successfully booked.")
        else:
            print(f"\nRoom {room_number + 1} is already booked.")
    else:
        print("\nInvalid room number. Please try again.")

def cancel_booking():
    """Function to cancel a booking."""
    room_number = int(input("\nEnter the room number you want to cancel: ")) - 1
    if 0 <= room_number < len(rooms):
        if rooms[room_number] == 'Booked':
            rooms[room_number] = 'Available'
            print(f"\nBooking for Room {room_number + 1} has been cancelled.")
        else:
            print(f"\nRoom {room_number + 1} is not booked.")
    else:
        print("\nInvalid room number. Please try again.")

def main():
    """Main function to drive the program."""
    while True:
        print("\nHotel Room Booking System")
        print("1. Display Room Status")
        print("2. Check Availability")
        print("3. Book a Room")
        print("4. Cancel Booking")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            display_rooms()
        elif choice == '2':
            check_availability()
        elif choice == '3':
            book_room()
        elif choice == '4':
            cancel_booking()
        elif choice == '5':
            print("\nThank you for using the Hotel Room Booking System.")
            break
        else:
            print("\nInvalid choice. Please try again.")

# Run the program
main()
