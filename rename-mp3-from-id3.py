# Foxter @ 29.10.2017 - 5:21PM
# Rename mp3 files from ID3 Tags
#
# Need install mutagen: pip install mutagen 
# My current works at v1.39.dev0 and python3
# thanks a lot to gummywormz


from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError
from os import rename, walk, path


def main():
    for dirName, sundirList, fileList in walk("D:\\path-to\\mp3\\folder"):
        for fname in fileList:
            if fname.endswith("mp3"):
                try:
                    cfile = path.join(dirName,fname)
                    audio = EasyID3(cfile)
                    title = audio.get("title","Error")[0]
                    artist = audio.get("artist","Error")[0]
                    if title != "Error" and artist != "Error":
                        name = artist + " - " + title + '.mp3'
                        name = name.replace("?","")
                        name = name.replace("*","")
                        name = name.replace("/"," - ")
                        realname = cfile.replace(fname,name)
                        print(fname + " переименован в " + realname)
                        rename(cfile,realname)
                except ID3NoHeaderError: 
                        print(cfile + " не переименован")

                        
if __name__ == "__main__":
    main()
