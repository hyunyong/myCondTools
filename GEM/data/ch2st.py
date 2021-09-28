import csv

chMap_ = csv.reader(open("HV3bV3ChMapFull.csv"))
vfatMap_ = csv.reader(open("vfatTypeListFull.csv"))
rawIdMap_ = open("rawId.txt")
maxChNum = 128

chStMap = {}
rawIdMap = {}
vfatMap = {}

for i in rawIdMap_:
  tmprawId = int(i.split(',')[0])
  tmpId = i.split(',')[1].split()
  tmpregion = int(tmpId[1])
  tmpstation = 1
  tmpchmaber = int(tmpId[9])
  tmplayer = int(tmpId[7])
  tmpeta = int(tmpId[-1])
  rawIdMap[tmpregion, tmpstation, tmpchmaber, tmplayer, tmpeta] = tmprawId

for i in chMap_:
  if int(i[0]) > 20:
    tmptype = int(i[0])
    tmpst = int(i[1])
    tmpch = int(i[2])
    chStMap[tmptype, tmpch] = tmpst

for i in vfatMap_:
  if (int(i[0]) > 20) and (int(i[3]) == 1):
    tmptype = int(i[0])
    tmpregion = int(i[2])
    tmpstation = 1
    tmplayer = int(i[4])
    tmpchmaber = int(i[5])
    tmpeta = int(i[6])
    tmpphi = int(i[7])
    tmpvfat = int(i[8])
    vfatMap[tmpregion, tmpstation, tmpchmaber, tmplayer, tmpvfat] = [tmptype, tmpeta, tmpphi]

def getStrip(region, station, chamber, layer, vfatAdd, channel):
  vfatType, iEta, iPhi = vfatMap[region, station, chamber, layer, vfatAdd]
  iStrip = chStMap[vfatType, channel]
  rawId = rawIdMap[region, station, chamber, layer, iEta]
  return rawId, iStrip + iPhi*maxChNum
 
print(getStrip(1,1,1,1,23,18)) 
