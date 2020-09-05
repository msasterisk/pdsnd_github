import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    This function asks the user to specify a city, month, and day to analyze.

    It returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = ''
    filter_choice = ''
    month = ''
    day = ''

    while city != 'chicago' and city != 'new york' and city != 'washington':
        city = input('\nWould you like to see data for Chicago, New York, or Washington?\n')
        city = city.lower()
        if city != 'chicago' and city != 'new york' and city != 'washington':
            print('\nInvalid choice!\n')

    while filter_choice != 'month' and filter_choice != 'day' and filter_choice != 'none':
        filter_choice = input('\nWould you like to filter the data by month, day, or not at all? Enter month, day or none\n')

    # get user input for month (all, january, february, ... , june)

    if filter_choice == 'month':
        while month != '1' and month != '2' and month != '3' and month != '4' and month != '5' and month != '6' and month != 'all':
            month = input('\nWhich month would you like to see data for? Enter 1 for January, 2 for February, 3 for March, 4 for April, 5 for May, 6 for June, or all\n')
        day = 'all'
        if month != 'all':
            month = int(month)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    if filter_choice == 'day':
        while day != '0' and day != '1' and day != '2' and day != '3' and day != '4' and day != '5' and day != '6' and day != 'all':
            day = input('\nWhich day would you like to see data for? Enter 0 for Monday, 1 for Tuesday, 2 for Wednesday, 3 for Thursday, 4 for Friday, 5 for Saturday, 6 for Sunday, or all\n')
        month = 'all'
        if day != 'all':
            day = int(day)

    if filter_choice == 'none':
        month = 'all'
        day = 'all'


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    This function loads data for the specified city and filters by month and day if applicable.

    It uses the following arguments:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    It returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    """
        ,Start Time,End Time,Trip Duration,Start Station,End Station,User Type,Gender,Birth Year
        1423854,2017-06-23 15:09:32,2017-06-23 15:14:53,321,Wood St & Hubbard St,Damen Ave & Chicago Ave,Subscriber,Male,1992.0
    """

    if city == 'chicago':
        df = pd.read_csv("chicago.csv", index_col=0, parse_dates=['Start Time','End Time'])


    if city == 'new york':
        df = pd.read_csv("new_york_city.csv", index_col=0, parse_dates=['Start Time','End Time'])

    if city == 'washington':
        df = pd.read_csv("washington.csv", index_col=0, parse_dates=['Start Time','End Time'])

    # create a new column that contains the start month using Pandas DatetimeIndex function
    df['Start Month']=pd.DatetimeIndex(df['Start Time']).month

    # create a new column that contains the start weekday using Pandas DatetimeIndex function
    df['Start Weekday']=pd.DatetimeIndex(df['Start Time']).weekday

    # create a new column that contains the start hour using Pandas DatetimeIndex function
    df['Start Hour']=pd.DatetimeIndex(df['Start Time']).hour





    # remove rows that do not match the month filter criteria
    if month != 'all':
        df=df[df['Start Month'] == month].head()

    # remove rows that do not match the weekday filter criteria
    if day != 'all':
        df=df[df['Start Weekday'] == day].head()


    print(df.head())


    """
    with open ("chicago.csv") as f:
        for line in f:
            if line.find(',Start Time,End Time,Trip Duration,'):
                continue
            first_val,start_time, end_time, trip_duration, start_station, end_station, user_type, gender, birth_year = line.split(',')
    """

    return df


def time_stats(df):
    """This function displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_start_month=df['Start Month'].mode()[0]
    print('The most common start month is:', most_common_start_month)

    # display the most common day of week
    most_common_start_weekday=df['Start Weekday'].mode()[0]
    print('The most common start weekday is:', most_common_start_weekday)

    # display the most common start hour
    most_common_start_hour=df['Start Hour'].mode()[0]
    print('The most common start hour is:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """This function displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print('The most common start station is:', most_common_start_station)

    # display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print('The most common end station is:', most_common_end_station)

    # display most frequent combination of start station and end station trip
    df['Start Station to End Station']=df['Start Station']+' ---> '+ df['End Station']
    most_common_trip=df['Start Station to End Station'].mode()[0]
    print('The most common trip is:', most_common_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """This function displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('The total travel time is:', total_travel_time, 'seconds')


    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('The mean travel time is:', mean_travel_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """This function displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types=df['User Type'].value_counts()
    print('Counts of user types:\n'+ str(user_types))
    print('\n')

    # Display counts of gender
    if 'Gender' in df.columns:
        gender=df['Gender'].value_counts()
        print('Counts of gender:\n'+ str(gender))
        print('\n')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year=df['Birth Year'].min()
        print('The earliest birth year is:', earliest_birth_year)

        latest_birth_year=df['Birth Year'].max()
        print('The most recent birth year is:', latest_birth_year)

        most_common_birth_year=df['Birth Year'].mode()[0]
        print('The most common birth year is:', most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea','yeah','you got it','of course','sure','sure thing','you bet','does the bear live in the woods?'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display another 5 rows of raw data? ').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
