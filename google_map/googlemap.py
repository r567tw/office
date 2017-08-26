import os
import urllib.request
import csv

head_url='https://maps.googleapis.com/maps/api/staticmap'
dname='google_map'

if (not os.path.exists(dname)):
    os.mkdir(dname)

f = open('example.csv', 'r', encoding = 'utf8')

for row in csv.DictReader(f,['代號','地址']):
    fname=row['代號']+'.jpg'
    place=urllib.parse.quote(row['地址'])
    img_url=head_url+'?center='+place+'&zoom=17&size=640x400&markers=color:red|'+place
    urllib.request.urlretrieve(img_url, os.path.join(dname, fname))

f.close()

