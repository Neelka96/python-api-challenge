### GCS_Fx (Geographic Coordinate System Functions)
### User Defined Functions
### Written by Neel K Agarwal

import matplotlib.pyplot as plt
from time import asctime
from scipy.stats import linregress

def __date__(Numerical_Month = True):
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
    xLabel = label_dict[xLabel]
    yLabel = label_dict[yLabel]
    return xLabel, yLabel

def __title__(xTitle, yTitle):
    ''''Self-contained function needed for plotting methods'''
    title = f'City {xTitle} vs. {yTitle} ({__date__()})'
    return title

def save_as(fileName, parent_dir = 'output_data'):
    '''Saves current pyplot object and displays it (flushing)'''
    '''Required arg `fileName` to name new .png figure'''
    '''Default parent directory of `output_data`'''
    outPath = f'{parent_dir}/{fileName}'
    plt.savefig(outPath)
    plt.show()

def __regress__(xSeries, ySeries, rounding = 2):
    '''Takes in iter. sequences for x axis & y axis and returns linear regression plots with seperate data'''
    (x_slope, y_intercept, r_value, _, _) = linregress(xSeries, ySeries)
    exp_vals = x_slope * xSeries + y_intercept
    eq_str = f'y = {round(x_slope, rounding)}x + {round(y_intercept, rounding)}'
    r_str = f'The r^2-value is: {r_value}'
    return exp_vals, eq_str, r_str

# PLOTTERS:
def s_plot(df, xColumn, yColumn):
    '''Creates a scatter plot with a DataFrame and two column labels.'''
    '''Function does not perform `plt.show()` in case of multiple plots.'''
    _, axis = plt.subplots()
    handle = axis.scatter(x = df[xColumn], y = df[yColumn])
    plt.grid(True)
    title = __title__(__label__(xColumn, yColumn, True))
    xLabel, yLabel = __label__(xColumn, yColumn)
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    return axis, handle

def r_plot(df, xColumn, yColumn):
    axis, s_handle = s_plot(df, xColumn, yColumn)
    ySeries, rEquation, r_printout = __regress__(df[xColumn], df[yColumn])
    print(r_printout)
    l_handle, = axis.plot(ySeries, color = 'red', alpha = 0.9)
    plt.annotate(rEquation, xy = (0, 0), color = 'red', fontsize = 12, alpha = 0.9)
    plt.legend(loc = 'best')
    plt.show()

if __name__ == '__main__':
    delim_index = __file__.rfind('/')
    fileName = __file__[(delim_index + 1):]
    print(f'| Executing {fileName}...\n' +
        '| File not intended as independent script.\n' +
        f'| {fileName} is library of user defined functions.\n' +
        '| Please see: https://github.com/Neelka96/python-api-challenge')