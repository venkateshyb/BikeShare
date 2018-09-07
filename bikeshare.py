## TODO: import all necessary packages and functions

import time
import pandas as pd
import numpy as np
## Filenames

chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city=' '
    while (city.lower()!='chicago') and (city.lower()!='new york') and (city.lower()!='washington'):
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or Washington?\n')
        if ((city.lower()=='chicago') or (city.lower()=='new york') or (city.lower()=='washington')):
            return city


    # TODO: handle raw input and complete function


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) Time period for filtering of data based on month, day or none
    '''
    time_period=' '
    while (time_period.lower()!='month') and (time_period.lower()!='day') and (time_period.lower()!='none'):
        time_period = input('\nWould you like to filter the data by month, day, or not at'
                            ' all? Type "none" for no time filter.\n')
        if ((time_period.lower()=='month') or (time_period.lower()=='day') or (time_period.lower()=='none')):
            return time_period




def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        (int) Month position based on the user input
    '''
    month=' '
    while (month.lower()!='january') and (month.lower()!='february') and (month.lower()!='march') and (month.lower()!='april') and (month.lower()!='may') and (month.lower()!='june'):
            month = input('\nWhich month? January, February, March, April, May, or June?\n')
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            if (month.lower()=='january') or (month.lower()=='february') or (month.lower()=='march') or (month.lower()=='april') or (month.lower()=='may') or (month.lower()=='june'):
                month = months.index(month.lower())+1
                return month


        # use the index of the months list to get the corresponding int
def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        (str) day of the week based on user input
    '''
    day=' '
    while (day.lower()!='monday') and (day.lower()!='tuesday') and (day.lower()!='wednesday') and (day.lower()!='thursday') and (day.lower()!='friday') and (day.lower()!='saturday') and (day.lower()!='sunday'):
        day = input('\nWhich day? Please type your response as words. Enter (Monday,Tuesday,Wednesday etc.)\n')
        if (day.lower()=='monday') or (day.lower()=='tuesday') or (day.lower()=='wednesday') or (day.lower()=='thursday') or (day.lower()=='friday') or (day.lower()=='saturday') or (day.lower()=='sunday'):
            return day
    # TODO: handle raw input and complete function



def popular_month(city_file):
    '''
    Question: What month occurs most often in the start time?
    Args:
        contains month table.
    Returns:
        no returns
    '''
    # TODO: complete function
    list1=['Jan','Feb','Mar','Apr','May','Jun']
    pop_month=city_file.value_counts().idxmax()
    print('The most popular month in Start time is {}'.format(list1[pop_month-1]))
    print('\n')
    #print(city_file.value_counts.idxmax())


def popular_day(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What day of the week (Monday, Tuesday, etc.) occurs most often in the start time?
    finds most popular day of the week
    Args:
        contains weekday table.
    Returns:
        no returns
    '''
    # TODO: complete function
    pop_day=city_file.value_counts().idxmax()
    print('The most popular day is ',pop_day)
    print('\n')


def popular_hour(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What hour of the day (0, 2, ... 22, 23) occurs most often in the start time?
    finds most popular hour
    Args:
        contains hour table.
    Returns:
        no returns
    '''
    # TODO: complete function
    pop_hour=city_file.value_counts().idxmax()
    print('The most popular hour is ',pop_hour)
    print('\n')


def trip_duration(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    Args:
        contains trip duration table.
    Returns:
        no returns
    '''
    # TODO: complete function
    print ('The total trip duration is ',city_file.sum())
    print ('The avg trip duration is',city_file.mean())
    print('\n')


def popular_stations(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most frequently used start station and most frequently
    used end station?
    Args:
        contains both Start and End Station table.
    Returns:
        no returns
    '''
    # TODO: complete function


    stations1=city_file['Start Station'].value_counts().idxmax()
    stations2=city_file['End Station'].value_counts().idxmax()
    print("Polular Start Station",stations1)
    print("Polular End Station",stations2)
    print('\n')




def popular_trip(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most common trip (i.e., the combination of start station and
    end station that occurs the most often)?
        Args:
            contains both Start and End Station table.
        Returns:
            no returns
    '''
    # TODO: complete function
    trip=city_file.groupby(['Start Station','End Station']).size().nlargest(1)
    print(trip)
    print('\n')


def users(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    Args:
        contains full table filtered based on users decision.
    Returns:
        no returns
    '''
    print("The Total number of users")
    print(city_file['User Type'].value_counts())
    print('\n')
    # TODO: complete function


def gender(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    Args:
        contains full table filtered based on users decision.
    Returns:
        no returns

    '''
    # TODO: complete function

    print("The counts of gender is")
    print(city_file['Gender'].value_counts())
    print('\n')


def birth_years(city_file):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the earliest birth year (when the oldest person was born),
    most recent birth year, and most common birth year?
    Args:
        contains full table filtered based on users decision.
    Returns:
        no returns
    '''
    print("The most recent birth year is {}".format(city_file['Birth Year'].min()))
    print("The most oldest birth year is {}".format(city_file['Birth Year'].max()))
    print("The most common birth year is {}".format(city_file['Birth Year'].value_counts().idxmax()))
    print('\n')
    # TODO: complete function


def display_data(city_file,n=0):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        contains full table filtered based on users decision and (int) n.
    Returns:
        no returns
    '''

    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    if display.lower()=='yes':

        for i in range(n,n+5):
            print(city_file.iloc[i])
            print(" \n")
        display_data(city_file,n+5)






    # TODO: handle raw input and complete function


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city2 = get_city()
    if city2.title()=='Chicago':
        city=pd.read_csv(chicago)
    elif city2.title()=='Washington':
        city= pd.read_csv(washington)
    elif city2.title()=='New York':
        city=pd.read_csv(new_york_city)

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('Calculating the first statistic...')

    city['Start Time']=pd.to_datetime(city['Start Time'])
    city['month']=city['Start Time'].dt.month
    city['day_of_week']=city['Start Time'].dt.weekday_name
    city['hour']=city['Start Time'].dt.hour
    #stations=city[['Start Station','End Station']]
    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()

        #TODO: call popular_month function and print the results
        popular_month(city['month'])

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'month':
        start_time = time.time()

        # TODO: call popular_day function and print the results
        month=get_month()
        city=city[(city.month==month)]

        popular_day(city['day_of_week'])

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    if time_period == 'day':
        start_time = time.time()

        # TODO: call popular_day function and print the results
        day=get_day()
        city=city[(city.day_of_week==day.title())]

        popular_month(city['month'])

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    popular_hour(city['hour'])


    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    trip_duration(city['Trip Duration'])


    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    popular_stations(city[['Start Station','End Station']])

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    popular_trip(city[['Start Station','End Station']])

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()


    # What are the counts of each user type?
    # TODO: call users function and print the results
    users(city)

    print("That took %s seconds." % (time.time() - start_time))
    if(city2.title()!='Washington'):
        print("Calculating the next statistic...")
        start_time = time.time()


        # What are the counts of gender?
        # TODO: call gender function and print the results
        gender(city)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
        # most popular birth years?
        # TODO: call birth_years function and print the results
        birth_years(city)

        print("That took %s seconds." % (time.time() - start_time))

        # Display five lines of data at a time if user specifies that they would like to
    display_data(city)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
