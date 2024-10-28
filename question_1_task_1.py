our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}


common_destination = our_routes.intersection(competitor_routes)
print("Destination that both airlines fly to:", common_destination)

unique_our_routes = our_routes.difference(competitor_routes)
print("Destination unique to our airline:", unique_our_routes)

all_destinations = our_routes.union(competitor_routes)
all_possible_destinations = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK"}
non_shared_destinations = all_possible_destinations.difference(all_destinations)

print("Destinations that neither airline shares:", non_shared_destinations)