### GCS_Fx (Geographic Coordinate System Functions)
### User Defined Functions
### Written by Neel K Agarwal


### <-- IMPORTED FUNCTIONS

# Function Dependencies --> Imported to Jupyter Notebook (WeatherPy.ipynb) through gcs_fx.py
import requests
import numpy as np
import matplotlib.pyplot as plt
from time import asctime, sleep
from scipy.stats import linregress, pearsonr
from citipy import citipy   # Install using `pip install citipy` 
                            # --> Library finds nearest cities to coordinate pairs

# TODO
#----------------------------------------------------
# Saved File Data


#----------------------------------------------------
# Plotters --> Call upon constructor functions
def s_plot(dict, x_key, y_key):
    '''Creates a scatter plot with a DataFrame and two column labels.'''
    '''Function does not perform `plt.show()` in case of multiple plots.'''
    _, axis = plt.subplots()
    handle = axis.scatter(dict[x_key], dict[y_key], label = f'{y_key} Scatter Plot')
    plt.grid(True)
    xTitle, yTitle = __label__(x_key, y_key, True)
    title = __title__(xTitle, yTitle)
    xLabel, yLabel = __label__(x_key, y_key)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    return axis, handle

def r_plot(dict, x, y, text_pos = (0, 0), coord_sys = 'data',
            decimal = 2, line_color = 'red', line_alpha = 1,
            text_color = 'red', text_size = 14, text_alpha = 1):
    '''Linear Regression Plotter: Uses scipy.stats.linregress()'''
    '''Automatically handles multiplotting, legends, annotating, and printouts.'''
    '''Takes in a DataFrame object and desired columns to use as axes'''
    (axis, _) = s_plot(dict, x, y)
    (slope, intercept, r_value, _, _) = linregress(dict[x], dict[y])
    print(f'The r^2-value is: {r_value**2}')
    regress_vals = [val * slope + intercept for val in dict[x]]
    # TODO:
    (correlation, _) = pearsonr(dict[x], dict[y])
    print(f'Correlation Coefficient: {correlation}') # TODO /->
    axis.plot(dict[x], regress_vals, color = line_color, 
            alpha = line_alpha, label = f'{y} Linear Regression')
    equation = f'y = {round(slope, decimal)}x + {round(intercept, decimal)}'
    plt.legend(loc = 'best')
    plt.annotate(text = equation, xy = text_pos, xycoords = coord_sys,
                color = text_color, fontsize = text_size, alpha = text_alpha)
    return axis

#----------------------------------------------------
# Utilities
def flush(fileName = None, save = False, parent_dir = 'output_data'):
    '''Flushes PyPlot and saves figure if given a string for arg `fileName`'''
    '''Can save with bool `save` variable with automatic naming'''
    '''Default parent directory of `output_data`'''
    if fileName:
        outPath = f'{parent_dir}/{fileName}'
        plt.savefig(outPath)
        plt.show()
    elif save:
        fileName = 'untitled_fig'
        outPath = f'{parent_dir}/{fileName}'
        plt.savefig(outPath)
        plt.show()
    else:
        plt.show()
        return print('| PyPlot flushed:\n' + 
                    '| Be advised - not saving')
    return print(f'| PyPlot flushed:\n' +
                f'| File saved successfully as {fileName}.')

def city_generator(curve_size = 1500, lat_range:tuple = (-90, 90), lng_range:tuple = (-180, 180)):
    '''Method to randomly generator geographical coordinates and find their nearest city'''
    '''SOURCE CODE FROM edX/2U --> Modified for modulated customizable purposes'''
    cities = []
    # Create a set of random lat and lng combinations
    lats = np.random.uniform(lat_range[0], lat_range[1], size = curve_size)
    lngs = np.random.uniform(lng_range[0], lng_range[1], size = curve_size)
    lat_lngs = zip(lats, lngs)
    for coord in lat_lngs:  # Loop finds nearest city for each coordinate pair
        city = citipy.nearest_city(coord[0], coord[1]).city_name
        if city not in cities:  # Append unique city to cities (list)
            cities.append(city)
    return cities

