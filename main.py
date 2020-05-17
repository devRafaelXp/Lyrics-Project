from colorama import Fore
from os import system
import urllib
import urllib.request
import json


def request_lyrics(artist, song):
    try:
        with urllib.request.urlopen(f'https://api.lyrics.ovh/v1/{artist}/{song}') as response:
            source = response.read()
        
    except urllib.error.HTTPError:                       
        print(f'{Fore.RED}Lyrics not found about: {song.replace("-", " ")} by {artist.replace("-", " ")}{Fore.RESET}')
   
    except urllib.error.URLError:
        print(f'{Fore.RED}Connection not found{Fore.RESET}')
        print('Check your connection')
        
    except Exception as e:
        print(e)
                
    else:
        lyrics = json.loads(source)
        system('clear')
        print(f'{Fore.GREEN}SUCCESS{Fore.RESET}')
        print(f'{Fore.GREEN}Lyrics found{Fore.RESET}')
        print('-'*10)
        print(f'{Fore.YELLOW}{lyrics["lyrics"]}{Fore.RESET}')      

def show_lyrics():     
    print('Search your favorites lyrics songs'.center(50))
    print(f'{Fore.RED}Note: Some songs lyrics may not appear here{Fore.RESET}')
    print('--'*20)
    
    artist = str(input('Artist: ')).strip().replace(' ', '-').capitalize()     
    song = str(input('Song: ')).strip().replace(' ', '-').capitalize()
   
    if artist == '' or song == '':
        print('Artist/Song is blank')
        
    else:        
        print('Searching...')        
        request_lyrics(artist, song)        


show_lyrics()