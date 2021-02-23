from collection_functions import *
from atla_collection import *
import csv

headers = ['season', 'episode_number_in_season', 'episode_number_overall', 'title', 'writers', 'directors', 'animation_studio', 'release_date', 'ratings', 'total_votes_on_ratings']

with open('csv_files/atla_basic_info.csv', 'w') as csv_file: #Create a csv file that shows season, title, writers, directors, animation studio, release date, ratings, and total votes on those ratings
    file_writer = csv.writer(csv_file)
    file_writer.writerow(headers)
    for i in range(0, len(atla_episode_titles)):
        file_writer.writerow([atla_seasons[i], atla_episode_number_season[i], atla_episode_number_overall[i], atla_episode_titles[i], atla_writers[i], atla_directors[i], atla_animation_studios[i], atla_release_dates[i], atla_ratings[i], atla_total_votes[i]])
    csv_file.close()

headers_2 = ['season', 'episode_number_in_season', 'episode_number_overall', 'title', '']

'''
with open('csv_files/atla_script_info.csv', 'w') as csv_file:
    file_writer = csv.writer(csv_file)
    file_writer.writerow(headers_2)
    keys = atla_all_scripts.keys()
    for i in range(0, len(keys)):
        file_writer.writerow([atla_all_scripts[keys[i]]])'''
    
