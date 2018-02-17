from ClasterMap import mymap
from TEXT import Locate_search
import sqlite3
#генерація карти
class Show_map():
    def __init__(self,key):
        self.key = key
        self.data = Locate_search().searching()
        self.add_markers()

    def add_markers(self):
        self.con = sqlite3.connect('All_Pars_BD.db3')
        self.cur = self.con.cursor()
        data = self.data
        import random
        for i in range(data.__len__()):
            data[i][0] = list(self.cur.execute("SELECT watch FROM main WHERE date = {0}".format(data[i][1])).fetchone())[0]
            data[i][1]= list(self.cur.execute("SELECT title FROM main WHERE date = {0}".format(data[i][1])).fetchone())[0]

        mymap(data,self.key)


if __name__ == '__main__':
    mp = Show_map('AIzaSyCOZ0t8PvYAnCPM5s6ZCiOngYr25C_oUy4')
    pass
