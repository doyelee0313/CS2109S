import os

import pandas as pd
import numpy as np

COUNTRIES_W_MOST_CASES = ['United States', 'India', 'Brazil']

def get_data() -> pd.DataFrame:
    '''
    Returns national-level data that is sorted by country name and date such that
    the next row (if any) in the `DataFrame` is the entry of the same country but
    for the next day, if such an entry exists.
    '''

    dirname = os.path.dirname(__file__)
    data_file_path = os.path.join(dirname, 'OxCGRT_2020.csv')
    df = pd.read_csv(data_file_path, dtype={'CountryName': str,\
        'CountryCode': str, 'RegionName': str, 'RegionCode': str,\
        'Jurisdiction': str, 'Date': np.float64, 'C1_School closing': np.float64,\
        'C2_Workplace closing': np.float64, 'C6_Stay at home requirements': np.float64,\
        'C8_International travel controls': np.float64,\
        'H4_Emergency investment in healthcare': np.float64,\
        'ConfirmedCases': np.float64, 'ConfirmedDeaths': np.float64})
    
    df_national = df[df['Jurisdiction'] == 'NAT_TOTAL']
    df_national = df_national.sort_values(by=['CountryName', 'Date'])

    return df_national

def get_n_cases_cumulative(df: pd.DataFrame) -> np.ndarray:
    '''
    Returns the number of cumulative confirmed cases as an `ndarray`.
    
    In particular, each row represents a country while the columns of the row
    represent the time series data of that country.
    '''
    return _convert_num_series_to_numpy(df, 'ConfirmedCases')

def get_n_deaths_cumulative(df: pd.DataFrame) -> np.ndarray:
    '''
    Returns the number of cumulative confirmed deaths as an `ndarray`.
    
    In particular, each row represents a country while the columns of the row
    represent the time series data of that country.
    '''
    return _convert_num_series_to_numpy(df, 'ConfirmedDeaths')

def get_n_cases_top_cumulative(df: pd.DataFrame) -> np.ndarray:
    '''
    Returns the number of cumulative confirmed cases as an `ndarray` for the
    countries with the most number of confirmed cases.
    
    In particular, each row represents a country while the columns of the row
    represent the time series data of that country.
    '''
    df_most_cases = df[df['CountryName'].isin(COUNTRIES_W_MOST_CASES)]
    return _convert_num_series_to_numpy(df_most_cases, 'ConfirmedCases')

def get_healthcare_spending(df: pd.DataFrame) -> np.ndarray:
    '''
    Returns governments' healthcare spending as an `ndarray`.
    
    In particular, each row represents a country while the columns of the row
    represent the time series data of that country.
    '''
    return _convert_num_series_to_numpy(df, 'H4_Emergency investment in healthcare')

def get_stringency_values(df: pd.DataFrame) -> np.ndarray:
    '''
    Returns stringency values for each country as an `ndarray`.
    
    Specifically, each row represents a country while the columns of the row
    represent the time series data of that country. In this case, the last axis
    contains 4 elements representing the stringency values for C1_School closing,
    C2_Workplace closing, C6_Stay at home requirements and C8_International
    travel controls, respectively.
    '''
    school_closing = _convert_num_series_to_numpy(df,\
        'C1_School closing')
    workplace_closing = _convert_num_series_to_numpy(df,\
        'C2_Workplace closing')
    stay_home = _convert_num_series_to_numpy(df,\
        'C6_Stay at home requirements')
    travel_controls = _convert_num_series_to_numpy(df,\
        'C8_International travel controls')
    
    n_countries = _get_n_countries(df)
    stringency_values = np.zeros((n_countries, school_closing.shape[1], 4))
    stringency_values[:, :, 0] = school_closing
    stringency_values[:, :, 1] = workplace_closing
    stringency_values[:, :, 2] = stay_home
    stringency_values[:, :, 3] = travel_controls

    return stringency_values

def get_mask_prices(n_prices: int) -> np.ndarray:
    '''
    Returns an `ndarray` of mask prices such that there are `n_prices` prices.
    Specifically, this `ndarray` is of shape `(n_prices,)`.
    '''
    rng = np.random.default_rng(2109)
    return rng.uniform(1, 5, n_prices) * 4

def _get_n_countries(df: pd.DataFrame) -> int:
    '''
    Returns the number of unique countries that are represented in `df`.
    '''
    return pd.unique(df['CountryName']).size

def _convert_num_series_to_numpy(df: pd.DataFrame, col_label: str) -> np.ndarray:
    '''
    Gets the numerical `Series` from `df` with `col_label`, and returns an `ndarray`
    such that each row represents a country while the columns of the row represent
    the time series data of that country.

    NOTE: this assumes that the data in `df` is arranged such that entries from
    the same country but of different dates are adjacent to each other. 
    '''
    n_countries = _get_n_countries(df)
    return np.nan_to_num(df[col_label].to_numpy()).reshape(n_countries, -1)
