import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")
# Message logger service
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, "auto:phase1_2021_design")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

process.source = cms.Source("EmptySource")

import Geometry.DTGeometryBuilder.dtGeometryDB_cfi
process.DTGeometryMuonMisalignedProducer = Geometry.DTGeometryBuilder.dtGeometryDB_cfi.DTGeometryESModule.clone()
process.DTGeometryMuonMisalignedProducer.appendToDataLabel = 'idealForMuonMisalignedProducer'
process.DTGeometryMuonMisalignedProducer.applyAlignment = cms.bool(False)
import Geometry.CSCGeometryBuilder.cscGeometryDB_cfi
process.CSCGeometryMuonMisalignedProducer = Geometry.CSCGeometryBuilder.cscGeometryDB_cfi.CSCGeometryESModule.clone()
process.CSCGeometryMuonMisalignedProducer.appendToDataLabel = 'idealForMuonMisalignedProducer'
process.CSCGeometryMuonMisalignedProducer.applyAlignment = cms.bool(False)
import Geometry.GEMGeometryBuilder.gemGeometryDB_cfi
process.GEMGeometryMuonMisalignedProducer = Geometry.GEMGeometryBuilder.gemGeometryDB_cfi.GEMGeometryESModule.clone()
process.GEMGeometryMuonMisalignedProducer.appendToDataLabel = 'idealForMuonMisalignedProducer'
process.GEMGeometryMuonMisalignedProducer.applyAlignment = cms.bool(False)

process.GEMAlDBWriter = cms.EDAnalyzer("GEMAlDBWriter",
                                       doChamber = cms.untracked.bool(False),
                                       doEndcap = cms.untracked.bool(False),
                                       doME11Chamber = cms.untracked.bool(True),
                                       doCSCEndcap = cms.untracked.bool(False),
                                       chamberFile = cms.untracked.string('gemAl.csv'),
                                       endcapFile = cms.untracked.string('GEMRing.csv')
                                       ME11ChamberFile = cms.untracked.string('cscAl.csv'),
                                       CSCEndcapFile = cms.untracked.string('cscEndcap.csv')
                                      )

# Database output service if you want to store soemthing in MisalignedMuon
from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    CondDBSetup,
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('DTAlignmentRcd'),
        tag = cms.string('DTAlignmentRcd')
    ),
        cms.PSet(
            record = cms.string('DTAlignmentErrorExtendedRcd'),
            tag = cms.string('DTAlignmentErrorExtendedRcd')
        ),
        cms.PSet(
            record = cms.string('CSCAlignmentRcd'),
            tag = cms.string('CSCAlignmentRcd')
        ),
        cms.PSet(
            record = cms.string('CSCAlignmentErrorExtendedRcd'),
            tag = cms.string('CSCAlignmentErrorExtendedRcd')
        ),
        cms.PSet(
            record = cms.string('GEMAlignmentRcd'),
            tag = cms.string('GEMAlignmentRcd')
        ),
        cms.PSet(
            record = cms.string('GEMAlignmentErrorExtendedRcd'),
            tag = cms.string('GEMAlignmentErrorExtendedRcd')
        )),

    connect = cms.string('sqlite_file:GEMAl.db')
)
process.p1 = cms.Path(process.GEMAlDBWriter)
process.MessageLogger.cout = cms.untracked.PSet(
    threshold = cms.untracked.string('INFO'),
    default = cms.untracked.PSet(
        limit = cms.untracked.int32(10000000)
    )
)


