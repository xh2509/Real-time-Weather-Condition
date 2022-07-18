def algo(line):
    windspeed = line.map(lambda x: x[5]) # get data
    windspeed = windspeed.map(lambda x: x.split(' ')[0]) # split by blank and exteact the number part
    windspeed = windspeed.map(lambda x: float(x)) # convert the number part from string to float

    min_windspeed = windspeed.min()
    max_windspeed = windspeed.max()


    temperature = line.map(lambda x: x[3]) # get data
    temperature = temperature.map(lambda x: float(x)) # convert the number part from string to float

    min_temperature = temperature.min()
    max_temperature = temperature.max()


    winddir = line.map(lambda x: x[4]) # get data

    dir_freq = winddir.map(lambda x: (x,1)) # map a tuple and append int 1 as frequency for each wind direction
    dir_freq = dir_freq.reduceByKey(lambda x, y: x+y) # perform aggregation (sum) all the frequency values for each unique wind direction
    dir_freq = dir_freq.map(lambda x: (x[1], x[0])).sortByKey(False) # sort the wind direction by the frequecy

    most_freq_dir = dir_freq.map(lambda x: x[1]).take(1)[0] # get the most frequent wind direction


    weather = line.map(lambda x: x[2]) # get data
    random_weather = weather.takeSample(False, 1, None)[0] # take random sample of all possible weathers


    output = [random_weather, min_temperature, max_temperature, min_windspeed, max_windspeed, most_freq_dir]
    return output