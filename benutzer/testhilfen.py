from bs4 import BeautifulSoup as bs

from .models import Benutzer

def create_benutzer(username, password, email=''):
    benutzer = Benutzer.objects.create_user(username=username, password=password, email=email)
    return benutzer

def get_benutzer():
    return Benutzer.objects.all()[0]

def delete_benutzer(benutzer):
    benutzer.delete()

def output(html_document):
    with open('seite.html', 'wb') as ausgabedatei:
        ausgabedatei.write(html_document)

def pretty(html_document):
    soup = bs(html_document, 'html.parser')
    print(soup.prettify())

def pretty_form(form):
    for entry in form:
        print(entry)
