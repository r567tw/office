import os
import urllib.request
import csv

zoom='17'
size='640x400'
markers='color:red|'
datafile='example.csv'

demand='&zoom='+zoom+'&size='+size+'&markers='+markers

head_url='https://maps.googleapis.com/maps/api/staticmap'
dname='google_map'


if (not os.path.exists(dname)):
    os.mkdir(dname)

f = open(datafile, 'r', encoding = 'utf8')

for row in csv.DictReader(f,['代號','地址']):
    fname=row['代號']+'.jpg'
    place=urllib.parse.quote(row['地址'])
    try:
        img_url=head_url+'?center='+place+demand+place
        urllib.request.urlretrieve(img_url, os.path.join(dname, fname))
        print(row['地址']+'已生成google map地圖')
    except:
        print(row['地址']+'找不到')

f.close()

