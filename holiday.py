city_prices = {
    1: {'hotel': 300, 'plane': 750, 'car': 50},  # London
    2: {'hotel': 285, 'plane': 645, 'car': 35},  # Paris
    3: {'hotel': 355, 'plane': 920, 'car': 75}   # New York
}

def itinerary():
    """Collects user inputs for city choice and length of stay,
    and calculates and returns the total holiday cost."""
    print("London, Paris, New York.")
    print("Above are some options for cities.\n")

    while True:
        try:
            city_choice = int(input("Which city would you like to travel to (London [1], Paris [2] or New York [3])?\nPlease choose associated number: "))
            if city_choice in city_prices:
                while True:
                    num_nights = int(input("How many nights would you like to stay for: "))
                    if num_nights >= 1:
                        city = city_prices[city_choice]
                        return calculate_total_cost(city, num_nights)
                    else:
                        print("\nInvalid input; please enter a number greater than 0.\n")
            else:
                print("\nInvalid choice. Please select again.\n")
        except ValueError:
            print("Please enter a number.")

def calculate_total_cost(city, num_nights):
    """Calculates the total cost of the trip based on the city prices
    and the number of nights stayed."""
    hotel_cost = city['hotel'] * num_nights
    plane_cost = city['plane']
    car_cost = city['car'] * num_nights
    return hotel_cost + plane_cost + car_cost

# Prompt the user and display the total price for the trip
print(f"The total price for the trip is: £{itinerary()}")