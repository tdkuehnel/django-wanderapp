from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core import mail
from django.test import TestCase
from django_webtest import WebTest
from django.urls import reverse
from io import BytesIO

from .models import Benutzer

from .testhilfen import create_benutzer, output

import datetime

# Create your tests here.

class BenutzerWanderstreckeFunctionalTest(TestCase):

    def test_wanderstrecke_wizard(self):
        """ Test Anlegen einer Wanderstrecke mit dem Wizard."""

        # Anlegen von Wanderstrecke für unangemeldete Benutzer zur Zeit nicht möglich.
        # Das kann sich aber ändern.
        response = self.client.get('/benutzer/wanderstreckewizardc1/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ihre Anmeldedaten', response.content)

        # Teste das Anlegen einer Wanderstrecke mit dem Wizard für angemeldete Benutzer.
        benutzer = create_benutzer('name123', 'kennwort')
        self.assertIsNotNone(benutzer)
        credentials = {'username': 'name123', 'password': 'kennwort' }
        response = self.client.post('/benutzer/anmeldung/', credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

        response = self.client.get('/benutzer/wanderstrecken/'+str(benutzer.id)+'/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ihre Wanderstrecken', response.content)
        self.assertIn('Hinzufügen mit Wizard'.encode(), response.content)

        formdata = {'bezeichnung':'Testwanderstrecke', 'beschreibung':'Blablub'}
        response = self.client.post('/benutzer/wanderstreckewizardc1/', formdata, follow=True)
        self.assertIn('Schritt 2'.encode(), response.content)

        object_id = response.redirect_chain[0][0][-2]
        with open('benutzer/test_json.json', "rb") as eingabedatei:
            formdata = {'json':eingabedatei, 'url': b'dasdasdassd'}
            response = self.client.post('/benutzer/wanderstreckewizard2/' + object_id +'/', formdata, follow=True)
        self.assertIn('Schritt 3'.encode(), response.content)

        img = BytesIO(
            b"GIF89a\x01\x00\x01\x00\x00\x00\x00!\xf9\x04\x01\x00\x00\x00"
            b"\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01\x00\x00"
        )
        img.name = 'bilddatei.gif'
        formdata = {'bild':img}
        response = self.client.post('/benutzer/wanderstreckewizard3/' + object_id +'/', formdata, follow=True)

        self.assertIn('Testwanderstrecke'.encode(), response.content)
        self.assertIn('Bearbeiten'.encode(), response.content)

        response = self.client.get('/benutzer/wanderstrecken/'+str(benutzer.id)+'/', follow=True)
        self.assertIn('Testwanderstrecke'.encode(), response.content)

        # Löschen der Wanderstrecke testen.
        response = self.client.post('/benutzer/wanderstrecke/loeschen/' + object_id +'/', follow=True)
        self.assertIn('Zur Zeit keine vorhanden'.encode(), response.content)

        #import pdb; pdb.set_trace()
        #output(response.content)
