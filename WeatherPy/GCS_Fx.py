### GCS_Fx (Geographic Coordinate System Functions)
### User Defined Functions
### Written by Neel K Agarwal


### <-- IMPORTED FUNCTIONS

# Function Dependencies --> Imported to Jupyter Notebook (WeatherPy.ipynb) through gcs_fx.py
from time import asctime
import matplotlib.pyplot as plt
from scipy.stats import linregress, pearsonr

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
    (correlation, _) = pearsonr(dict[x], dict[y])
    print(f'Correlation Coefficient: {correlation}')
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
        fileName = 'flushed_fig'
        outPath = f'{parent_dir}/{fileName}'
        plt.savefig(outPath)
        plt.show()
    else:
        plt.show()
        return print('| PyPlot flushed:\n' + 
                    '| Be advised - not saving')
    return print(f'| PyPlot flushed:\n' +
                f'| File saved successfully as {fileName}.')


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