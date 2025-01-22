# Python API Challenge - Vacation_WeatherPy
`Module 6`  
`(edX/2U & UT) Data Analytics and Visualization Bootcamp`  
`Cohort UTA-VIRT-DATA-PT-11-2024-U-LOLC`  
`By Neel Kumar Agarwal`  

## Table of Contents  
1. [Introduction](#introduction)  
    - [WeatherPy](#weatherpy)  
    - [VacationPy](#vacationpy)  
2. [Setup and Usage](#setup-and-usage)  
    - [Prerequisites](#prerequisites)  
    - [Instructions](#instructions)  
    - [User Defined Module - gcs_fx](#user-defined-module---gcs_fx)  
3. [Files and Directory Structure](#files-and-directory-structure)  
4. [Expected Results](#expected-results)  



## Introduction  
This challenge is broken into two assignments: WeatherPy and VacationPy.  


### WeatherPy:  
Data's true power is its ability to definitively answer questions. So, let's take what  
you've learned about Python requests, APIs, and JSON traversals to answer a fundamental  
question: "What is the weather like as we approach the equator?"  

Now, we know what you may be thinking: “That's obvious. It gets hotter.” But, if pressed  
for more information, how would you prove that?  

So, in this deliverable we'll create a Python script to visualize the weather of over 500  
cities of varying distances from the equator. We'll use the citipy Python libraryLinks to  
an external site., the OpenWeatherMap APILinks to an external site., and our problem-solving  
skills to create a representative model of weather across cities.  


### VacationPy:  
Well, if we can do that, then surely we can work our magic to plan a perfect destination  
vacation based off of climate. Using the power of a different API and method for calling  
that API (as per usual), we can even graph the data in the form of a map.  

In this deliverable, we'll use your weather data skills to plan future vacations. Also,  
we'll use Jupyter notebooks, the geoViews Python library, and the Geoapify API. Our main  
tasks will be to use the Geoapify API and the geoViews Python library and to employ our  
Python skills to create map visualizations.  

[:arrow_up: Return to TOC](#table-of-contents)  


## Setup and Usage  
### Prerequisites  
- Python 3.x  
- Standard libraries: `pathlib`, `time`, `requests` (included with Python)  
- Non-standard library: `pandas`, `numpy`, `matplotlib`, `scipy`, and `citipy`  
- IDE that supports Jupyter Notebooks with Python  

[:arrow_up: Return to TOC](#table-of-contents)  



### Instructions  
1. Clone this repository.  
2. Ensure IDE is up to date and running.   
3. Open `WeatherPy.ipynb` in your IDE and run all cells.  
4. If the necessary dependencies aren't found, install using the following methods:  
    - For *pip*  
        `pip install <missing_library>`  
    - For *anaconda*  
        `conda install <missing_library>`  
> [!WARNING]  
> Please note that neither *pathlib*, *time*, nor *requests* was installed using conda.  
> *pathlib*, *time*, and *requests* are base modules almost always included with Python  
> installations. It is recommended to use `pip install` for these two modules to avoid  
> path dependencies.  
5. IDE/Terminal (depending on how code is being executed) will prompt user for 'confirm'
6. **Results will print throughout the Jupyter Interactive Notebook**  

[:arrow_up: Return to TOC](#table-of-contents)  



### User Defined Module - gcs_fx
A small python file has been created alongside the Jupyter Notebook `WeatherPy.ipynb` for the  
purpose of creating a separation between the heavy-lifting of graphing methods required by the  
assigned challenge, as a microcosm version of a 'back-end'. Said file is named GCS_Fx.py and  
runs under the alias gcs in the notebook. Modules `numpy`, `matplotlib.pyplot`, `time`, `scipy`,  
`citipy`, and `requests` have all been transferred to GCS_Fx to enhance readability of WeatherPy  
and allow for focus of modifying data as DataFrames via `pandas` and duplicating graphs with  
reoccurring corrections of labels and titles. The automatic generation of geographic coordinate  
pairs provided in the source code by edX and 2U has also been moved to the backend and given  
arguments that allow for slight customization using `citipy` and `numpy`, as well as the API calls  
used to retrieve the graphed data. The API calls are set by default for the purpose of this  
challenge but are moved to the backend and given arguments to change the queries.  

Top-Level graphing methods group multiple matplotlib.pyplot functions together so only one line  
of code must be deployed to create the graphs and display the data/results. Top-level code has  
been given default arguments for preferred outputs but allows for changes based on slightly  
different needs of different data outputs. In doing so, sensitive `pyplot` methods are being  
protected from errors while still allowing for custom outputs. almost all of the methods used  
in the Notebook could be modulated, graphical output is the least subject to changes, whereas  
if the DataFrames used are changed the output will still be correct if 'back-end' directories  
for label constructors are updated accordingly. Additional `update` methods could be added as  
well. Please be advised, this was done for practice as well as improving the usefulness of the  
notebook and cleaning up the code in general.  

The following shorthand list was used initially to help frame the reasons why this path was  
taken as opposed to re-coding it each time:
- Readability
- Easy customization
- Replication
- Protection of sensitive methods
- Separation of dependencies into another Python file:
    - Cleans/protects namespace
    - Creates specific roles --> Which code is more variable?
        - DataFrames are viable to changes
        - Pyplot objects are subject to specific designations/formatting
            - Methods can always be updated for more label corrections and formatting req,
            --> Simply add more names into the directory
        - API call can be considered non-variable but arguments for changing queries are provided

[:arrow_up: Return to TOC](#table-of-contents)  


## Files and Directory Structure  
```  
python-api-challenge/
|
|-- Vacation_WeatherPy
|   |—- output_data/
|   |   |—- cities.csv
|   |-- gcs_fx.py
|   |-- VacationPy.ipynb
|   |-- WeatherPy.ipynb
|-- .gitignore
|-- README.md
```  
This structure ensures all inputs are organized within their respective folders.  
Outputs will be created without additional directory structuring  

[:arrow_up: Return to TOC](#table-of-contents)  