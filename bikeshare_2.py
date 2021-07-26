import time
import pandas as pd
import numpy as np
# numpy has not been used.
# all of the user input and calculated data will be printed to show the user his inputs and results.
# all user input will be converted into lower for standardization.  
# all the data output will be displayed in a good looking format for a better readability.

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # cities from dict are printed to show options for the user.          
    print('You can analyze the following city\'s:')
    for k1,v1 in CITY_DATA.items():
        print('   {}'.format(k1))
        
    # pre-define city as an empty string for the upcoming while loop.    
    city = str( )
    
    # while-loop to ask for the users choice of city from the list.
    # if the user input does not fit the citylist he will get a notification and has to repeat his input.      
    while True:
        city = input('Please select a city from the list to analyze: ').lower()
        if city not in CITY_DATA.keys():
            print('\nInvalid input. Your answer is not in the list.\n')
            continue
        else:
            break
       
                          
    # creating a list for months and days including all.
    # pre-define month and day as an empty string for the upcoming while loop.
    # if the user input does not fit the month and day data he will get a notification and has to repeat his input.
    MONTH_DATA = ['all','january','february','march','april','may','june']
    DAY_DATA = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    month = str()
    day = str()
    
    # get user input for month (all, january, february, ... , june)
    # months are printed to show options for the user including 'all'.
    while month not in MONTH_DATA:
        print('\nYou can filter the data by month. You can select a filter from the following list: ')
        for k2 in MONTH_DATA:
                print('   {}'.format(k2))        
        month = input('Please select a filter from the list: ').lower()
        if month not in MONTH_DATA:
            print('\nInvalid input. Your answer is not in the list.\n')
        else:
            break
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    # days are printed to show options for the user including 'all'.
    while day not in DAY_DATA:
        print('\nYou can filter the data by day of week. You can select a filter from the following list: ')
        for k3 in DAY_DATA:
                print('   {}'.format(k3))        
        day = input('Please select a filter from the list: ').lower()
        if day not in DAY_DATA:
            print('\nInvalid input. Your answer is not in the list.\n')
        else:
            break
    
    # print the selected filters for confirmation to the user.
    print('You selected: ')
    print('   '+city)
    print('   '+month)
    print('   '+day)
    
    
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
    # load csv data for the selected city by user.
    df = pd.read_csv(CITY_DATA[city])

    # create columns for start time, month and day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.day_name()

    # if filtered by month
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # if filtered by day
    if day != 'all':
        df = df[df['day of week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    common_month = df['month'].mode()[0]
    print('\nMost common month as number:')
    print(common_month)

    # display the most common day of week
    common_day_of_week = df['day of week'].mode()[0]
    print('\nMost common day of week:')
    print(common_day_of_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('\nMost common start hour:')
    print(common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('\nMost common start station:')
    print(common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('\nMost common end station:')
    print(common_end)

    # display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + ' - ' + df['End Station']
    combination = df['Combination'].mode()[0]
    print('\nMost frequent combination of start and end station:')
    print(combination)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal travel time:')
    print(total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean travel time:')
    print(mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # displayed by Subscriber or Customer
    user_types = df['User Type'].value_counts()
    print('\n',user_types)

    # Display counts of gender
    # displayed by Male or Female
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('\n',gender)
    else:
        print('\nNo information about gender.')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        print('\nEarliest year of birth:')
        print(earliest)
        recent = df['Birth Year'].max()
        print('\nRecent year of birth:')
        print(recent)
        common_birth_year = df['Birth Year'].mode()[0]
        print('\nMost common year of birth:')
        print(common_birth_year)
        
    else:
        print('\nNo information about birth year.')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """
    Asks user if he would like to display 5 rows of raw data from his filters.
    User has the option to display more raw data or continue.
    """
    # pre-define answer options, raw_data1 and a counter for upcoming while loop.
    # creating a list for months and days including all.
    # pre-define month and day as an empty string for the upcoming while loop.
    # if the user input does not fit the month and day data he will get a notification and has to repeat his input.
    OPTIONS = ['yes','no']
    raw_data1 = str()
    row_count = 0
    
    # while loops to check if the user wants to display raw data and if he wants to repeat that.
    while raw_data1 not in OPTIONS:
        raw_data1 = input('\nWould you like to display 5 rows of the raw data?  yes / no :\n').lower()
        if raw_data1 == 'yes':
            print(df.head())
        elif raw_data1 not in OPTIONS:
            print('\nInvalid input.\n')
              
     
    while raw_data1 == 'yes':
        raw_data2 = input('Would you like to display 5 more rows of raw data?  yes / no :\n').lower()
        row_count += 5
        if raw_data2 == 'yes':
            print(df[row_count:row_count+5])
        elif raw_data2 == 'no':
            break
        elif raw_data2 not in OPTIONS:
            print('\nInvalid input.\n')
    

    print('-'*40)
        

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
