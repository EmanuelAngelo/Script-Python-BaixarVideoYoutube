from pytube import YouTube, streams
from pytube.cli import on_progress

link = input("Insira o link aqui jovem: ")

yt = YouTube(link, on_progress_callback= on_progress)

print( "Titulo do video: ", yt.title)
print("Baixando...")

ys = yt.streams.get_highest_resolution()
ys.download()
