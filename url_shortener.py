import requests
def shorten_link(full_link):
    API_KEY = "" #Generate your own from cuttly website
    BASE_URL = "https://cutt.ly/api/api.php"
    payload = {'key': API_KEY, 'short': full_link}
    request = requests.get(BASE_URL, params= payload)
    data = request.json()
    try:
        short_link = data['url']['shortLink']
        print('Shortened Link: ', short_link)
    except:
        status = data['url']['status']
        print("Error: ", status)
    

link = input("Enter the link you want to shorten: ")
print("\n")
shorten_link(link)    
