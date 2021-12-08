
__all__ = ["create_ATLAS_layers"]

from DetectorATLASModel import CaloSamplingMaker
import json


#
# ATLAS detector cell configuration
#
def create_ATLAS_layers( basepath ):

  cells = json.load(open(basepath + '/atlas_granularity.json', 'r'))

  psb = CaloSamplingMaker( "PSB", "Collection_PSB", cells["PSB"],
                    # layer configuration
                    ShaperFile      = basepath + "/pulseLar.dat",
                    BunchIdStart    = -21, # -525ns
                    BunchIdEnd      = 3, # +75ns
                    StartSamplingBC = -2, 
                    NSamples        = 5,
                    EletronicNoise  = 90, # MeV
                    UseOF2          = False,
                    #OFCalibrationFile = basepath+"/noise-dataset-lar.dat",
                    #OFWeights       = [-0.0000853580,    0.265132,    0.594162,     0.389505,     0.124353],
                    )

  pse = CaloSamplingMaker( "PSE", "Collection_PSE", cells['PSE'],
                    # layer configuration
                    ShaperFile      = basepath+"/pulseLar.dat",
                    BunchIdStart    = -21, # -525ns
                    BunchIdEnd      = 3, # +75ns
                    StartSamplingBC = -2, 
                    NSamples        = 5,
                    EletronicNoise  = 90, # MeV
                    UseOF2          = False,
                    #OFCalibrationFile = basepath+"/noise-dataset-lar.dat",
                    #OFWeights       = [-0.0000853580,    0.265132,    0.594162,     0.389505,     0.124353],
                    )
  
  emb1 =CaloSamplingMaker( "EMB1", "Collection_EMB1", cells['EMB1'],
                    # layer configuration
                    ShaperFile      = basepath+"/pulseLar.dat",
                    BunchIdStart    = -21, # -525ns
                    BunchIdEnd      = 3, # +75ns
                    StartSamplingBC = -2, 
                    NSamples        = 5,
                    EletronicNoise  = 26, # MeV
                    UseOF2          = False,
                    #OFCalibrationFile = basepath+"/noise-dataset-lar.dat",
                    #OFWeights       = [-0.0000853580,    0.265132,    0.594162,     0.389505,     0.124353],
                    )
  
  emb2 =CaloSamplingMaker( "EMB2", "Collection_EMB2", cells['EMB2'],
                    # layer configuration
                    ShaperFile      = basepath+"/pulseLar.dat",
                    BunchIdStart    = -21, # -525ns
                    BunchIdEnd      = 3, # +75ns
                    StartSamplingBC = -2, 
                    NSamples        = 5,
                    EletronicNoise  = 60, # MeV
                    UseOF2          = False,
                    #OFCalibrationFile = basepath+"/noise-dataset-lar.dat",
                    #OFWeights       = [-0.0000853580,    0.265132,    0.594162,     0.389505,     0.124353],
                    )
  
  emb3 =CaloSamplingMaker( "EMB3", "Collection_EMB3", cells['EMB3'],
                    ShaperFile      = basepath+"/pulseLar.dat",
                    BunchIdStart    = -21, # -525ns
                    BunchIdEnd      = 3, # +75ns
                    StartSamplingBC = -2, 
                    NSamples        = 5,
                    EletronicNoise  = 40, # MeV
                    UseOF2          = False,
                    #OFCalibrationFile = basepath+"/noise-dataset-lar.dat",
                    #OFWeights       = [-0.0000853580,    0.265132,    0.594162,     0.389505,     0.124353],
                    )
  
  tilecal1 = CaloSamplingMaker( "TileCal1", "Collection_TileCal1", cells['TileCal1'],
                    ShaperFile      = basepath+"/pulseTile.dat",
                    BunchIdStart    = -6, # -150ns
                    BunchIdEnd      = 4, # +100ns
                    StartSamplingBC = -3, 
                    NSamples        = 7,
                    EletronicNoise  = 20, # MeV
                    UseOF2          = True,
                    #OFCalibrationFile = basepath+"/noise-dataset-tile.dat",
                    #OFWeights       =  [-0.3781,   -0.3572,    0.1808,    0.8125,   0.2767,    -0.2056,    -0.3292]
                    )
  
  tilecal2 = CaloSamplingMaker( "TileCal2", "Collection_TileCal2", cells['TileCal2'],
                    ShaperFile      = basepath+"/pulseTile.dat",
                    BunchIdStart    = -6, # -150ns
                    BunchIdEnd      = 4, # +100ns
                    StartSamplingBC = -3, 
                    NSamples        = 7,
                    EletronicNoise  = 20, # MeV
                    UseOF2          = True,
                    #OFCalibrationFile = basepath+"/noise-dataset-tile.dat",
                    #OFWeights       =  [-0.3781,   -0.3572,    0.1808,    0.8125,   0.2767,    -0.2056,    -0.3292]
                    )
  
  tilecal3 = CaloSamplingMaker( "TileCal3", "Collection_TileCal3", cells['TileCal3'],
                    ShaperFile      = basepath+"/pulseTile.dat",
                    BunchIdStart    = -6, # -150ns
                    BunchIdEnd      = 4, # +100ns
                    StartSamplingBC = -3, 
                    NSamples        = 7,
                    EletronicNoise  = 20, # MeV
                    UseOF2          = True,
                    #OFCalibrationFile = basepath+"/noise-dataset-tile.dat",
                    #OFWeights       =  [-0.3781,   -0.3572,    0.1808,    0.8125,   0.2767,    -0.2056,    -0.3292]
                    )
  
  tilecalExt1 = CaloSamplingMaker( "TileExt1", "Collection_TileExt1", cells['TileExt1'],
                    ShaperFile      = basepath+"/pulseTile.dat",
                    BunchIdStart    = -6, # -150ns
                    BunchIdEnd      = 4, # +100ns
                    StartSamplingBC = -3, 
                    NSamples        = 7,
                    EletronicNoise  = 20, # MeV
                    UseOF2          = True,
                    #OFCalibrationFile = basepath+"/noise-dataset-tile.dat",
                    #OFWeights       =  [-0.3781,   -0.3572,    0.1808,    0.8125,   0.2767,    -0.2056,    -0.3292]
                    )
  
  tilecalExt2 = CaloSamplingMaker( "TileExt2", "Collection_TileExt2", cells['TileExt2'],
                    ShaperFile      = basepath+"/pulseTile.dat",
                    BunchIdStart    = -6, # -150ns
                    BunchIdEnd      = 4, # +100ns
                    StartSamplingBC = -3, 
                    NSamples        = 7,
                    EletronicNoise  = 20, # MeV
                    UseOF2          = True,
                    #OFCalibrationFile = basepath+"/noise-dataset-tile.dat",
                    #OFWeights       =  [-0.3781,   -0.3572,    0.1808,    0.8125,   0.2767,    -0.2056,    -0.3292]
                    )
  
  tilecalExt3 = CaloSamplingMaker( "TileExt3", "Collection_TileExt3", cells['TileExt3'],
                    ShaperFile      = basepath+"/pulseTile.dat",
                    BunchIdStart    = -6, # -150ns
                    BunchIdEnd      = 4, # +100ns
                    StartSamplingBC = -3, 
                    NSamples        = 7,
                    EletronicNoise  = 20, # MeV
                    UseOF2          = True,
                    #OFCalibrationFile = basepath+"/noise-dataset-tile.dat",
                    #OFWeights       =  [-0.3781,   -0.3572,    0.1808,    0.8125,   0.2767,    -0.2056,    -0.3292]
                    )
  
  emec1 = CaloSamplingMaker( "EMEC1", "Collection_EMEC1", cells['EMEC1'],
                    ShaperFile      = basepath+"/pulseLar.dat",
                    BunchIdStart    = -21, # -525ns
                    BunchIdEnd      = 3, # +75ns
                    StartSamplingBC = -2, 
                    NSamples        = 5,
                    EletronicNoise  = 26, # MeV
                    UseOF2          = False,
                    #OFCalibrationFile = basepath+"/noise-dataset-lar.dat",
                    #OFWeights       = [-0.0000853580,    0.265132,    0.594162,     0.389505,     0.124353],
                    )
  
  emec2 = CaloSamplingMaker( "EMEC2", "Collection_EMEC2", cells['EMEC2'],
                    ShaperFile      = basepath+"/pulseLar.dat",
                    BunchIdStart    = -21, # -525ns
                    BunchIdEnd      = 3, # +75ns
                    StartSamplingBC = -2, 
                    NSamples        = 5,
                    EletronicNoise  = 60, # MeV
                    UseOF2          = False,
                    #OFCalibrationFile = basepath+"/noise-dataset-lar.dat",
                    #OFWeights       = [-0.0000853580,    0.265132,    0.594162,     0.389505,     0.124353],
                    )
  
  emec3 = CaloSamplingMaker( "EMEC3", "Collection_EMEC3", cells['EMEC3'],
                    ShaperFile      = basepath+"/pulseLar.dat",
                    BunchIdStart    = -21, # -525ns
                    BunchIdEnd      = 3, # +75ns
                    StartSamplingBC = -2, 
                    NSamples        = 5,
                    EletronicNoise  = 40, # MeV
                    UseOF2          = False,
                    #OFCalibrationFile = basepath+"/noise-dataset-lar.dat",
                    #OFWeights       = [-0.0000853580,    0.265132,    0.594162,     0.389505,     0.124353],
                    )
  
  hec1 = CaloSamplingMaker( "HEC1", "Collection_HEC1", cells['HEC1'],
                    # layer configuration
                    ShaperFile      = basepath+"/pulseLar.dat",
                    BunchIdStart    = -21, # -525ns
                    BunchIdEnd      = 3, # +75ns
                    StartSamplingBC = -2, 
                    NSamples        = 5,
                    EletronicNoise  = 250, # MeV
                    UseOF2          = False,
                    #OFCalibrationFile = basepath+"/noise-dataset-lar.dat",
                    #OFWeights       = [-0.0000853580,    0.265132,    0.594162,     0.389505,     0.124353],
                    )
 

  hec2 = CaloSamplingMaker( "HEC2", "Collection_HEC2", cells['HEC2'],
                    # layer configuration
                    ShaperFile      = basepath+"/pulseLar.dat",
                    BunchIdStart    = -21, # -525ns
                    BunchIdEnd      = 3, # +75ns
                    StartSamplingBC = -2, 
                    NSamples        = 5,
                    EletronicNoise  = 400, # MeV
                    UseOF2          = False,
                    #OFCalibrationFile = basepath+"/noise-dataset-lar.dat",
                    #OFWeights       = [-0.0000853580,    0.265132,    0.594162,     0.389505,     0.124353],
                    )
 


  hec3 = CaloSamplingMaker( "HEC3", "Collection_HEC3", cells['HEC3'],
                    # layer configuration
                    ShaperFile      = basepath+"/pulseLar.dat",
                    BunchIdStart    = -21, # -525ns
                    BunchIdEnd      = 3, # +75ns
                    StartSamplingBC = -2, 
                    NSamples        = 5,
                    EletronicNoise  = 750, # MeV
                    UseOF2          = False,
                    #OFCalibrationFile = basepath+"/noise-dataset-lar.dat",
                    #OFWeights       = [-0.0000853580,    0.265132,    0.594162,     0.389505,     0.124353],
                    )
  #
  # ATLAS layer map
  #
  layers = [    
      [ psb,  pse ], # PS=0, ECal=0
      [ emb1, emec1 ], # EM1=1, ECal=0
      [ emb2, emec2 ], # EM2=2, ECal=0
      [ emb3, emec3 ], # EM3=3, ECal=0
      [ tilecal1, tilecalExt1, hec1 ], # HAD1=4, HCal=1
      [ tilecal2, tilecalExt2, hec2 ], # HAD2=5, HCal=1
      [ tilecal3, tilecalExt3, hec3 ], # HAD3=6, HCal=1
     ] 
  return layers

