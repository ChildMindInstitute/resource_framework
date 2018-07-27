#!/usr/bin/env python
__author__ = "Jake Son"

import numpy as np
import pandas as pd
from pprint import pprint

# Create dataframe from simulated data

def create_simulated_df(n_samp=250):
    
    # TODO Include contact information
    # TODO Include areas of expertise (for presenters)

    options = {
        'date': ['NA', '2018_06', '2018_04', '2017_12', '2017_07','2017_04',
                 '2015_01', '2014_05', '2013_09', '2011_04'],
        'people': ['NA', 'septimus_batya', 'alexander_lindsay',
                       'gregory_camille', 'camacho_nicolas', 'kramer_eliza',
                       'franco_alex', 'xu_ting', 'koo_bonhwang', 'klein_arno'],
        'topics': ['NA', 'neuroscience', 'machine_learning', 'psychology', 'coding',
                   'grad_school', 'psychopharm', 'data_science', 'medicine'],
        'category': ['NA', 'research', 'presentation', 'resource', 'cmi_staff'],
        'status': ['NA', 'poster', 'in_progress', 'proceeding', 'publication'],
        'datatypes': ['NA', 'fmri', 'behavioral', 'eye_tracking', 'eeg', 'audio',
                     'actigraphy', 'genetic'],
        'database': ['NA', 'fcp', 'adhd200', 'hbn', 'nki'],
        'difficulty': ['NA', 'beginner', 'intermediate', 'advanced']
    }

    sim_dict = {'date': [],
                'people': [],
                'topics': [],
                'category': [],
                'status': [],
                'datatypes': [],
                'database': [],
                'difficulty': []
                }

    for i in range(n_samp):

        for key in sim_dict.keys():

            n_rand = np.random.randint(len(options[key]))

            sim_dict[key].append(options[key][n_rand])

    df = pd.DataFrame.from_dict(sim_dict).set_index('date').sort_values('date')

    return df

    
def search_topic(df):
    
    need_topic = True
    
    print("Here's a list of topics:")
    pprint(list(df.topics.unique()))
    
    while need_topic:
    
        u_args = input('What topic are you interested in?: ')

        if u_args in list(df.topics.unique()):

            filtered_df = df[df['topics'].str.contains(u_args)]
            need_topic = False

        else:

            print('Your search term was not found - here are your options: ')
            pprint(list(df.topics.unique()))
    
    print('\nDataframe updated.')
    
    return u_args, filtered_df
    
    
def search_category(df):
    
    need_category = True
    
    print("Here's a list of categories:")
    pprint(list(df.category.unique()))
    
    while need_category:
    
        u_args = input('What categories are you interested in?: ')

        if u_args in list(df.category.unique()):

            filtered_df = df[df['category'].str.contains(u_args)]
            need_category = False

        else:

            print('Your search term was not found - here are your options: ')
            pprint(list(df.category.unique()))
    
    print('\nDataframe updated.')
    
    return u_args, filtered_df


def search_status(df):
    
    need_status = True
    
    print("Here's a list of research states:")
    pprint(list(df.status.unique()))
    
    while need_status:
    
        u_args = input('What research status are you interested in?: ')

        if u_args in list(df.status.unique()):

            filtered_df = df[df['status'].str.contains(u_args)]
            need_status = False

        else:

            print('Your search term was not found - here are your options: ')
            pprint(list(df.status.unique()))
    
    print('\nDataframe updated.')
    
    return u_args, filtered_df
    
def search_datatype(df):
    
    need_datatype = True
    
    print("Here's a list of datatypes:")
    pprint(list(df.datatypes.unique()))
    
    while need_datatype:
    
        u_args = input('What datatypes are you interested in?: ')

        if u_args in list(df.datatypes.unique()):

            filtered_df = df[df['datatypes'].str.contains(u_args)]
            need_datatype = False

        else:

            print('Your search term was not found - here are your options: ')
            pprint(list(df.datatypes.unique()))
    
    print('\nDataframe updated.')
    
    return u_args, filtered_df
    
    
def search_database(df):
    
    need_database = True
    
    print("Here's a list of databases")
    pprint(list(df.database.unique()))
    
    while need_database:
    
        u_args = input('What datatypes are you interested in?: ')

        if u_args in list(df.database.unique()):

            filtered_df = df[df['database'].str.contains(u_args)]
            need_database = False

        else:

            print('Your search term was not found - here are your options: ')
            pprint(list(df.database.unique()))
    
    print('\nDataframe updated.')
    
    return u_args, filtered_df


def search_difficulty(df):
    
    need_difficulty = True
    
    print("Here's a list of difficulties")
    pprint(list(df.difficulty.unique()))
    
    while need_difficulty:
    
        u_args = input('What datatypes are you interested in?: ')

        if u_args in list(df.difficulty.unique()):

            filtered_df = df[df['difficulty'].str.contains(u_args)]
            need_difficulty = False

        else:

            print('Your search term was not found - here are your options: ')
            pprint(list(df.difficulty.unique()))
    
    print('\nDataframe updated.')
    
    return u_args, filtered_df


def search_multiple(df, topics=False, category=False, status=False, datatypes=False, database=False,
                    difficulty=False):
    
    filters = []
    updated = False
    
    if topics:
        
        if updated:
        
            topic_args, up_df = search_topic(up_df)
            filters.append(topic_args)
        
        else:
            
            topic_args, up_df = search_topic(df)
            filters.append(topic_args)
            updated = True
        
    if category:
        
        if updated:
        
            category_args, up_df = search_category(up_df)
            filters.append(category_args)
            
        else:
            
            category_args, up_df = search_category(df)
            filters.append(category_args)
            updated = True
        
    if status:
        
        if updated:
        
            status_args, up_df = search_status(up_df)
            filters.append(status_args)

        else:
            
            status_args, up_df = search_status(df)
            filters.append(status_args)
            updated = True
       
    if datatypes:
        
        if updated:
        
            datatypes_args, up_df = search_datatype(up_df)
            filters.append(datatypes_args)
            
        else:
            
            datatypes_args, up_df = search_datatype(df)
            filters.append(datatypes_args)
            updated = True

    if database:
        
        if updated:
        
            database_args, up_df = search_database(up_df)
            filters.append(database_args)
            
        else:
            
            database_args, up_df = search_database(df)
            filters.append(database_args)
            updated = True
    
    if difficulty:
        
        if updated:
        
            difficulty_args, up_df = search_difficulty(up_df)
            filters.append(difficulty_args)
            
        else:
            
            difficulty_args, up_df = search_difficulty(df)
            filters.append(difficulty_args)
            updated = True

    return filters, up_df
    
    
    
    
    
