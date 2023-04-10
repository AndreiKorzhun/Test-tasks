import json
from datetime import datetime


def json_pars(json_array, key):
    """ Takes a key and updates the date and time in all fields with that key in the dictionary. """
    if isinstance(json_array, dict):
        for i in json_array.keys():
            if i == key:
                json_array[i] = datetime.now()
            else:
                json_pars(json_array=json_array[i], key=key)
    if isinstance(json_array, list):
        for i in json_array:
            json_pars(json_array=i, key=key)
    return json_array


with open("example_2.json", "r", encoding="utf-8") as file:
    json_array = json.loads(file.read())

json_array = json_pars(json_array=json_array, key="updated")

json_data = json.dumps(json_array, indent=4, default=str)
with open("example_2.json", "w") as file:
    file.write(json_data)
