

title = ['123','31']
position = [['49.89','32.625083'],['49.158140','32.925083']]
label = ['A','B']
key = 'AIzaSyCOZ0t8PvYAnCPM5s6ZCiOngYr25C_oUy4'

class mymap:
    def __init__(self,date,key):
        self.date = date
        self.key =key
        self.f = open('mymap.html', 'w')
        self.f.write('''
<!DOCTYPE html>
<html>
    <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Marker Clustering</title>
        <style> #map { height: 100%; } 
                html, body {height: 100%;margin: 0;padding: 0;} 
        </style>
    </head>
    <body>
        <div id="map">
        </div>
        <script>
            function initMap() {
            var map = new google.maps.Map(document.getElementById('map'), {zoom: 6,center: {lat: 49.000000, lng: 32.000000}});
            var markers = locations.map(function(location, i) {return new google.maps.Marker({title: title[i % title.length],position: location,label: who[i % who.length]});});
            var markerCluster = new MarkerClusterer(map, markers,{imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});}      
        ''')
        self.claster()

    def claster(self):
        inf = []
        for i in range(len(self.date)):
            if len(self.date[i]) == 4:
                inf.append(self.date[i])
        who,title,loc= '','',''
        # for j in range(len(inf)):
        #     inf[j][0]
        import random
        for  i in range(len(inf)):
            r = random.randrange(0,100,1)
            r /= 10000
            lat = float(inf[i][2]) +r
            lng = float(inf[i][3]) +r
            who +='"{0}",'.format(inf[i][0])
            title+= '"{0}",'.format(str(inf[i][1]).replace('"',''))
            loc += "{"+'lat: {0}, lng: {1}'.format(lat,lng)+'},'



        self.f.write('\tvar who = [' + who + ']')
        self.f.write('\n\t\t\tvar title = [' + title+ ']')
        # pos = ["{ lat: " + ', lng: '.join(self.date[i][2]) + "}" for i in range(self.position.__len__())]
        # pos = "{ lat: {0}, lng: {1} },".format(self.date[i][2],self.date[i][3])
        self.f.write("\n\t\t\tvar locations = [" + loc + ']')
        self.f.write(
                '\n\t\t</script><script src="https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js"></script>')
        k = '\n\t\t<script async defer src="https://maps.googleapis.com/maps/api/js?key=' + self.key + '&callback=initMap"></script></body></html>'
        self.f.write(k)


if __name__ == '__main__':
    m = mymap(title,key)