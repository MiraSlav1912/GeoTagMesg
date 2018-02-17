#! -*- coding:utf-8 -*-
import re
from datetime import datetime
import urllib.request
from encodings.aliases import aliases as cdn
import requests

class line_zmi:
    def __init__(self, title, text_, date_, link, domain):
        self.title = title.strip()[:250]
        self.text = text_.strip()
        self.date = date_
        self.link = link
        self.source = domain
        self.dt_edit = datetime.today()
        self.reason = ''
        self.target = ''
        self.comment = ''
        self.loyalty = ''

    def to_dict(self):
        return {x: self.__dict__[x] for x in self.__dict__}

def clear_1(line):
    line = re.sub(r'< ?/i ?>', '', line)
    line = re.sub(r'< ?i ?>', '', line)
    line = re.sub(r'< ?/em ?>', '', line)
    line = re.sub(r'< ?em ?>', '', line)
    line = re.sub(r'< ?/li ?>', '', line)
    line = re.sub(r'< ?li ?>', '', line)
    line = re.sub(r'< ?/span ?>', '', line)
    line = re.sub(r'< ?span ?>', '', line)
    line = re.sub(r'< ?/strong ?>', '', line)
    line = re.sub(r'< ?strong ?>', '', line)
    line = re.sub(r'< ?script.+?/ ?script ?>(?s)', '', line)
    line = re.sub(r'< ?style.+?/ ?style ?>(?s)', '', line)
    line = re.sub(r'<!--.+?-->(?s)', r'', line)
    line = re.sub(r'\n( |\t|\f|\r)*\n', '', line)
    line = re.sub(r'< ?img.*?>', '', line)
    line = re.sub(r'</a>', '', line)
    line = re.sub(r'<a .*?>', '', line)
    line = re.sub(r'<br>', '', line)
    return line

def clear__(line):
    line = re.sub(r'< ?/i ?>', '', line)
    line = re.sub(r'< ?i ?>', '', line)
    line = re.sub(r'< ?/em ?>', '', line)
    line = re.sub(r'< ?em ?>', '', line)
    line = re.sub(r'< ?/li ?>', '', line)
    line = re.sub(r'< ?li ?>', '', line)
    line = re.sub(r'< ?script.+?/ ?script ?>(?s)', '', line)
    line = re.sub(r'< ?strong.+?/ ?strong ?>(?s)', '', line)
    line = re.sub(r'< ?style.+?/ ?style ?>(?s)', '', line)
    line = re.sub(r'<!--.+?-->(?s)', r'', line)
    line = re.sub(r'\n( |\t|\f|\r)*\n', '', line)
    line = re.sub(r'< ?img.*?>', '', line)
    line = re.sub(r'</a>', '', line)
    line = re.sub(r'<a .*?>', '', line)
    line = re.sub(r'<br>', '', line)
    return line


def clear_href(f_in):
    f_out = f_in[:f_in.rfind('.')] + '_hr' + f_in[f_in.rfind('.'):]
    with open(f_out, 'w', encoding='utf_8') as f:
        for line in open(f_in, 'r', encoding='utf_8'):
            line1 = re.sub(r'</a>', '', line)
            f.write(re.sub(r'<a .*?>', '', line1))
    return f_out


def clean_html(f_in):
    line = ''.join(open(f_in, 'r', encoding='utf_8'))
    line = re.sub(r'< ?/p ?>', '', line)
    line = re.sub(r'< ?p ?.*?>', '', line)
    line = re.sub(r'< ?/i ?>', '', line)
    line = re.sub(r'< ?i ?>', '', line)
    line = re.sub(r'< ?/em ?>', '', line)
    line = re.sub(r'< ?em ?>', '', line)
    line = re.sub(r'< ?/li ?>', '', line)
    line = re.sub(r'< ?li ?>', '', line)
    line = re.sub(r'< ?script.+?/ ?script ?>(?s)', '', line)
    line = re.sub(r'< ?style.+?/ ?style ?>(?s)', '', line)
    line = re.sub(r'<!--.+?-->(?s)', r'', line)
    line = re.sub(r'\n( |\t|\f|\r)*\n', '', line)
    line = re.sub(r'< ?img.*?>', '', line)
    line = re.sub(r'</a>', '', line)
    line = re.sub(r'<a .*?>', '', line)
    line = re.sub(r'<.*?>', ' TAG ', line)
    return line


