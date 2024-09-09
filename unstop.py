class TrainCoach:
    def __init__(self):
        # Initialize 80 seats in 12 rows (11 rows with 7 seats, 1 row with 3 seats)
        self.seats = []
        self.create_seats()

    def create_seats(self):
        # Add seats to the train coach
        seat_number = 1
        for row in range(11):  # Rows 1 to 11 (7 seats each)
            self.seats.append({'row': row + 1, 'seats': [True] * 7})
        self.seats.append({'row': 12, 'seats': [True] * 3})  # Last row (3 seats)

    def display_seats(self):
        # Display seat layout: O for available, X for booked
        for row in self.seats:
            seat_display = ['O' if seat else 'X' for seat in row['seats']]
            print(f"Row {row['row']:>2}: {' '.join(seat_display)}")

    def find_and_book_seats(self, num_seats):
        # Try to find adjacent seats in one row
        for row in self.seats:
            available_seats = row['seats'].count(True)
            if available_seats >= num_seats:
                # Try to find adjacent available seats
                seat_index = self.find_adjacent_seats(row['seats'], num_seats)
                if seat_index is not None:
                    booked_seats = self.book_seats_in_row(row, seat_index, num_seats)
                    return booked_seats

        # If adjacent seats are not available, book the nearest available seats
        return self.book_nearest_seats(num_seats)

    def find_adjacent_seats(self, row_seats, num_seats):
        # Find adjacent seats in the row
        for i in range(len(row_seats) - num_seats + 1):
            if all(row_seats[i:i+num_seats]):
                return i
        return None

    def book_seats_in_row(self, row, start_index, num_seats):
        # Book seats in the given row starting from start_index
        booked_seats = []
        for i in range(start_index, start_index + num_seats):
            row['seats'][i] = False
            booked_seats.append(f"Row {row['row']} Seat {i + 1}")
        return booked_seats

    def book_nearest_seats(self, num_seats):
        # Book the nearest available seats in multiple rows
        booked_seats = []
        for row in self.seats:
            for i in range(len(row['seats'])):
                if row['seats'][i] and num_seats > 0:
                    row['seats'][i] = False
                    booked_seats.append(f"Row {row['row']} Seat {i + 1}")
                    num_seats -= 1
                if num_seats == 0:
                    return booked_seats
        return booked_seats

def main():
    train = TrainCoach()  # Create the train coach with 80 seats
    train.display_seats()  # Display the initial seat layout

    while True:
        try:
            num_seats = int(input("\nEnter number of seats to book (1-7), or 0 to exit: "))
            if num_seats == 0:
                print("Exiting...")
                break
            if num_seats < 1 or num_seats > 7:
                print("Invalid number of seats. Please enter a number between 1 and 7.")
                continue

            # Book the seats
            booked_seats = train.find_and_book_seats(num_seats)
            if booked_seats:
                print(f"Booked seats: {', '.join(booked_seats)}")
                train.display_seats()  # Display the updated seat layout
            else:
                print("Not enough seats available.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
