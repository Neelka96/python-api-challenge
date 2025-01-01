### GCS_Fx (Geographic Coordinate System Functions)
### User Defined Functions
### Written by Neel K Agarwal


### <-- IMPORTED FUNCTIONS

# Function Dependencies --> Imported to Jupyter Notebook (WeatherPy.ipynb) through gcs_fx.py
from time import asctime
import matplotlib.pyplot as plt
from scipy.stats import linregress

#----------------------------------------------------
# Plotters --> Call upon constructor functions
def s_plot(dict, x_key, y_key):
    '''Creates a scatter plot with a DataFrame and two column labels.'''
    '''Function does not perform `plt.show()` in case of multiple plots.'''
    _, axis = plt.subplots()
    handle = axis.scatter(x = dict[x_key], y = dict[y_key], label = f'{y_key} Scatter Plot')
    plt.grid(True)
    xTitle, yTitle = __label__(x_key, y_key, True)
    title = __title__(xTitle, yTitle)
    xLabel, yLabel = __label__(x_key, y_key)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    return axis, handle

def r_plot(dict, x, y, decimal = 2):
    '''Linear Regression Plotter: Uses scipy.stats.linregress()'''
    '''Automatically handles multiplotting, legends, annotating, and printouts.'''
    '''Takes in a DataFrame object and desired columns to use as axes'''
    (axis, _) = s_plot(dict, x, y)
    (slope, intercept, r_value, _, _) = linregress(dict[x], dict[y])
    print(f'The r^2-value is: {r_value**2}')
    regress_vals = []
    for val in dict[x]:
        regress_vals.append(val * slope + intercept)
    axis.plot(dict[x], regress_vals, color = 'r', alpha = 0.9, label = f'{y} Linear Regression')
    equation = f'y = {round(slope, decimal)}x + {round(intercept, decimal)}'
    plt.legend(loc = 'best')
    # TODO:
    # xCord = 
    # yCord =
    # plt.annotate(text = equation, xycoords = 'axes points', xy = (),
    #             color = 'r', fontsize = 12, alpha = 1)
    return axis

#----------------------------------------------------
# Utilities
def flush(fileName = None, save = False, parent_dir = 'output_data'):
    '''Saves current pyplot object and displays it (and flushing pyplot)'''
    '''Required arg `fileName` to name new .png figure'''
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