def cl_html(line):
#line=re.sub(r'< ?/p ?>','',line)
    #line=re.sub(r'< ?p ?.*?>','',line)
    line = re.sub(r'< ?/i ?>', '', line)
    line = re.sub(r'< ?i ?>', '', line)
    line = re.sub(r'< ?/em ?>', '', line)
    line = re.sub(r'< ?em ?>', '', line)
    line = re.sub(r'< ?/li ?>', '', line)
    line = re.sub(r'< ?li ?>', '', line)
    line = re.sub(r'< ?script.+?/ ?script ?>(?s)', '', line)
    line = re.sub(r'< ?style.+?/ ?style ?>(?s)', '', line)
    line = re.sub(r'<!--.+?-->(?s)', r'', line)
    line = re.sub(r'\n( |\t|\f|\r)*\n', '', line)
    line = re.sub(r'< ?img.*?>', '', line)
    line = re.sub(r'</a>', '', line)
    line = re.sub(r'<a .*?>', '', line)
    line = re.sub(r'<.*?>', ' TAG ', line)
    return line


def clear_(f_in, script=True, style=True, space_line=True, comment=True, img=True, link=True):
    f_out = f_in[:f_in.rfind('.')] + '_clr' + f_in[f_in.rfind('.'):]
    with open(f_out, 'w', encoding='utf_8') as f:
        line = ''.join(open(f_in, 'r', encoding='utf_8'))
        line = re.sub(r'< ?/p ?>', '', line)
        line = re.sub(r'< ?p ?.*?>', '', line)
        line = re.sub(r'< ?/i ?>', '', line)
        line = re.sub(r'< ?i ?>', '', line)
        line = re.sub(r'< ?/li ?>', '', line)
        line = re.sub(r'< ?li ?>', '', line)
        if script:
            patern = re.compile(r'< ?script.+?/ ?script ?>', re.DOTALL)
            line = patern.sub('', line)
        if style:
            patern = re.compile(r'< ?style.+?/ ?style ?>', re.DOTALL)
            line = patern.sub('', line)
        if comment:
            patern = re.compile(r'<!--.+?-->', re.DOTALL)
            line = patern.sub('', line)
        if space_line:
            line = re.sub(r'\n( |\t|\f|\r)*\n', '', line)
        if img:
            line = re.sub(r'< ?img.*?>', '', line)
        if link:
            line = re.sub(r'</a>', '', line)
            line = re.sub(r'<a .*?>', '', line)
        f.write(line)
    return f_out


