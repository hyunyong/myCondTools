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
  return rawId, iEta, iStrip + iPhi*maxChNum

sCurvesFileName = "minus_20211029.csv"
sCurves = csv.reader(open(sCurvesFileName))
outCSV = open(sCurvesFileName.replace(".csv", "_reprocess.csv"),'w')
wr = csv.writer(outCSV)
outL = []
for i in sCurves:
  if i[0].startswith("detName"): 
    wr.writerow(i) 
    continue
  detTmp = i[0].split("-")
  strip = getStrip(-1 if detTmp[1] == "M" else 1, 1, int(detTmp[2].split("L")[0]), int(detTmp[2].split("L")[1]), int(float(i[1])), float(i[2]))
  outL.append([i[0], i[1], i[2], strip[2], i[4], i[5]])

for i in outL:
  wr.writerow(i)
outCSV.close()
