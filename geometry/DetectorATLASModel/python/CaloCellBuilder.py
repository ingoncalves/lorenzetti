
__all__ = ["CaloCellBuilder"]

from Gaugi import Logger
from Gaugi.macros import *
from G4Kernel import treatPropertyValue, recordable
import os


#
# Calo cell builder
#
class CaloCellBuilder( Logger ):


  # basepath
  __basepath = os.environ['LZT_PATH']+'/geometry/DetectorATLASModel/data/'


  def __init__( self, name, 
                      HistogramPath  = "Expert", 
                      HitsKey = "Hits",
                      OutputLevel    = 1,
                      ):

    Logger.__init__(self)
    self.__recoAlgs = []
    self.__histpath = HistogramPath
    self.__outputLevel = OutputLevel
    self.__hitsKey = HitsKey
    
    # configure
    self.configure()



  #
  # Configure 
  #
  def configure(self):

    MSG_INFO(self, "Configure CaloCellBuilder.")

    from CaloCellBuilder import CaloCellMaker, CaloCellMerge, CaloPulseShapeMaker, PulseGenerator, OptimalFilter

    collectionKeys = []
 
    # Get the layer cell configuration
    from DetectorATLASModel import create_ATLAS_layers 
    layers = create_ATLAS_layers(self.__basepath)
    

    for layer_id, layer in enumerate( layers ):

      for sampling in layer:

        for seg in sampling.segments:

          MSG_INFO(self, "Create new CaloCellMaker and dump all cells into %s collection", seg.CollectionKey)

          pulse_shape = CaloPulseShapeMaker( "CaloPulseShapeMaker",
                                             ShaperFile      = seg.ShaperFile,
                                             OutputLevel     = self.__outputLevel,
                                           )

          pulse = PulseGenerator( "PulseGenerator", 
                                  NSamples        = seg.NSamples, 
                                  OutputLevel     = self.__outputLevel,
                                  SamplingRate    = 25.0,
                                  Pedestal        = 0.0,
                                  DeformationMean = 0.0, 
                                  DeformationStd  = 0.0,
                                  NoiseMean       = 0.0,
                                  NoiseStd        = seg.EletronicNoise,
                                  StartSamplingBC = seg.StartSamplingBC, 
                                )

          of = OptimalFilter("OptimalFilter",
                              Weights  = seg.OFWeights,
                              OutputLevel=self.__outputLevel)


          alg = CaloCellMaker("CaloCellMaker", 
                              # input key
                              EventKey                = recordable( "EventInfo" ), 
                              HitsKey                 = recordable( self.__hitsKey ),
                              # output key
                              CollectionKey           = seg.CollectionKey, 
                              # Hits grid configuration
                              EtaBins                 = seg.EtaBins,
                              PhiBins                 = seg.PhiBins,
                              RMin                    = seg.RMin,
                              RMax                    = seg.RMax,
                              Sampling                = seg.Sampling,
                              Segment                 = seg.Segment,
                              Detector                = seg.Detector,
                              # Bunch crossing configuration
                              BunchIdStart            = seg.BunchIdStart,
                              BunchIdEnd              = seg.BunchIdEnd,
                              BunchDuration           = 25, #ns
                              # monitoring configuration
                              HistogramPath           = self.__histpath + '/' + seg.name,
                              OutputLevel             = self.__outputLevel,
                              DetailedHistograms      = False, # Use True when debug with only one thread
                              )


          alg.Tools = [pulse_shape, pulse, of]
          self.__recoAlgs.append( alg )
          collectionKeys.append( seg.CollectionKey )


    MSG_INFO(self, "Create CaloCellMerge and dump all cell collections into %s container", "Cells")
    # Merge all collection into a container and split between truth and reco
    mergeAlg = CaloCellMerge( "CaloCellMerge" , 
                              CollectionKeys  = collectionKeys,
                              CellsKey        = recordable("Cells"),
                              TruthCellsKey   = recordable("TruthCells"),
                              OutputLevel     = self.__outputLevel )

    self.__recoAlgs.append( mergeAlg )



  def merge( self, acc ):
    for reco in self.__recoAlgs:
      acc+=reco 















