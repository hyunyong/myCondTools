#include "CondCore/PopCon/interface/PopConAnalyzer.h"
#include "myCondTools/GEM/interface/GEMMaskedStripSourceHandler.h"
#include "FWCore/Framework/interface/MakerMacros.h"

typedef popcon::PopConAnalyzer<popcon::GEMMaskedStripSourceHandler> GEMMaskedStripDBWriter;
//define this as a plug-in
DEFINE_FWK_MODULE(GEMMaskedStripDBWriter);
