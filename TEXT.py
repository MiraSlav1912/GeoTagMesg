import sqlite3
import re
from itertools import groupby
from time import time

class Locate_search:
    def __init__(self):
        self.text = self.load_text()
        self.filter = self.filter()
        self.keys = self.load_keys()
        self.search = self.searching()
        # self.koord = self.koord()

    def load_text(self):
        self.name_db = 'All_Pars_BD.db3'
        self.con = sqlite3.connect(self.name_db)
        self.cur = self.con.cursor()
        dd = self.cur.execute("SELECT name FROM sqlite_master WHERE name='main'").fetchone()
        if not dd: print("Базу даних з вхідним текстом не знайдено")
        self.cur.execute(
            "SELECT date,title,body FROM main "
            "ORDER BY date DESC")
        tx = self.cur.fetchall()
        self.con.close()
        # конвертування в list
        tx = [list(tx[i]) for i in range(tx.__len__())]
        id = [int(tx[i][0]) for i in range(tx.__len__())]
        #tx = [tx[i][1] +" "+tx[i][2] for i in range(tx.__len__())]

        tx = [[tx[i][1],tx[i][2]] for i in range(tx.__len__())]
        txid = [{id[i]:tx[i]} for i in range(id.__len__())]

        return txid

    def filter(self):
        tx = self.text
        #tx = [el for el, _ in groupby(tx)]
        #IGNOR= ['Украин', 'Росси','ВИДЕО']
        t = []
        id=[]
        for i in range(tx.__len__()):
            id.append(list(tx[i].keys())[0])
            t.append(list(tx[i].values())[0])
        t = [[re.findall(r'[А-Я]\w+',t[i][0]),re.findall(r'[А-Я]\w+',t[i][1])] for i in range(len(t))]
        tx = [[id[i],list(set(t[i][0])),list(set(t[i][1]))] for i in range(len(t))]
        return tx

    def load_keys(self):
        self.name_db = 'UA+WORLD.db3'
        self.con = sqlite3.connect(self.name_db)
        self.cur = self.con.cursor()
        dd = self.cur.execute("SELECT * FROM main").fetchone()
        if not dd:
            print("Базу даних з вхідним текстом не знайдено")
        self.cur.execute("SELECT * FROM main ")
        UA_= self.cur.fetchall()
        UA_ = [[list(UA_[i])] for i in range(UA_.__len__())]
        self.con.close()
        CORECT = []
        for i in range(len(UA_)):
            koord = str(UA_[i]).split(' ')
            lat = koord[0][2:]
            long = koord[1][:-2]
            i = 2
            names =[]
            while i < len(koord)-1:
                names.append(re.sub(r'\s', '', koord[i]))
                i+=1
            CORECT.append([names,lat,long])
            pass
        return CORECT

    def searching(self):
        tx = self.filter
        keys = self.keys
        id = [i[0] for i in tx]
        title = [i[1] for i in tx]
        # text = [i[2] for i in tx]

        match = []
        #АЛЯ ПОШУК
        for i in range(len(tx)):
            for j in range(len(title[i])):
                for x in range(len(keys)):
                    for y in range(len(keys[x][0])):
                        # keys[x][0][y] = str(keys[x][0][y]).replace(" ", '')
                        k = str(keys[x][0][y]).replace("'",'')
                        t = title[i][j]

                        # крок 1 - тупий перебір
                        if keys[x][0][y] in title[i][j]:
                            match.append([k, id[i],str(keys[x][1]).replace("'",''),str(keys[x][2]).replace("'",'')])
                        if k =='':
                            continue
                        # крок 2 - часткова відповідність
                        # збіжність першої букви
                        # print(t + '\t' + k)
                        if k[0] == t[0] and 70 < len(k) / len(t) * 100 < 130:

                            sz = len(k)
                            # if sz <= 2:
                            #     continue
                            if sz <= 4:
                                if k[:sz] == t[:sz]:
                                    match.append([k, id[i],keys[x][1]])
                                    continue
                            elif 4 < sz < 8:
                                if k[:sz - 1] == t[:sz - 1]:
                                    match.append([k, id[i],str(keys[x][1]).replace("'",''),str(keys[x][2]).replace("'",'')])
                                    continue
                            else:
                                if k[:sz - 3] == t[:sz - 3]:
                                    match.append([k, id[i],str(keys[x][1]).replace("'",''),str(keys[x][2]).replace("'",'')])
                                    continue

        #фільтр дублікатів
        seen = []
        for line in match:
            if line not in seen:
                seen.append(line)
        return seen

    # def koord(self):
    #     data = self.searching()
    #     dat = [data[i][0] for i in range(data.__len__())]
    #     dat = list(set(dat))
    #     for i in range(len(dat)):
    #         if dat[i] == 'АТО':
    #             dat[i]= 'Горлівка'
    #         if dat[i] == 'Чорне':
    #             dat[i]= 'Чорне море'
    #         if dat[i] == 'Азовське':
    #             dat[i]= 'Азовське море'
    #         if dat[i] == 'ДНР':
    #             dat[i]= 'Донецьк'
    #         if dat[i] == 'ЕС':
    #             dat[i] = 'Європа'
    #         if dat[i] == 'ЛНР':
    #             dat[i] = 'Луганськ'
    #     from geopy.geocoders import Nominatim
    #     import time, random
    #
    #     koord = []
    #     for i in range(dat.__len__()):
    #         geolocator = Nominatim(timeout=2)
    #         try:
    #             location = geolocator.geocode("%s"% dat[i])
    #         except:
    #             import time
    #             time.sleep(5)
    #             location = geolocator.geocode("%s" % dat[i])
    #         lat = location.latitude
    #         long = location.longitude
    #         koord.append([dat[i],lat,long])
    #     all_data = []
    #     for i in range(len(data)):
    #         for j in range(len(koord)):
    #             if koord[j][0] == data[i][0]:
    #                 all_data.append([data[i][1],data[i][0],koord[j][1],koord[j][2]])
    #     return all_data


if __name__ == '__main__':
    l = Locate_search()
    print(l)


# tic = time()
#toc =  time()
#print(tic - toc)
