# -*- coding: utf-8 -*-

import requests
import json
import array as arr


class __SearchResultException(Exception):
    pass


class __PlataformException(Exception):
    pass


class ProClubs():
    def __init__(self, plataform=None):
        self.__plataform = plataform
        self.clubs = []
        self.clubInfo = []

    def searchClubsByName(self, name=None):
        clubs = self.__get('/clubsComplete/{}'.format(name))

        for c in clubs:
            self.clubs.append(clubs[c])

    def getClub(self, key=None):
        self.clubInfo = self.__get('/clubs/{}/info'.format(key))
        print(self.clubInfo)

    def __get(self, endpoint=None):
        API_URL = 'https://www.easports.com/iframe/fifa17proclubs/api/platforms/'

        return requests.get(API_URL+self.__plataform+endpoint).json()['raw']


pC = ProClubs('XBOXONE')
pC.getClub(40518)
