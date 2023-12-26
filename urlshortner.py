import pyshorteners

def shortenurl(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

url_shorten = input("Enter url : ")
shortened = shortenurl(url_shorten)
print("Original URL:", url_shorten)
print("Shortened URL:", shortened)

