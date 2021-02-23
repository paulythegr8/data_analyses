from collection_functions import *

#################################### CODE FOR IMDB INFO (RATINGS, VOTES PER RATING, RELEASE DATES) AND CLEANUP ##########################################

#Setup
atla_ratings = []
atla_total_votes = []
atla_release_dates = []
atla_seasons = []

for season in range(1, 4):
    imdb_info = collect_imdb_info("https://www.imdb.com/title/tt0417299/episodes?season=" + str(season))
    atla_ratings += imdb_info["ratings"]
    atla_total_votes += imdb_info["votes"]
    atla_release_dates += imdb_info["release_dates"]
    atla_seasons += [season] * len(imdb_info["ratings"])

#Cleanup
atla_ratings.pop(0)
atla_seasons.pop(0)
atla_total_votes.pop(0)
atla_release_dates.pop(0) #removes the pilot episode because I don't care about it

################################## CODE TO GET EPISODE TITLES AND DO CLEANUP #########################################

#Setup
fandom_url = "https://avatar.fandom.com/wiki/Avatar_Wiki:Transcripts"
atla_episode_titles = collect_titles(fandom_url, series = "atla")


#Cleanup
atla_episode_titles.pop(41) #gets rid of the pre-season 3 comic and the pilot episode
atla_episode_titles.pop(0) #gets rid of the pilot episode
atla_episode_titles[16] = atla_episode_titles[16][:-13] #to get rid of the "(commentary)" text that's appended to some of the episodes
atla_episode_titles[17] = atla_episode_titles[17][:-13]
atla_episode_titles[9] = "Jet (episode)" #renaming episodes whose urls would lead somewhere else if kept unchanged

######## CODE TO GET WIKIPEDIA INFO (EPISODE NUMBER TOTAL, EPISODE NUMBER IN THE CONTEXT OF THE SEASON, WRITERS, DIRECTORS, ANIMATON STUDIOS) #########

wikipedia_url = "https://en.wikipedia.org/wiki/List_of_Avatar:_The_Last_Airbender_episodes"
wikipedia_episode_info = collect_episode_info(wikipedia_url, series = "atla")

#Setup
atla_episode_number_overall = wikipedia_episode_info["episode_num"]
atla_episode_number_season = wikipedia_episode_info["num_in_season"]
atla_writers = wikipedia_episode_info["writers"]
atla_directors = wikipedia_episode_info["directors"]
atla_animation_studios = wikipedia_episode_info["animators"]

#Cleanup
tales_of_ba_sing_se_wda = ['Joann Estoesa, Lisa Wahlander, Andrew Huebner, Gary Scheppke, Lauren Macmullan, Katie Mattila, Justin Ridge and Giancarlo Volpe', 'Ethan Spaulding', 'DR Movie']
atla_writers[34] = tales_of_ba_sing_se_wda[0]
atla_directors[34] = tales_of_ba_sing_se_wda[1]
atla_animation_studios[34] = tales_of_ba_sing_se_wda[2]


################################## CODE TO GET SCRIPTS FOR EACH EPISODE ###########################################

#Setup
atla_all_scripts = {}
base_transcript_url = "https://avatar.fandom.com/wiki/Transcript:"

for episode in atla_episode_titles:
    url = base_transcript_url + ("_".join(episode.split(" ")))
    atla_all_scripts[episode] = collect_transcripts(url)


#troubleshooting done


