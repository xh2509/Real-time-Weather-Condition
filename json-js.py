import json
import os
import re


with open('updated_weather.json', 'r') as file:
    res = []
    res = file.readlines()
with open('updated_weather.js', "w") as resfile:
    resfile.write('var testData2 = {"type":"FeatureCollection","features":')
    for r in res:
        resfile.write('\n' + r + ','+'\n')
        resfile.write('\n};')


