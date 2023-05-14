
    url = f"https://www.bing.com/images/search?q={key}&form=HDRSC2" # search URL for image results

    response = requests.get(url)
    for _ in range(6):
        soup = BeautifulSoup(response.content, "html.parser")
        response = requests.get(url, headers={"Range": "bytes=100-"})
        results = soup.find_all("div", class_="imgpt")
