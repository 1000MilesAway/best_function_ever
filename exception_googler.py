import webbrowser
from googlesearch import search

whitelist = ['stackoverflow.com', 'ru.stackoverflow.com']


def google_problem(error):
    query = "Python " + str(error)
    search_result = search(query, tld="co.in", stop=10)
    for j in search_result:
        domain = j[8:].split('/')[0]
        if domain in whitelist:
            webbrowser.open(j, new=0, autoraise=True)
            break
