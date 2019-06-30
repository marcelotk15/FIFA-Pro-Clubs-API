# -*- coding: utf-8 -*-

import requests
import json
import array as arr
import pprint


class __SearchResultException(Exception):
    pass


class __PlataformException(Exception):
    pass


class ProClubs():
    def __init__(self, plataform=None):
        self.__plataform = plataform
        self.clubs = []
        self.club = {}

    def searchClubsByName(self, name=None):
        clubs = self.__get('/clubsComplete/{}'.format(name))

        for c in clubs:
            self.clubs.append(clubs[c])

    def getClub(self, key=None, infos=['info', 'stats', 'matches', 'membersComplete', 'seasonRank', 'seasonalStats']):
        for info in infos:
            g = self.__get('/clubs/{}/{}'.format(key, info))

            if info == 'stats' or info == 'seasonRank' or info == 'seasonalStats':
                self.club[info] = g['{}'.format(key)]
            elif info == 'info':
                self.club[info] = g[0]
            else:
                self.club[info] = g

    def __get(self, endpoint=None):
        API_URL = 'https://www.easports.com/iframe/fifa17proclubs/api/platforms/'
        
        return requests.get(API_URL+self.__plataform+endpoint).json()['raw']


pC = ProClubs('XBOXONE')
pC.getClub(40518)
pprint.pprint(pC.club)
