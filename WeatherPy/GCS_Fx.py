from time import asctime
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Doesn't require an argument
# Returns the current day as a string:
# Ex. 2024-04-01
def date_str(Numerical_Month = True):
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
        
    new_str = f'{time_year}-{time_month}-{time_day}'
    return f'{new_str}'

def r_plot(x_vals, y_vals, rounding = 2):
    '''Takes in iter. sequences for x axis & y axis and returns linear regression plots with seperate data'''
    (x_slope, y_intercept, r_value, p_value, std_Err) = linregress(x_vals, y_vals)
    exp_vals = x_slope * x_vals + y_intercept
    str_eq = f'y = {round(x_slope, rounding)}x + {round(y_intercept, rounding)}'
    plt.plot(x_vals, exp_vals, color = 'red')
    try:
        plt.annotate(str_eq, color = 'red', loc = 'best', fontsize = 12, alpha = 0.9)
    except Exception as e:
        print(f'Could not annotate.\Cause: {e.__cause__}\nClass: {e.__class__}')
    plt.show()
    return str_eq, exp_vals

def axis_titles():
    title_dict = {
        'Lat': 'Latitude',
        'Lng': 'Longitude',
        'Max Temp': 'Max Temperature',
        ''
    }