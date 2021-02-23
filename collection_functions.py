from bs4 import BeautifulSoup
import requests
import re

def collect_imdb_info(imdb_season_url): 
    '''input is an imdb url for a season of either atla or tlok. The output is a dictionary of three arrays:
    the ratings array, the array that shows how many votes determined that rating, and the release datea array.
     ALL ARRAY INDEXES CORRESPOND TO EACH OTHER'''
    request = requests.get(imdb_season_url)
    soup = BeautifulSoup(request.text, "html.parser")
    imdb_dict = {}
    imdb_dict["ratings"] = [float(rating.get_text().strip().split('\n')[0]) for rating in soup.find_all("div", class_ = "ipl-rating-star small")]
    imdb_dict["votes"] = [int(votes.get_text().strip().split('\n')[1][1:-1].replace(",", "")) for votes in soup.find_all("div", class_ = "ipl-rating-star small")]
    imdb_dict["release_dates"] = [airdate.get_text().strip() for airdate in soup.find_all("div", class_ = "airdate")]
    return imdb_dict

def collect_episode_info(wikipedia_url, series):
    '''input is a wikipedia url. Output is a dictionary of 5 arrays which are: episode writers, episode directors, episode animation studios,
    episode number, and episode number in that particular season'''
    request = requests.get(wikipedia_url)
    soup = BeautifulSoup(request.text, "html.parser")
    rows = [tr for tr in soup.find_all("tr", class_ = "vevent")]
    
    writers = []
    directors = []
    animators = []
    num_in_season = []

    for row in rows:
        data = [td.get_text() for td in row.find_all("td")]
        if series.lower() == "atla":
            num_in_season.append(int(data[0]))
            directors.append(data[2])
            writers.append(data[3])
            animators.append(data[4])
        elif series.lower() == "tlok":
            num_in_season.append(int(data[0]))
            animators.append(data[2])
            directors.append(data[3])
            writers.append(data[4])
        else:
            raise Exception("Series has either got to be atla or tlok")
    episode_num = [i for i in range(1, len(num_in_season)+ 1)]
        

    episode_info_dict = {}
    episode_info_dict["episode_num"] = episode_num
    episode_info_dict["num_in_season"] = num_in_season
    episode_info_dict["writers"] = writers
    episode_info_dict["directors"] = directors
    episode_info_dict["animators"] = animators
    return episode_info_dict


def collect_titles(fandom_url, series):
    '''input is a url of the page with the links to all of the transcripts for every avatar episode ever made. Output is an array of all episode titles'''
    request = requests.get(fandom_url)
    soup = BeautifulSoup(request.text, "html.parser")
    episode_titles = []

    tables = soup.find_all("table", class_ = "wikitable")
    for table in tables[:15]:
        for row in table.find_all("tr"):
            episode_titles.append(row.find("td").get_text().strip()[1:-1])
    if series.lower() == "atla":
        return episode_titles[:63]
    elif series.lower() == "tlok":
        return episode_titles[63:]
    else:
        raise Exception("Series has either got to be atla or tlok")
    
def collect_transcripts(episode_transcript_url):
    request = requests.get(episode_transcript_url)
    soup = BeautifulSoup(request.text, "html.parser")
    speakers = []
    lines = []

    tables = soup.find_all("table", class_ = "wikitable")
    for table in tables:
        for tr in table.find_all("tr"):
            if len(tr.find_all("td")) == 1:
                if tr.find("th"):
                    speakers.append(tr.find("th").get_text().strip())
                    lines.append(tr.find("td").get_text().strip())
                else:
                    speakers.append("Scene_Description")
                    lines.append(tr.find("td").get_text().strip())
            elif len(tr.find_all("td")) == 2:
                speakers.append("Scene_Description")
                lines.append(tr.find_all("td")[1].get_text().strip())
            else:
                raise Exception("Somethings weird with this episode url: ", episode_transcript_url)
    
    return [speakers, lines]

#print(collect_transcripts("https://avatar.fandom.com/wiki/Transcript:The_Boy_in_the_Iceberg")[1][0])








'''
for title in collect_titles("https://avatar.fandom.com/wiki/Avatar_Wiki:Transcripts", series = "atla"):
    print(title)'''






