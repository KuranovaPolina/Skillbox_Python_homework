import requests
import json


my_rec = requests.get('https://breakingbadapi.com/api/deaths/')
deaths_info = json.loads(my_rec.text)

sorted_deaths_info = sorted(deaths_info, key=lambda elem: elem["number_of_deaths"], reverse=True)

my_rec2 = requests.get(f'https://breakingbadapi.com/api/episodes')
episodes_info = json.loads(my_rec2.text)

episode_id = 0
death_list = []
for episode in episodes_info:
    if int(episode['season']) == sorted_deaths_info[0]['season'] and int(episode['episode']) == sorted_deaths_info[0]['episode']:
        episode_id = episode['episode_id']
        break

for death in deaths_info:
    if int(death['season']) == sorted_deaths_info[0]['season'] and death['episode'] == sorted_deaths_info[0]['episode']:
        death_list.append(death['death'])

result_dict = {
    'episode_id': episode_id,
    'season': sorted_deaths_info[0]['season'],
    'episode': sorted_deaths_info[0]['episode'],
    'death_count': sorted_deaths_info[0]['number_of_deaths'],
    'death_list': death_list
}

print(result_dict)

with open('result.json', 'w') as file:
    json.dump(result_dict, file, indent=4)
