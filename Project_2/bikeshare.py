import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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



    while True:
      city = input("\nPlease Enter the City Which you would like to analyze ? \nChicago, \nNew York City or \nWashington?\n")
      if city in ('Chicago', 'New York City', 'Washington'):
        print("Something got wrong. \nCould you please enter again ?\n")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
      month = input("\nPlease enter the month Which you would like to analyze? \nJanuary, February, March, April, May, June or \nif you don't decide just type 'all'?\n")
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print("Something got wrong. \nCould you please enter again ?\n")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("\nPlease enter the day Which you would like to analyze? \nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or \nif you don't decide just type 'all'?\n")
      if day not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'all'):
        print("Something got wrong. \nCould you please enter again ?\n")
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
    # convert the Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the neyesw dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating Statistics of The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
def most_common_month(df):
    df['month'] = df['Start Time'].dt.month_name()
    most_popular_month=df['month'].mode()[0]
    print('Most Popular Month of Year:',most_popular_month)

    # TO DO: display the most common day of week

def most_common_day(df):
    df['day'] = df['Start Time'].dt.day_name()
    most_popular_day=df['day'].mode()[0]
    print('Most Popular Day of Week:',most_popular_day)

    # TO DO: display the most common start hour

def most_common_hour(df):
    df['hour'] = df['Start Time'].dt.hour
    most_popular_hour=df['hour'].mode()[0]
    print('Most Popular Start Hour:',most_popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station=df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:',common_start_station)

    # TO DO: display most commonly used end station

    common_end_station=df['End Station'].mode()[0]
    print('Most Commonly Used End Station:',common_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    df['Start End Station'] = df['Start Station'].map(str) + '&' + df['End Station']
    frequent_start_end = df['Start End Station'].value_counts().idxmax()
    print('Most frequent combination of start station and end station of trip: ',frequent_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Convert seconds to readable time format
    def readable_time_sec(seconds):
        m, s = divmod(seconds,60)
        h, m = divmod(m,60)
        d, h = divmod(h,24)
        y, d = divmod(d,365)
        print('Years: {}, Days: {}, Hours: {}, Mins: {}, Secs: {}'.format(y,d,h,m,s))

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:\n')
    readable_time_sec(total_travel_time)

    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time: {} seconds'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    count_user_types = df['User Type'].value_counts()
    print('Total counts of user types : {}.'.format(count_user_types))

    # TO DO: Display counts of gender

    try:
      count_gender_types = df['Gender'].value_counts()
      print('\nTotal counts of gender types are :', count_gender_types)
    except KeyError:
      print("\nTotal counts of gender types are:\nData unavailable for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest_birth_year = df['Birth Year'].min()
      print('\nThe earliest year of birth:', earliest_birth_year)
    except KeyError:
      print("\nThe earliest year of birth:\nData unavailable for this month.")

    try:
      recent_birth_year = df['Birth Year'].max()
      print('\nMost recent year of birth:', recent_birth_year)
    except KeyError:
      print("\nMost recent year of birth:\nData unavailable for this month.")

    try:
      common_birth_year = int(df['Birth Year'].mode()[0])
      print('\nMost common year of birth:', common_birth_year)
    except KeyError:
      print("\nMost common year of birth:\nData unavailable for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # TO DO: Display rawdata if the user wants to see

def raw_data(df):
    user_choice = input('\nWould you like to see the raw data? \nPlease enter yes or no.\n If yes, It will be shown 5 lines of raw data.\n')
    line_cnt = 0

    while True:
        if user_choice.lower() != 'no':
            print(df.iloc[line_cnt : line_cnt + 5])
            line_cnt += 5
            user_choice = input('\nWould you like to see more raw data? \nPlease enter yes or no.\n')
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