def url_line_header(url_, hst):
    r = urllib.request.Request(url=url_)
    r.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/30.0')
    r.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    r.add_header('Accept-Language', 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3')
    r.add_header('Accept-Encoding', 'identity, *;q=0')
    r.add_header('Connection', 'keep-alive')
    r.add_header('Cache-Control', 'max-age=0')
    r.add_header('Host', hst)
    r.method = 'GET'
    try:
        f = urllib.request.urlopen(r, timeout=3.0)
        cod = cod_page(f)
        fl = f.read().decode(cod, errors='ignore')# 'replace')
        return fl
    except urllib.error.HTTPError:
        return None
        # print('connect error')
    except urllib.error.URLError:
        pass#print('url error')
    return None

def url_line_header_ruvesna(url_, hst='rusvesna.su'):
    """GET /news HTTP/1.1

Host: rusvesna.su

User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3

Accept-Encoding: gzip, deflate

Cookie: __cfduid=d10b947010da40e46385e8cd8680f42ed1458284615; _ga=GA1.2.1491951867.1458284530; _ym_uid=1458284531265355917; jcsuid=BnopKcnancTw9tOjjX8D; has_js=1; __lx198116_load_cnt=6; __lx198116_load_tmr=1472117804025; __lx198116_load_tmr_pre=1472117804453; kdmViewedPages=2; kdmRefUrl=; kdmLocUrl=http%253A%252F%252Frusvesna.su%252Fnews; _ym_isad=2; OX_sd=2; OX_plg=swf|sl|pdf|wmp|shk|pm; slidebox=open; _ym_visorc_33632934=b; KCMFLAG=1; _gat=1; ar_syn=1

Connection: keep-alive

If-Modified-Since: Thu, 28 Jul 2016 10:37:11 GMT

Cache-Control: max-age=0
"""
    r = urllib.request.Request(url=url_)
    r.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0')
    r.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    r.add_header('Accept-Language', 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3')
    r.add_header('Accept-Encoding', 'deflate')
    r.add_header('Cookie', '__cfduid=d10b947010da40e46385e8cd8680f42ed1458284615; _ga=GA1.2.1491951867.1458284530; _ym_uid=1458284531265355917; jcsuid=BnopKcnancTw9tOjjX8D; has_js=1; __lx198116_load_cnt=6; __lx198116_load_tmr=1472117804025; __lx198116_load_tmr_pre=1472117804453; kdmViewedPages=2; kdmRefUrl=; kdmLocUrl=http%253A%252F%252Frusvesna.su%252Fnews; _ym_isad=2; OX_sd=2; OX_plg=swf|sl|pdf|wmp|shk|pm; slidebox=open; _ym_visorc_33632934=b; KCMFLAG=1; _gat=1; ar_syn=1')
    r.add_header('Connection', 'keep-alive')
    r.add_header('Cache-Control', 'max-age=0')
    r.add_header('Host', hst)
    r.method = 'GET'
    try:
        f = urllib.request.urlopen(r, timeout=3.0)
        cod = cod_page(f)
        fl = f.read().decode(cod, errors='ignore')# 'replace')
        return fl
    except urllib.error.HTTPError:
        return None
        # print('connect error')
    except urllib.error.URLError:
        pass#print('url error')
    return None

def url_line_header_segodnya(url_, hst):
    r = urllib.request.Request(url=url_)
    r.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0')
    r.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    r.add_header('Accept-Language', 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3')
    r.add_header('Accept-Encoding', 'deflate')
    r.add_header('Cookie', '_ddn_intercept_2_=4e67be4fc20d6d41eaf55e80a63f93fc; has_js=1; _ym_visorc_10957408=b')
    r.add_header('Connection', 'keep-alive')
    r.add_header('Cache-Control', 'max-age=0')
    r.add_header('Host', hst)
    r.method = 'GET'
    try:
        f = urllib.request.urlopen(r, timeout=3.0)
        cod = cod_page(f)
        fl = f.read().decode(cod, errors='ignore')# 'replace')
        return fl
    except urllib.error.HTTPError:
        return None
        # print('connect error')
    except urllib.error.URLError:
        pass#print('url error')
    return None

def url_line_header_itar_tass(url_, hst):
    r = urllib.request.Request(url=url_)
    r.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0')
    r.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    r.add_header('Accept-Language', 'uk,ru;q=0.8,en-us;q=0.5,en;q=0.3')
    r.add_header('Accept-Encoding', 'deflate')
    r.add_header('Connection', 'keep-alive')
    r.add_header('Cache-Control', 'max-age=0')
    r.add_header('Host', hst)
    r.method = 'GET'
    try:
        f = urllib.request.urlopen(r, timeout=3.0)
        cod = cod_page(f)
        fl = f.read().decode(cod, errors='ignore')
        return fl
    except urllib.error.HTTPError:
        return None
        # print('connect error')
    except urllib.error.URLError:
        pass#print('url error')
    return None

def url_line_header1251(url_, hst):
    r = urllib.request.Request(url=url_)
    r.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0')
    r.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    r.add_header('Accept-Language', 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3')
    r.add_header('Accept-Encoding', 'identity, *;q=0')
    r.add_header('Connection', 'keep-alive')
    r.add_header('Cache-Control', 'max-age=0')
    r.add_header('Host', hst)
    r.method = 'GET'
    try:
        f = urllib.request.urlopen(r, timeout=3.0)
        fl = f.read().decode('cp1251', 'replace')
        return fl
    except urllib.error.HTTPError:
        return None
        # print('connect error')
    except urllib.error.URLError:
        pass #print('url error')
    except:
        f = urllib.request.urlopen(r, timeout=3.0)
        fl = f.read().decode('cp1251')
        return fl
    return None


def url_line__(url):
    """Повертає веб-сторінку в строці з кодуванням utf-8"""
    try:
        f = urllib.request.urlopen(url, timeout=3.0)
        cod = cod_page(f)
        fl = f.read().decode(cod, errors='ignore')
        if len(fl) < 10: raise IndexError
        return fl
    except:
        print('Page {0} temporally inaccessible!'.format(url))
        return None

def url_line(url):
    """Повертає веб-сторінку в строці з кодуванням utf-8"""
    try:
        #print(url)
        f = urllib.request.urlopen(url, timeout=3.0)
        cod = cod_page(f)
        fl = f.read().decode(cod)
        if len(fl) < 10: raise IndexError
        #"ISO-8859-1"
        #print('a',cod,url)
        return fl
    except:
        linef = requests.get(url).text
        return linef
        # linef = []
        # f = urllib.request.urlopen(url)
        # cod = cod_page(f)
        # for lf in f:
        #     try:
        #         linef.append(lf.decode(cod, errors='ignore'))
        #     except:
        #         continue
                #print('b',cod,url)
        # return ''.join(linef)

def url_line1251(url):
    """Повертає веб-сторінку в строці з кодуванням utf-8"""
    try:       
        f = urllib.request.urlopen(url, timeout=3.0)
        fl = f.read().decode('cp1251')        
        return fl
    except:
        linef = []
        f = urllib.request.urlopen(url)
        for lf in f:
            try:
                linef.append(lf.decode('cp1251', errors='ignore'))
            except:
                continue
        return ''.join(linef)

def coding_page(f):
    patern = re.compile(r'charset=([-\w\d]+)', re.IGNORECASE)
    chrset = patern.findall(f.info()['Content-Type'])
    if len(chrset) == 0:
        for line in f:
            chrset = patern.findall(str(line))


def cod_page(f):
    cod_p = re.findall(r'charset=([-\w\d]+)(?i)', f.info()['Content-Type'])
    if len(cod_p) == 0: return 'utf_8'
    ch = cod_p[0].lower().replace('-', '_')
    if ch in cdn.keys():
        return cdn[ch]
    if ch in cdn.values():
        return ch


def get_coding(url):
    patern = re.compile(r'charset=([-\w\d]+)', re.IGNORECASE)
    try:
        response = urllib.request.urlopen(url)
        chrset = patern.findall(response.info()['Content-Type'])
        if len(chrset) == 0:
            gl = 15
            for line in response:
                chrset = patern.findall(str(line))
                gl -= 1
                if gl == 0:
                    return 'utf_8'
                if len(chrset) != 0:
                    ch = chrset[0].lower().replace('-', '_')
                    if ch in cdn.keys():
                        return cdn[ch]
                    if ch in cdn.values():
                        return ch
            return 'utf_8'
        else:
            ch = chrset[0].lower().replace('-', '_')
            if ch in cdn.keys():
                return cdn[ch]
            if ch in cdn.values():
                return ch
    except:
        print('Помилка завантаження сторінки:\n', url)
        return None


def page_link(f_in, tofile=False):
    try:
        line = ''.join(open(f_in, 'r', encoding='utf_8'))
        line = re.sub(r'\n', '', line)
        line = re.sub(r'\s{2,}', ' ', line)
        patern = re.compile(r'<a .*?/a>', re.DOTALL)
        links = patern.findall(line)
        if tofile:
            f_out = f_in[:f_in.rfind('.')] + '_link' + f_in[f_in.rfind('.'):]
            with open(f_out, 'w', encoding='utf_8') as f:
                for l in links:
                    f.write(l + '\n')
        return links
    except:
        return None


def str_link(line):
    try:
        line = re.sub(r'\n', '', line)
        line = re.sub(r'\s{2,}', ' ', line)
        patern = re.compile(r'<a .*?/a>', re.DOTALL)
        links = patern.findall(line)
        return links
    except:
        return None


def get_ptag(line):
    try:
        line = re.sub(r'\n', '', line)
        line = re.sub(r'\s{2,}', ' ', line)
        line = re.sub(r'< ?/i ?>', '', line)
        line = re.sub(r'< ?i ?>', '', line)
        line = re.sub(r'< ?/em ?>', '', line)
        line = re.sub(r'< ?em ?>', '', line)
        line = re.sub(r'< ?/li ?>', '', line)
        line = re.sub(r'< ?li ?>', '', line)
        line = re.sub(r'< ?script.+?/ ?script ?>(?s)', '', line)
        line = re.sub(r'< ?style.+?/ ?style ?>(?s)', '', line)
        line = re.sub(r'<!--.+?-->(?s)', r'', line)
        line = re.sub(r'\n( |\t|\f|\r)*\n', '', line)
        line = re.sub(r'< ?img.*?>', '', line)
        line = re.sub(r'</a>', '', line)
        line = re.sub(r'<a .*?>', '', line)
        line = re.sub('&#8217;', "'", line)
        patern = re.compile(r'<p.*?/p>', re.DOTALL)
        ptn = re.compile(r'<.*?>')
        links = patern.findall(line)
        llll = []
        for s in links:
            w = ptn.split(s)
            if w[1]: llll.append(w[1])
        return llll
    except:
        return None


def tag_content(line):
    patern = re.compile(r'<.*?>')
    content = patern.split(line)
    rez = [x for x in content if len(x) > 0]
    return rez


def get_link(line):
    patern = re.compile(r'href=["\']?([-/\:_\.\w\d]+)["\']?')
    href = patern.findall(line)
    return href


def clear_span(line):
    #patern=re.compile(r'< ?span.+?/ ?span ?>',re.DOTALL)#жадный
    patern = re.compile(r'< ?span.+/ ?span ?>', re.DOTALL)#не жадный
    return patern.sub('', line)


def del_alltag(f_in):
    p = re.compile(r'<.*?>', re.DOTALL)
    f_out = f_in[:f_in.rfind('.')] + '_notag' + f_in[f_in.rfind('.'):]
    with open(f_out, 'w', encoding='utf_8') as f:
        line = ''.join(open(f_in, 'r', encoding='utf_8'))
        line = p.sub(' TAG ', line)
        f.write(line)
    return f_out


def grouping_words(allwords, dist_gr=3, len_gr=8):
    ls1 = enumerate(allwords)
    ls2 = [x for x in ls1 if x[1] != 'TAG']
    ##    with open('ert.txt','w',encoding='utf_8') as f:
    ##        for l in ls2:
    ##            f.write(str(l[0])+'-'+l[1]+'\n')
    rez = list()
    lst = list()
    for i in range(len(ls2)):
        if len(lst) == 0:
            if i != 0:
                lst.append(ls2[i - 1][1])
            lst.append(ls2[i][1])
            num = ls2[i][0]
            continue
        if ls2[i][0] - num < dist_gr:
            lst.append(ls2[i][1])
            num = ls2[i][0]
        else:
            if len(lst) >= len_gr:
                rez.append(' '.join(lst))
            lst = []
    return rez


if __name__ == '__main__':
    pass
    # ***********************************************************
    #p=re.compile(r'<w:t.*?>(.*?)</w:t>') Текст между тегами в MS Word
    # ***********************************************************


    # l='http://www.bbc.co.uk/ukrainian/news_in_brief/2013/04/130413_ek_lutsenko_crime.shtml'
    #l='http://www.itar-tass.com/c1/705938.html'
    l = 'http://news.meta.ua/'
    #l = 'http://www.unian.ua/news/565724-odesitam-vimknuli-opalennya.html'
    line = url_line(l)
    print(line)
    # dd = get_ptag(line)
    #l='/media/D6109B75109B5AF7/PYTHON/rezult/www_unian_net/pg1.html'
    #ddd=clean_html(l)
    #dd=grouping_words(ddd.split())
    # for ll in dd:
    #print(tag_content(ll))
    # print(ll)

    #page_link('txt_in.txt',tofile=True)
    #for line in open('new_link.txt','r',encoding='utf_8'):
    #    print(tag_content(line))
    #url='http://tass-online.ru'
    #print(get_coding(url))
    #clear_('txt_in.txt')
##    url='http://lenta.ru/news/2012/11/10/'
##    print(del_alltag(clear_('ff.txt')))


##    cod=get_coding(url)
##    print(cod)
##    f_in='news.txt'
##    opener = urllib.request.FancyURLopener({})
##    f = opener.open(url)
##    with open(f_in,'w',encoding='utf_8') as f1:
##        f1.write(f.read().decode(cod))
##    page_link(f_in,tofile=True)
#del_alltag(clear_(f_in))
#url='http://ru.tsn.ua/ukrayina/miliciya-uveryaet-chto-golodaet-lish-odin-dnepropetrovskiy-terrorist.html'
#url='http://korrespondent.net/ukraine/events/1410192-v-litve-doch-ukrainskogo-diplomata-sbila-peshehoda'
#url='http://lenta.ru/news/2012/10/19/deal/'
#url='http://lenta.ru/lib/14159943/'
#url='http://www.bbc.co.uk/ukrainian/news_in_brief/2012/10/121028_nk_udar_election.shtml'
#url='http://mobile.aukro.ua/listing.php/showcat?buy=1&change_view=1&id=47558&order=bd&view=gal&ap=1&aid=22297973&utm_source=ukr.net&utm_medium=advert&utm_campaign=link_mobile_market&utm_content=telefony'


#clear_('ssss.html')
#print(get_coding('ssss.html'))
#lll=get_link(url)
#g='<a href="http://www.bbc.co.uk/ukrainian/multimedia">Відео/Аудіо</a>'
#print(get_link(g))
#g='<a href="/ukrainian/multimedia/2012/11/121102_elephant_talks_it.shtml">Слон у Кореї заговорив людською мовою<span class="cta"><span>Проглянути</span><span class="duration">00:46</span></span></a>'
#print(clear_span(g))
#print(get_link(g))
#print(tag_content(clear_span(g)))
'''
    gl=15
    try:
        response = urllib.request.urlopen(url)
        chrset=patern.findall(response.info()['Content-Type'])
        if len(chrset)==0:
            for line in response:
                chrset=patern.findall(str(line))
                gl-=1
                if gl==0:
                    return None
                if len(chrset)!=0:
                    ch=chrset[0].lower().replace('-','_')
                if ch in cdn.keys():
                    return cdn[ch]
                if ch in cdn.values():
                    return ch
        else:
            return None
    except:
        if not os.path.exists(url):
            return None
        with open(url,'r',encoding='utf_8') as f:
            for line in f:
                gl-=1
                if gl==0:
                    return None
                chrset=patern.findall(str(line))
                if len(chrset)!=0:
                    ch=chrset[0].lower().replace('-','_')
                    if ch in cdn.keys():
                        return cdn[ch]
                    if ch in cdn.values():
                        return ch
            else:
                return None    '''
