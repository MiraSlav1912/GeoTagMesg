import gmplot
from ClasterMap import mymap
from TEXT import Locate_search
import sqlite3
#генерація карти
class Show_map():
    def __init__(self,key):
        self.key = key
        self.data = Locate_search().searching()
        self.add_markers()
        # self.mymap = gmplot.GoogleMapPlotter(49, 32, 6, key)
        #self.mymap.draw('./mymap.html')
        # webbrowser.open('mymap.html')
    def add_markers(self):
        self.con = sqlite3.connect('All_Pars_BD.db3')
        self.cur = self.con.cursor()
        data = self.data
        import random
        for i in range(data.__len__()):
            data[i][0] = list(self.cur.execute("SELECT watch FROM main WHERE date = {0}".format(data[i][1])).fetchone())[0]
            data[i][1]= list(self.cur.execute("SELECT title FROM main WHERE date = {0}".format(data[i][1])).fetchone())[0]
            #data[i][1] = str(data[i][1]).replace('\xa','')

            # title = str(list(title)[0]).replace('"',"'")
            # rd = random.randrange(1,10000,1)
            # rd /= 1000000
        # for i in range(len(data)):
        #     print(data[i][2],data[i][3])
        # print([data[i][2],data[i][3]])
        # pos = [[data[i][2],data[i][3]] for i in range(len(data))]
        # tit = [data[i][1] for i in range(len(data))]
        # sour = [data[i][0] for _ in range(len(data))]
        mymap(data,self.key)
        pass
        #self.mymap.marker(data[i][2]+rd,data[i][3]+rd, "blue",title=title)
        #pass
        # mymap.claster(key,title,position,label)
    #self.mymap(title,[data[i][2],data[i][3]],'A',self.key)

if __name__ == '__main__':
    mp = Show_map('AIzaSyCOZ0t8PvYAnCPM5s6ZCiOngYr25C_oUy4')
    pass
