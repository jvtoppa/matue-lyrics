import time
import tweepy
import random
import linecache
import creds

#auth key
auth = tweepy.OAuth1UserHandler(creds.oauth1, creds.oauth2, creds.oauth3, creds.oauth4)
#api call
api = tweepy.API(auth)
while True:
    #abre letras
    with open("tue_musicas.txt", 'r', encoding="utf-8") as file:
    #le as linhas e seleciona uma linha aleatoriamente
        x = len(file.readlines())

        y = random.randint(0, x)

    line = linecache.getline('tue_musicas.txt', y)
    line2 = linecache.getline('tue_musicas.txt', y+1)
    #escolhe linhas que não comecem com parenteses, linhas vazias ou linhas com o título da música
    while line == '\n' or (('Lyrics' in line) == True) or (('Embed' in line) == True) or line2 == '\n' or (('Lyrics' in line2) == True) or (('Embed' in line2) == True):
        y = random.randint(0, x)
        line2 = linecache.getline('tue_musicas.txt', y+1)
        if line == line2 or line2[0] == '(':
            line2 == ''
        line = linecache.getline('tue_musicas.txt', y)


    print(line+line2)
    api.update_status(status=line+line2)
    #espera uma hora (aparece no console)
    for i in reversed(range(1,3600)):

        print(f"{i}   ", end="\r", flush=True)
        time.sleep(1)

    
