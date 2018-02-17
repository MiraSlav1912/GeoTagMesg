__author__ = 'Myroslav'

from lxml.html import fromstring
import htmlmov
from datetime import date,timedelta
from urllib.request import urlparse
import sqlite3

RU_MONTH = [{'январь':'01'}, {'февраль':'02'}, {'март':'03'}, {'апрель':'04'}, {'май':'05'}, {'июнь':'06'},
            {'июль':'07'},{'август':'08'},{'сентябрь':'09'}, {'октябрь':'10'}, {'ноябрь':'11'}, {'декабрь':'12'}]

class Cenzor:
    def get_name(self): return 'Цензор'

    def check_on_duplicate(self,dT):
        name_db = 'All_Pars_BD.db3'
        con = sqlite3.connect(name_db)
        cur = con.cursor()
        try: dd = cur.execute("SELECT date FROM main").fetchone()
        except: return ''

        dT  = str(dT).replace("-",'')
        dT = dT[-2:]+dT[-4:-2] + dT[2:4]
        if dT[0] == 0 : dT = dT[1:]
        cur.execute(
            "SELECT link FROM main "
            "WHERE domain LIKE '%{0}%' and date between {1} AND {2} ".format(Cenzor().get_name(), int(dT) * 10000, int(dT) * 10000 + 9999))
        check_list = cur.fetchall()
        return check_list
    def run(self, dT):
        hrf = []
        url = 'https://censor.net.ua/news/all/page/{1}/archive/{0}/category/0/sortby/hits'
        chek_list = Cenzor().check_on_duplicate(dT)
        try:
            #Завантажуємо код сторінки
            i = 1
            while i < 5:
                url_ = url.format(dT,i)
                i+=1
                page = htmlmov.url_line(url_)
                doc = fromstring(page)
                doc.make_links_absolute(url_)
                #Заванажуємо посилання повідовлень за зазначену дату
                ref_news = doc.xpath("//div[@class = 'curpane']//article[@class = 'item type1']//h3/a")
                hrf += [ref_news[x].get("href") for x in range(ref_news.__len__())]
                [hrf.remove(j) for i in chek_list for j in hrf if i[0] == j]
        except Exception as ex:
                print(ex)
        inf = [[],[],[],[],[],[]]
        qwe=0
        if len(hrf) == 0:
            print("Пусто")
            return inf

        for x in hrf:
            try:
                qwe +=1
                print("{0}/{1}".format(qwe,hrf.__len__()))
                url_1 = x
                page1 = htmlmov.url_line(url_1)
                doc1 = fromstring(page1)
                doc1.make_links_absolute(url_1)
                #Заповлення масиву даними
                inf[0].append(url_1)
                datePub = str(doc1.xpath("//article//header/time[@class = 'published dateline']/text()"))
                datePub = str(datePub).replace("'",'').replace(' ','').replace(":",'').replace('.','').replace('[','').replace(']','')
                inf[1].append(datePub)
                title = doc1.xpath("//article//header/h1/text()")
                inf[2].extend(title)
                t = doc1.xpath("//div[@class = 'text']//h2/text()")
                t += doc1.xpath("//div[@class = 'text']//p/text()")
                txt = ' '.join([x.strip() for x in t if x.strip()])
                inf[3].append(txt.replace('\xa0',''))
                inf[4].append(str(Cenzor().get_name()))
                w = doc1.xpath("//div[@class ='main']//span[@title = 'просмотров']//span[@class ='info']/text()")
                inf[5].append(w[0])
            except Exception as ex:
                print(ex)
            continue
        return inf
    def write_bd(self,dT):
        self.name_db = 'All_Pars_BD.db3'
        self.con = sqlite3.connect(self.name_db)
        self.cur = self.con.cursor()
        self.inf = self.run(dT)

        dd = self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='main'").fetchone()
        if not dd:
            self.cur.execute('''CREATE TABLE main
                                    ( link text,date integer, title text, body text, domain text, watch text)''')

        # for i in range(self.inf[0].__len__()): self.cur.execute("INSERT INTO main (watch) VALUES ({0})".format(self.inf[5][i]))
        # pass
        [self.cur.execute("INSERT INTO main ( link, date, title, body, domain, watch) "
                          "VALUES (?, ?, ?, ?, ?, ?)",
                          (self.inf[0][i], self.inf[1][i], self.inf[2][i], self.inf[3][i], self.inf[4][i], self.inf[5][i]))
         for i in range(self.inf[0].__len__())]

        self.con.commit()
        self.con.close()