def api_openWeather(
    query_list,
    apiKey,
    query_remainder = 1000,
    base_api = f'https://api.openweathermap.org/data/2.5/weather',
    units = 'metric',
    force_run = False
):
    query_size = len(query_list)
    queries_postAPI = query_remainder - query_size
    if force_run == False:
        if queries_postAPI < 0:
            print(
                'Sorry but this API is limited to 1000 requests per day.\n' +
                f'You\'ve requested {queries_postAPI * -1} queries too many today.\n\n' +
                f'Please try again with only {query_remainder} queries in your data set.\n' +
                'Return Error code: -1')        
            return -1
        elif (queries_postAPI < 1000):
            print(
                f'You\'ve requested {query_size} queries. You have 1000 per day.\n' +
                f'If you continue you will have only {queries_postAPI} afterwards.')
            question = 'Are you sure you want to continue? Enter y to continue: '
            flag = input(question).lower()        
        flags = {'y': True, 'yes': True, 'continue': True, 'cont': True}
        if flag in flags:
            flag = flags[flag]
    elif force_run == True:
        flag = True
    else:
        print(f'Bad input {force_run}: Quitting early')
        return -1

    if flag == True:
        # Setup for API Key, data storage, and logging counters
        url = f'{base_api}?appid={apiKey}'
        data = []
        record_count = 1
        set_count = 1
        # Data logging printout
        print(
            '\n' +
            '-----------------------------\n'
            'Beginning Data Retrieval\n' +
            '-----------------------------\n')
        # Loop through all the queries to fetch data (in this case a city's weather data)
        for i, query in enumerate(query_list):
            if (i % 50 == 0 and i >= 50):   # Group cities in sets of 50 for logging
                set_count += 1
                record_count = 1
            # Append query info to API-URL!!!
            query_url = f'{url}&q={query}&units={units}'
            print(f'Processing Record {record_count} of Set {set_count} | {query}') # Logging printout for each query
            record_count += 1
            try:
                # Run API request for each query - parse out data points and append to output list
                response = requests.get(query_url).json()
                data.append({
                    'City': query,
                    'Lat': response['coord']['lat'],
                    'Lng': response['coord']['lon'],
                    'Max Temp': response['main']['temp_max'],
                    'Humidity': response['main']['humidity'],
                    'Cloudiness': response['clouds']['all'],
                    'Wind Speed': response['wind']['speed'],
                    'Country': response['sys']['country'],
                    'Date': response['dt']
                })
            # If there's an error, skip the query
            except:
                print(f'Query {query} not found. Skipping...')
                pass
            sleep(1)    # Pause between queries to avoid rate limiting
        # Indicate that Data Loading is complete
        print(
            '\n' +
            '-----------------------------\n' +
            'Data Retrieval Complete\n' +
            '-----------------------------\n')
        return data
    else:
        print('\nAPI call canceled! \nReturn Code: 0')
        return 0


#----------------------------------------------------
# Constructors
def __date__(Numerical_Month = True):
    '''!!!Private constructor used by `__title__` constructor only!!!'''
    '''Method uses system's Unix Timestamp and returns str date in form: `YYYY-MM-DD`'''
    time_curr = asctime()
    time_year = time_curr[-4:]
    time_month = time_curr[4:7]
    time_day = time_curr[8:10]
    if Numerical_Month == True:
        month_dict = {
            'Jan': '01', 'Feb': '02', 'Mar': '03',
            'Apr': '04', 'May': '05', 'Jun': '06',
            'Jul': '07', 'Aug': '08', 'Sep': '09',
            'Oct': '10', 'Nov': '11', 'Dec': '12'
        }
        time_month = month_dict[time_month]
    return f'{time_year}-{time_month}-{time_day}'

def __label__(xLabel, yLabel, form_switch = False):
    '''!!!Private constructor used by `Plotter` functions only!!!'''
    '''Takes inputs of 2 label names from exisitng directories to make graph-ready with units'''
    '''Non-required arg of form_switch indicates constructing title parts for __title__ constructor'''
    label_dict = {      # For Axis Label Corrections
        'Lat': 'Latitude',
        'Lng': 'Longitude',
        'Max Temp': 'Max Temperature (C)',
        'Humidity': 'Humidity (%)',
        'Cloudiness': 'Cloudiness (%)',
        'Wind Speed': 'Wind Speed (m/s)'
        }
    if form_switch:
        label_dict = {      # For Title corrections and creation
            'Lat': 'Latitude',
            'Lng': 'Longitude',
            'Max Temp': 'Max Temperature',
            'Humidity': 'Humidity',
            'Cloudiness': 'Cloudiness',
            'Wind Speed': 'Wind Speed'
            }
    if xLabel in label_dict:
        xLabel = label_dict[xLabel]
    if yLabel in label_dict:
        yLabel = label_dict[yLabel]
    return xLabel, yLabel

def __title__(xTitle, yTitle):
    '''!!!Private constructor used by `Plotter` Functions only!!!'''
    ''''Self-contained function needed for plotting methods'''
    ''''Returns the complete title of a graph'''
    title = f'City {xTitle} vs. {yTitle} ({__date__()})'
    return title

# TODO:
# def __correlation__(coefficient):


### IMPORTED FUNCTIONS /-->


#----------------------------------------------------
# If running directly:
if __name__ == '__main__':
    delim_index = __file__.rfind('/')
    fileName = __file__[(delim_index + 1):]
    print(f'| Executing {fileName}...\n' +
        '| File not intended as independent script.\n' +
        f'| {fileName} is library of user defined functions.\n' +
        '| Please see: https://github.com/Neelka96/python-api-challenge')