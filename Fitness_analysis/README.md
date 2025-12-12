# Fitness Data Analyzer

A simple Python project that generates fitness data, saves it into a CSV file, and visualizes the data using Matplotlib.
It includes:
Steps per day
Calories burned
Hours of sleep
Correlation between sleep and steps
Three visual graphs combined into one screen

## Features
- Automated Data Generation
- The script generates random fitness data for:
- Sleep hours (5–9 hrs)
- Steps (3000–15000)
- Calories burned (1500–3000)
### Saves Data to CSV
- Automatically creates a file: fitness_data.csv
### Data Visualization
Creates 3 visualizations in one window:
1. Bar Chart: Steps per day
2. Line Chart: Calories burned
3. Scatter Plot: Sleep vs Steps
### Correlation Calculation
- Shows how strongly sleep hours relate to steps taken.

## Requirements
- Install dependencies before running: pip install numpy matplotlib

## How to Run
- Clone the repository
- Run the script: fitness_tracker.py
- A window will open showing all your graphs together.
- A CSV file will be generated containing all the fitness data.