class ZelvRU:
    def get_name(self): return 'ЗелвРУ'

    def run(self, dT):
        hrf = []
        url = 'https://zelv.ru/v-rossii/page/{0}'
        chek_list = ZelvRU().check_on_duplicate_1(dT)
        try:
            #Завантажуємо код сторінки
            i = 1
            while i < 10:
                url_ = url.format(i)
                i+=1
                page = htmlmov.url_line(url_)
                doc = fromstring(page)
                doc.make_links_absolute(url_)
                #Заванажуємо посилання повідовлень за зазначену дату
                import re
                dat = doc.xpath("//div[@class = 'newsitem_tools']//div[@class = 'newsitem_published']/text()")
                mon = [re.findall(r'[а-я]+',dat[i])[1] for i in range(dat.__len__())]
                for i in range(dat.__len__()):
                    try:
                        for j in range(RU_MONTH.__len__()):
                            mon[i] = RU_MONTH[0][mon[i]]
                    except:
                        continue

                day_year = [''.join(re.findall(r'\d',dat[i])) for i in range(dat.__len__())]
                dat = [day_year[i][:2]+mon[i]+day_year[i][2:] for i in range(dat.__len__())]
                ref_news = doc.xpath("//div[@class = 'news_item_c']//h2/a")
                hrf += [ref_news[x].get("href") for x in range(ref_news.__len__())]
                hrf = [[hrf[i],dat[i]] for i in range(hrf.__len__())]

                hrf_new= []
                for i in range(hrf.__len__()):
                    if hrf[i][1][:-4] == dT:
                        if len(chek_list) !=0:
                            for j in range(chek_list.__len__()):
                                if chek_list[j][0] == hrf[i][0]:
                                    hrf_new.append(hrf[i])
                        else:
                            hrf_new.append(hrf[i])
                pass


        except Exception as ex:
                print(ex)
        inf = [[],[],[],[],[]]
        qwe=0
        if len(hrf_new) == 0:
            print("Пусто")
            return inf

        for x in hrf_new:
            try:
                qwe +=1
                print("{0}/{1}".format(qwe,hrf_new.__len__()))
                url_1 = x[0]
                page1 = htmlmov.url_line(url_1)
                doc1 = fromstring(page1)
                doc1.make_links_absolute(url_1)
                #Заповлення масиву даними
                inf[0].append(url_1)

                if x[1][0] == '0':
                    dP = x[1][1:]
                else:
                    dP = x[1]
                # d m y t
                date_Pub = dP[:-10] + dP[-10:-8] + dP[-6:-4] + dP[-4:]
                inf[1].append(date_Pub)
                title = doc1.xpath("//div[@class = 'title']/h1/text()")
                inf[2].extend(title)
                t = doc1.xpath("//div[@class = 'title']/div[@class='newsitem_text']/text()")
                txt = ' '.join([x.strip() for x in t if x.strip()])
                inf[3].append(txt)
                inf[4].append(ZelvRU().get_name())
            except Exception as ex:
                print(ex)
            continue
        return inf
    def write_bd(self,dT):
        self.name_db = 'All_Pars_BD.db3'
        self.con = sqlite3.connect(self.name_db)
        self.cur = self.con.cursor()
        self.inf = self.run(dT)

        dd = self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='main'").fetchone()
        if not dd:
            self.cur.execute('''CREATE TABLE main
                                    ( link text,date integer, title text, body text, domain text)''')

        [self.cur.execute("INSERT INTO main ( link, date, title, body, domain) "
                          "VALUES (?, ?, ?, ?, ?)",
                          (self.inf[0][i], self.inf[1][i], self.inf[2][i], self.inf[3][i], self.inf[4][i]))
         for i in range(self.inf[0].__len__())]

        self.con.commit()
        self.con.close()
    def check_on_duplicate_1(self,dT):
        name_db = 'All_Pars_BD.db3'
        con = sqlite3.connect(name_db)
        cur = con.cursor()
        try: dd = cur.execute("SELECT date FROM main").fetchone()
        except: return ''
        # if dT[0] =='0':
        #     dT = dT[1:]
        dT  = str(dT).replace("-",'')
        dT = dT[:-4]+dT[-2:]
        if dT[0] == 0 : dT = dT[1:]
        cur.execute(
            "SELECT link FROM main "
            "WHERE domain LIKE '%{0}%' and date between {1} AND {2} ".format(ZelvRU().get_name(), int(dT) * 10000, int(dT) * 10000 + 9999))
        check_list = cur.fetchall()
        return check_list

