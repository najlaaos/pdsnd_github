import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new York City': 'new_york_city.csv',
              'washington': 'washington.csv' }
# def  function
    pass
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
      Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Ask user specify a city (chicago, new york city, washington).
    while True:
        city = input("\nWhich city would you like to filter by?\nNew York City.\nChicago.\nWashington\n").strip().lower()
        if city not in ('new york city', 'chicago', 'washington'):
          print("Sorry, I didn't catch that. Try again.")
          continue
        else:
          break

    # Asks user to specify a month to filter on, or choose all.
    while True:
            month = input("\nWhich month would you like to filter by? \nJanuary \nFebruary \nMarch \nApril \nMay \nJune \nor type 'all' if you do not have any preference?\n").strip().lower()
            if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
              print("\nThat's invalid choice, please type a valid month name or all.")
              continue
            else:
             break


    # Asks user to specify a day of week, or choose all.
    while True:
          day = input("\nAre you looking for a specific day?\nplease choose one or all of these days: \n(Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or 'all'.)\n").strip().lower()
          if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("\nThat's invalid choice, please type a valid day name or all.")
            continue
          else:
            break

    print('-'*40)
    return city, month, day







def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df










def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    Most_common_month= df['month'].mode()[0]
    print('Most Common Month:', Most_common_month)


    # display the most common day of week
    Most_common_day= df['day_of_week'].mode()[0]
    print('Most Common day of week:', Most_common_day)


    # display the most common start hour
    df['Start_hour'] = df['Start Time'].dt.hour
    Most_com
