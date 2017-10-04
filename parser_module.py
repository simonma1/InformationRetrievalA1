import BeautifulSoup


def create_parsed_text(filename):
    soup = BeautifulSoup.BeautifulSoup(filename)
    return soup.findAll('reuters')




