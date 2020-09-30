import bs4
import requests



playlist=[]
url=input("Enter the Youtube Playlist URL : ") #Takes the Playlist Link
try:
    data = requests.get(url)
except:
    print("Error: Unable to fetch data from the error or the link is not valid.")
    exit()
soup=bs4.BeautifulSoup(data.text,'html.parser')


for links in soup.find_all('a'):
        link=links.get('href')
        if (link[0:6]=="/watch" and link[0]!="#"):
            link="https://www.youtube.com"+link
            link=str(link)
            playlist.append(link)
del playlist[0:2]
