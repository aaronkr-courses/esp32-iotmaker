"""
Parse data from sensor readings.

This module defines the Parse class, which takes a dictionary of data and extracts relevant information such as sensor name, values, units, and timestamp. It provides methods to access specific values and their corresponding units.

Example usage:
data = {
    "sensor": "temperature",
    "values": {
        "current": 22.5,
        "min": 18.0,
        "max": 25.0
    },
    "unit": {
        "current": "°C",
        "min": "°C",
        "max": "°C"
    },
    "timestamp": 1625247600
}
parse = Parse(data)
print(parse.name)  # Output: temperature
print(parse.get("current"))  # Output: 22.5
print(parse.get_unit("current"))  # Output: °C
"""
class Parse:

   def __init__(self, data):

       self.data = data

       # sensor name
       self.name = data.get("sensor")

       # values
       self.values_dict = data.get("values", {})

       # sorted keys
       self.keys = list(self.values_dict.keys())
       self.keys.sort()

       # first key
       if len(self.keys):
           self.key = self.keys[0]
       else:
           self.key = None

       # values ordered by keys
       self.values = []

       for k in self.keys:
           self.values.append(self.values_dict[k])

       # first value
       if len(self.values):
           self.value = self.values[0]
       else:
           self.value = None

       # units
       self.unit = data.get("unit", {})

       # timestamp
       self.timestamp = data.get("timestamp")

   def get_unit(self, key):

       if key in self.unit:
           return self.unit[key]

       return ""

   def get(self, key, default=None):

       if key in self.values_dict:
           return self.values_dict[key]

       return default
