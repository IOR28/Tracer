# Tracker

Tracker is a Python applications that allows to log all your incomes, expenses and investments using Jupyter Notebooks.
Each month can be tracked in a single notebook and generate an interactive HTML file as a result with tables and plots.
A higher level annual notebook can be added in order to automatically execute a set of monthly notebooks of the same year 
and generate results for a complete year.

## Installation

To get the source code, clone it from GitHub:

```bash
git clone https://github.com/IOR28/Tracker

cd ./Tracker
```

### Dependencies

Tracker has been developed in Python 3.9, although the code may work in older versions.

Required packages are:

- `notebook`
- `pandas`
- `plotly`
- `notebook-as-pdf`

Use the requirements file to install these in your virtual environment:

```bash
pip3 install -r requirements.txt
```

## Usage

First, you will have to define the variables under directory `types_definition`. Set your currency format and 
add/remove/modify income, expense and investment types to your needs.

To start defining your monthly trackers you must create a folder indicating the year and copy the example notebook, 
setting its name in the process. Example:

```bash
# Create directory
mkdir 2022/

# Copy first notebook
cp X_month.ipynb 2022/1_January.ipynb
```

Run the notebook and start logging in your movements! Use the example methods to introduce data into trackers, you 
should run each cell only once in order to not duplicate information. Modify the example notebooks to your needs.

> In order for the modules to be properly imported the monthly notebooks are instructed to change working directory to 
> its parent folder. If you do not like this, you can set jupyter `--notebook-dir` everytime or add the project to PYTHONPATH.

Annual notebooks can be used from the main project directory, and they will search their monthly trackers inside the 
corresponding directories.

