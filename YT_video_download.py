import pytube

link = input('Enter YT Video URL: ')
yt = pytube.YouTube(link)
yt.streams.first().download()
print('Downloaded', link)
