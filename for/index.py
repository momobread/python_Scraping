from requests import get

websites = (
    "google.com",
    "https://airbnb.com",
    "twitter.com",
    "https://facebook.com"
)

results = {

}


for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    reponse = get(website)
    if reponse.status_code >= 500:
        results[website] ="server Error"
    elif reponse.status_code >=400:
        results[website] = "client error"
    elif reponse.status_code >=300:
        results[website] = "please redirect"
    elif reponse.status_code >=200:
        results[website] ="Ok"
    elif reponse.status_code >=100:
        results[website] = "inform"
    else:
        results[website] ="Failed"

print(results)


