import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import wget



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    http = httplib2.Http()
    dropbox_path="C:/dropbox/target"
    i=1
    for element in range(40,50):
        print("Processing page ----------------------- "+str(element)+" ----------------------------------------------------------------------------------------------------")
        status, response = http.request('https://www.amigaremix.com/remixes/'+str(element))

        for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
            if link.has_attr('href'):
                if ".mp3" in link["href"]:
                    print("Downloading file nr. "+str(i))
                    print(link['href'])
                    string=link['href'].replace("\""," ")

                    wget.download("https://www.amigamusicremixer.com"+string,dropbox_path)
                    print("\n")
                    i = i + 1