class ZelvUA:
    def get_name(self): return 'ЗелвЮА'

    def run(self, dT):
        hrf = []
        url = 'https://zelv.ru/ukraina/page/{0}'
        chek_list = ZelvUA().check_on_duplicate_1(dT)
        try:
            #Завантажуємо код сторінки
            i = 1
            while i < 10:
                url_ = url.format(i)
                i+=1
                page = htmlmov.url_line(url_)
                doc = fromstring(page)
                doc.make_links_absolute(url_)
                #Заванажуємо посилання повідовлень за зазначену дату
                import re
                dat = doc.xpath("//div[@class = 'newsitem_tools']//div[@class = 'newsitem_published']/text()")
                mon = [re.findall(r'[а-я]+',dat[i])[1] for i in range(dat.__len__())]
                for i in range(dat.__len__()):
                    try:
                        for j in range(RU_MONTH.__len__()):
                            mon[i] = RU_MONTH[0][mon[i]]
                    except:
                        continue

                day_year = [''.join(re.findall(r'\d',dat[i])) for i in range(dat.__len__())]
                dat = [day_year[i][:2]+mon[i]+day_year[i][2:] for i in range(dat.__len__())]
                ref_news = doc.xpath("//div[@class = 'news_item_c']//h2/a")
                hrf += [ref_news[x].get("href") for x in range(ref_news.__len__())]
                hrf = [[hrf[i],dat[i]] for i in range(hrf.__len__())]

                hrf_new= []
                for i in range(hrf.__len__()):
                    if hrf[i][1][:-4] == dT:
                        if len(chek_list) !=0:
                            for j in range(chek_list.__len__()):
                                if chek_list[j][0] == hrf[i][0]:
                                    hrf_new.append(hrf[i])
                        else:
                            hrf_new.append(hrf[i])
                pass


        except Exception as ex:
                print(ex)
        inf = [[],[],[],[],[]]
        qwe=0
        if len(hrf_new) == 0:
            print("Пусто")
            return inf

        for x in hrf_new:
            try:
                qwe +=1
                print("{0}/{1}".format(qwe,hrf_new.__len__()))
                url_1 = x[0]
                page1 = htmlmov.url_line(url_1)
                doc1 = fromstring(page1)
                doc1.make_links_absolute(url_1)
                #Заповлення масиву даними
                inf[0].append(url_1)

                if x[1][0] == '0':
                    dP = x[1][1:]
                else:
                    dP = x[1]
                # d m y t
                date_Pub = dP[:-10] + dP[-10:-8] + dP[-6:-4] + dP[-4:]
                inf[1].append(date_Pub)
                title = doc1.xpath("//div[@class = 'title']/h1/text()")
                inf[2].extend(title)
                t = doc1.xpath("//div[@class = 'title']/div[@class='newsitem_text']/text()")
                txt = ' '.join([x.strip() for x in t if x.strip()])
                inf[3].append(txt)
                inf[4].append(ZelvUA().get_name())
            except Exception as ex:
                print(ex)
            continue
        return inf
    def write_bd(self,dT):
        self.name_db = 'All_Pars_BD.db3'
        self.con = sqlite3.connect(self.name_db)
        self.cur = self.con.cursor()
        self.inf = self.run(dT)

        dd = self.cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='main'").fetchone()
        if not dd:
            self.cur.execute('''CREATE TABLE main
                                    ( link text,date integer, title text, body text, domain text)''')

        [self.cur.execute("INSERT INTO main ( link, date, title, body, domain) "
                          "VALUES (?, ?, ?, ?, ?)",
                          (self.inf[0][i], self.inf[1][i], self.inf[2][i], self.inf[3][i], self.inf[4][i]))
         for i in range(self.inf[0].__len__())]

        self.con.commit()
        self.con.close()
    def check_on_duplicate_1(self,dT):
        name_db = 'All_Pars_BD.db3'
        con = sqlite3.connect(name_db)
        cur = con.cursor()
        try: dd = cur.execute("SELECT date FROM main").fetchone()
        except: return ''
        # if dT[0] =='0':
        #     dT = dT[1:]
        dT  = str(dT).replace("-",'')
        dT = dT[:-4]+dT[-2:]
        if dT[0] == 0 : dT = dT[1:]
        cur.execute(
            "SELECT link FROM main "
            "WHERE domain LIKE '%{0}%' and date between {1} AND {2} ".format(ZelvUA().get_name(), int(dT) * 10000, int(dT) * 10000 + 9999))
        check_list = cur.fetchall()
        return check_list


if __name__ == '__main__':
        date_load = date.today()
        # dT = str(date_load.strftime('%d%m%Y'))
        dT ='2018-02-08'
        #m = Cenzor().run(dT)
        m = Cenzor().write_bd(dT)
        pass



