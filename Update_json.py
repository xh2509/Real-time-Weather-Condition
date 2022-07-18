# -- coding: utf-8 -#
import json
import re

with open("weather_condition.json", "r", encoding="utf-8") as f:
    load_dict_wea = json.load(f)


states_list = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District Of Columbia','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Maryland','Maine','Annapolis','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming','Puerto Rico']
weather_list = load_dict_wea
#weather_list.append(load_dict_wea)
print(weather_list)

with open("us-states.json", "r", encoding="utf-8") as f:
    load_dict = json.load(f)
    print(load_dict)

n = len(load_dict)
print(range(0,n))

for i in range(0,n):
    if states_list[i]==load_dict[i]['properties']['name']:
        load_dict[i]['properties'].update(weather_list[i])

with open("updated_weather.json", "w", encoding="utf-8") as f:
    json.dump(load_dict, f)




