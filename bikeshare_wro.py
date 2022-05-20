import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Set up month selection options
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

# Set up day of the week selection options
DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_key = ''
    while city_key.lower() not in CITY_DATA:
        city_key = input('\nWhat is the city name to analyze? (Chicago, New York City, or Washington)\n')
        # Set up logic to find if city is in CITY_DATA.
        if city_key.lower() in CITY_DATA:
            city = CITY_DATA[city_key.lower()]
        else:
            print('\n>> City is invalid. Please re-enter the name of a city to analyze. (Chicago, New York City, or Washington)')

    # TO DO: get user input for month (all, january, february, ... , june)
    month_key = ''
    while month_key.lower() not in MONTH_DATA:
        month_key = input('\nWhat is the month name to analyze? (January thru June, or all)\n')
        # Set up logic to find if month is in MONTH_DATA.
        if month_key.lower() in MONTH_DATA:
            month = month_key.lower()
        else:
            print('\n>> Month is invalid. Please re-enter a month to analyze. (January thru June, or all)')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_key = ''
    while day_key.lower() not in DAY_DATA:
        day_key = input('\nWhat is the day of the week to analyze? (Sunday thru Saturday, or all)\n')
        # Set up logic to find if day of the week is in DAY_DATA.
        if day_key.lower() in DAY_DATA:
            day = day_key.lower()
        else:
            print('\n>> Day is invalid. Please re-enter a day to analyze. (Sunday thru Saturday, or all)')

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
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Set up logic to pull month, day of week and hour from Start Time column.
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # Set up logic to read month in MONTH_DATA dataset.
    if month != 'all':
        month = MONTH_DATA.index(month)
        df = df[df['month'] == month]

    # Set up logic to read day of the week in DAY_DATA dataset.
    if day != 'all':
        df = df[df['day of week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f'\nThe most common month for selections is:\t {MONTH_DATA[common_month].title()}')

    # TO DO: display the most common day of week
    common_day = df['day of week'].mode()[0]
    print(f'\nThe most common day of the week for selections is:\t {common_day}')

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print(f'\nThe most common start hour for selections is:\t {common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'\nThe most common start station for selections is:\t {common_start_station}')

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f'\nThe most common end station for selections is:\t {common_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    common_combination = ('1. ' + df['Start Station'] + ', and 2.' + df['End Station']).mode()[0]
    print(f'\nThe most frequest station combination for selections is:\t {common_combination}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time in days
    tot_travel_time = (df['Trip Duration'].sum())/(24*60*60)
    print(f'The total travel time for selections is:\t {tot_travel_time} days')

    # TO DO: display mean travel time
    avg_travel_time = (df['Trip Duration'].mean())/60
    print(f'The mean travel time for selections is:\t {avg_travel_time} minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# Assistance noted - mentor reminded me that I needed to include 'city' in def user_stats(df, city)
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f'The user type count for selections is:\n {user_type}')

    # TO DO: Display counts of gender
    # Set up logic to find gender and birth info in chicago and new york city files.
    # Gender and birth data no available for Washington
    if city != 'washington':
        gender_type = df['Gender'].value_counts()
        print(f'The gender count for selections is:\n {gender_type}')

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        latest_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print(f'The earliest birth year for selections is:\t {earliest_birth}')
        print(f'The most recent birth year for selections is:\t {latest_birth}')
        print(f'The most common birth year for selections is:\t {common_birth}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# Set up logic to return more rows of data.
def header(df):
    print(df.head())
    more = 0
    while True:
        see_data = input('n\Do you want to see more data (yes/no)?\n')
        if see_data.lower() != 'yes':
            return
        more = more + 5
        print(df.iloc[more:more+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        # Assistance noted - mentor reminded me that I needed to include 'city' in def user_stats(df, city)
        user_stats(df, city)
        header(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
