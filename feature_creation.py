import pandas as pd
import numpy as np
from datetime import datetime
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar

def cleanDates(df):
    """PURPOSE: Create date features
       INPUT: pandas dateframe"""

    # AUTHOR: Victoria Levchenko
    
    # NOTE:
    # NOT explicitly using 'Closed Date', 'Due Date', and 'Resolution Action Updated Date'
    # because this data is created after the time of submission
    
    # OTHER PROPOSED CHANGES:
    # Create a time of day variable to track differences between morning, afternoon, and night complaints
    
    # ALTER object types to datatime for date columns
    df['Created Date'] = pd.to_datetime(df['Created Date'])
    df['Closed Date'] = pd.to_datetime(df['Closed Date'])
    df['Due Date'] = pd.to_datetime(df['Due Date'])
    df['Resolution Action Updated Date'] = pd.to_datetime(df['Resolution Action Updated Date'])

    # CREATE sequential week feature
    week = df['Created Date'].dt.week
    year = df['Created Date'].dt.year
    df['Create Date - Year & Week'] = year.astype(str) + ' - ' + week.astype(str)
    
    # CREATE year, month, week, day of week features
    df['Created Date - Year'] = df['Created Date'].dt.year
    df['Created Date - Month'] = df['Created Date'].dt.month
    df['Created Date - Week'] = df['Created Date'].dt.week
    df['Created Date - Day of the Week'] = df['Created Date'].dt.dayofweek
    df['Created Date - Hour'] = df['Created Date'].dt.hour
    
    # CREATE weekend or weekday flag
    df['Created Date - Weekend Flag'] = np.where(df['Created Date - Day of the Week']>4, 1, 0) 
    df['Created Date - Weekday Flag'] = np.where(df['Created Date - Day of the Week']<=4, 1, 0) 
    
    # CREATE flag for holidays
    cal = calendar()
    holidays = cal.holidays(start=df['Created Date'].min(), end=df['Created Date'].max())
    df['Created Date - Holiday Flag'] = df['Created Date'].isin(holidays)
    df['Created Date - Holiday Flag'] = np.where(df['Created Date - Holiday Flag']==True, 1, 0) 
    
    # CREATE seasons categorical feature
    seasons = {1:'winter', 2:'winter', 3:'spring', 4:'spring', 5:'spring', 
               6:'summer', 7:'summer', 8:'summer', 9:'fall', 10:'fall', 11:'fall', 12:'winter'}
    df['Created Date - Seasons'] = df['Created Date - Month'].map(seasons)
    
    
    
    return df`
