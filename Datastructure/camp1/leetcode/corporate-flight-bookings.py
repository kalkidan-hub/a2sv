class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0]*(n+1)

        # seat reservation
        for book in bookings:
            flights[book[0]-1] += book[2]
            flights[book[1]] -= book[2]
        
        total_seats = [0]

        for flight in flights:
            total_seats.append(total_seats[-1] + flight)
        
        return total_seats[1:-1]
        