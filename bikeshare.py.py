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
        city = input('Would you like to see data for Chicago, New York City or Washington?: ').lower()
        if city in (CITY_DATA):
            print('\nIt seems you want to see: {}\n'.format(city))
            print('If not, please restart the program [press ctrl+c]')
            break
        else:
            print('\nInvalid answer. Please try again: ')
            continue
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = input('Which month would you like to analyze? january, february, march, april, may, june, or all: ').lower()
        if month in months:
            print('\nIt seems you want to see: {}\n'.format(month))
            print('If not, please restart the program [press ctrl+c]')
            break
        else:
            print('\nInvalid answer. Please try again: ')
            continue
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
        day = input('What day of the week would you like to filter by? Enter: monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all: ').lower()
        if day in days:
            print('\nIt seems you want to see: {}\n'.format(day))
            print('If not, please restart the program [press ctrl+c]')
            break
        else:
            print('\nInvalid answer. Please try again: ')
            continue
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
    if day.lower() != 'all':
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df
   
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    months_2 = ['all', 'January', 'February', 'March', 'April', 'May', 'June']
    print('The most common month is: ', months_2[common_month])
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is: ', common_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour to start to travel is ', common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', common_start_station)
    
    # TO DO: display most commonly used end station
    common_used_end_station= df['End Station'].mode().values[0]
    print("The most commonly used end station is: {} ".format(common_used_end_station))
    
    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    most_combination= df['combination'].mode().values[0]
    print("The most frequent combination of start station and end station trip is: {} ".format(most_combination ))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
   # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: {}'.format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print('The mean travel time is: {}'.format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df,city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
   # TO DO: Display counts of user types
    print("The counts of user types are:")
    user_types = df['User Type'].value_counts()
    print(user_types)
    if city in ('chicago', 'new york city'):
        # TO DO: Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('The gender count is: ', gender_count)
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest= df['Birth Year'].min()
        print('The earliest birth year: {}.\n'.format(earliest))
        recent= df['Birth Year'].max()
        print('The latest birth year: {}.\n'.format(recent))
        most_common_year= df['Birth Year'].mode()[0]
        print('The most common birth year: {}.\n'.format(most_common_year))
    else:
        pa=0
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
  
   while True:
        view_input_five = input('\nWould you like to see next 5 rows of data? Please enter yes or no:').lower()
        if view_input_five in ('yes', 'y'):
            n = 0     
            print(df.iloc[n:n+5])
            n += 5
        elif view_input_five == 'no':    
            break
        else:
            print('\nInvalid answer. Please enter yes or no: ')
            continue
            
    
                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()          
        if restart.lower() != 'yes':
            break  


if __name__ == "__main__":
    main()