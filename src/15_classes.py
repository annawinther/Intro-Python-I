# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon: 

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
        self.lat_lon = {"lat": lat, "lon": lon}

    def get_lat(self):

        return {"lat": self.lat}

    def get_lon(self):

        return {"lon": self.lon}

home = LatLon("50", "130")

print(home.lat_lon)
print(home.get_lat())
print(home.get_lon())

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.


# YOUR CODE HERE
class Waypoint(LatLon): 

    def __init__(self, name, *args):
        self.name = name
        super(Waypoint, self).__init__(*args)

    def __repr__(self):

        return str({"name": self.name, "lat": self.lat, "lon": self.lon})

    def __str__(self):
        return str({"name": self.name, "lat": self.lat, "lon": self.lon})

    def get_location(self):
        return {"name": self.name, "lat": self.lat, "lon": self.lon}

point = Waypoint('home', '33', '66')

print(point.name)
print(point.get_lon())
print(point.get_lat())
print(point.get_location()

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
print(geocache)