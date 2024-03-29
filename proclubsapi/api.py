"""-*- coding: utf-8 -*-"""

import requests
import json
import array as arr
import pprint
from conf.settings import API_URL, PLATAFORMS, INFOS


class ProClubs():
    def __init__(self, plataform):
        if plataform.upper() in PLATAFORMS:
            self.__plataform = plataform
        else:
            raise Exception('Wrong plataform...')
        self.clubs = []
        self.club = {}

    def searchClubsByName(self, name):
        clubs = self.__get('/clubsComplete/{}'.format(name))
        for c in clubs:
            self.clubs.append(clubs[c])

    def getClub(self, key, infos=INFOS):
        for i in infos:
            g = self.__get('/clubs/{}/{}'.format(key, i))

            if (i == 'stats') or (i == 'seasonRank') or (i == 'seasonalStats'):
                self.club[i] = g['{}'.format(key)]
            elif i == 'info':
                self.club[i] = g[0]
            else:
                self.club[i] = g

    def __get(self, endpoint=None):
        url = '{}{}{}'.format(API_URL, self.__plataform, endpoint)

        return requests.get(url).json()['raw']
