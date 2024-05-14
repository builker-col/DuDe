from resources import DuDe
import colorama
import json
from colorama import Fore, Style

dude = DuDe('data/')
dude.find_duplicates_tqdm

duplicates = dude.get_duplicates()

for key, value in duplicates.items():
    if len(value) > 1:
        print(f'{Fore.RED}{key} has {len(value)} duplicates: {value}{Style.RESET_ALL}')
    else:
        print(f'{Fore.GREEN}{value} is duplicated by {key}{Style.RESET_ALL}')

hash_map = dude.get_hash_map()

with open('hash_map.json', 'w') as f:
    json.dump(hash_map, f)

with open('duplicates.json', 'w') as f:
    json.dump(duplicates, f)

print('Data written to hash_map.json and duplicates.json')