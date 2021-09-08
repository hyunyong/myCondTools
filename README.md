# myCondTools
- GEMeMap
```
cmsrel CMSSW_12_1_0_pre2
cd CMSSW_12_1_0_pre2/src
git clone git@github.com:hyunyong/myCondTools.git
cmsenv 
scram b -j12
cd myCondTools/GEM/test
cmsRun writeGEMEMap2DB.py
```
- GEM Alignment DB
```
cmsrel CMSSW_12_1_0_pre2
cd CMSSW_12_1_0_pre2/src
git clone git@github.com:hyunyong/myCondTools.git
cmsenv 
scram b -j12
cd myCondTools/GEM/test
cmsRun GEMAlDBWriter_cfg.py
```

