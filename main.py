import springer as sp
import elsiever as els
import elibrary as elib


article = input()

url_springer = f'https://link.springer.com/search?query={article}&facet-content-type=%22Article%22'
url_elsiever = f'https://www.sciencedirect.com/search?qs={article}'
url_elibrary_part = article

springer = sp.springer(url_springer)
elsiever = els.elsiever(url_elsiever)
elibrary = elib.elibrary(url_elibrary_part)

springer.run('springer.csv')
elsiever.run('elsiever.csv')
elibrary.run('elibrary.csv')








