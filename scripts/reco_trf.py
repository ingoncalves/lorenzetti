#!/usr/bin/env python3

from Gaugi.messenger    import LoggingLevel, Logger
from Gaugi              import GeV
from P8Kernel           import EventReader
from G4Kernel           import *

from CaloRec            import CaloClusterMaker
from CaloRingerBuilder  import *

import numpy as np
import argparse
import sys,os


mainLogger = Logger.getModuleLogger("job")
parser = argparse.ArgumentParser(description = '', add_help = False)
parser = argparse.ArgumentParser()


parser.add_argument('-i','--inputFile', action='store', dest='inputFile', required = False,
                    help = "The event input file generated by the Pythia event generator.")

parser.add_argument('-o','--outputFile', action='store', dest='outputFile', required = False,
                    help = "The reconstructed event file generated by lzt/geant4 framework.")

parser.add_argument('--outputLevel', action='store', dest='outputLevel', required = False, type=int, default=1,
                    help = "The output level messenger.")

parser.add_argument('-nt','--numberOfThreads', action='store', dest='numberOfThreads', required = False, type=int, default=1,
                    help = "The number of threads")

parser.add_argument('--evt','--numberOfEvents', action='store', dest='numberOfEvents', required = False, type=int, default=None,
                    help = "The number of events to apply the reconstruction.")

parser.add_argument('--visualization', action='store_true', dest='visualization', required = False,
                    help = "Run with Qt interface.")

parser.add_argument('-n', '--ntuple', action='store', dest='ntuple',required = False, default = 'physics',
                    help = "Choose the ntuple schemma: raw (energy estimation studies) or physics (physics studies)")



if len(sys.argv)==1:
  parser.print_help()
  sys.exit(1)

args = parser.parse_args()


# Get all output names
if not '.root' in args.outputFile:
  args.outputFile+='.root'

# Add index for each thread
outputFileList = []
for thread in range( args.numberOfThreads ):
  outputFileList.append( args.outputFile.replace( '.root', "_%d.root"%thread ) )



from DetectorATLASModel import DetectorConstruction as ATLAS
from DetectorATLASModel import CaloCellBuilder



acc = ComponentAccumulator("ComponentAccumulator",
                            ATLAS("GenericATLASDetector"),
                            RunVis=args.visualization,
                            NumberOfThreads = args.numberOfThreads,
                            OutputFile = args.outputFile)


gun = EventReader( "PythiaGenerator",
                   EventKey   = recordable("EventInfo"),
                   FileName   = args.inputFile)



calorimeter = CaloCellBuilder("CaloCellATLASBuilder",
                              HistogramPath = "Expert/CaloCells",
                              OutputLevel   = args.outputLevel)



cluster = CaloClusterMaker( "CaloClusterMaker",
                            CellsKey        = recordable("Cells"),
                            EventKey        = recordable("EventInfo"),
                            ClusterKey      = recordable("Clusters"),
                            TruthKey        = recordable("Particles"),
                            EtaWindow       = 0.4,
                            PhiWindow       = 0.4,
                            MinCenterEnergy = 15*GeV,
                            HistogramPath   = "Expert/Clusters",
                            OutputLevel     = args.outputLevel)


truth_cluster = CaloClusterMaker( "TruthCaloClusterMaker",
                            CellsKey        = recordable("TruthCells"),
                            EventKey        = recordable("EventInfo"),
                            ClusterKey      = recordable("TruthClusters"),
                            TruthKey        = recordable("TruthParticles"),
                            EtaWindow       = 0.4,
                            PhiWindow       = 0.4,
                            MinCenterEnergy = 15*GeV,
                            HistogramPath   = "Expert/TruthClusters",
                            OutputLevel     = args.outputLevel)




pi = np.pi
ringer = CaloRingerBuilder( "CaloRingerBuilder",
                            RingerKey     = recordable("Rings"),
                            ClusterKey    = recordable("Clusters"),
                            DeltaEtaRings = [0.00325, 0.025, 0.050, 0.1, 0.1, 0.2 ],
                            DeltaPhiRings = [pi/32, pi/128, pi/128, pi/128, pi/32, pi/32, pi/32],
                            NRings        = [64, 8, 8, 4, 4, 4],
                            LayerRings    = [1,2,3,4,5,6],
                            HistogramPath = "Expert/Ringer",
                            OutputLevel   = args.outputLevel)


truth_ringer = CaloRingerBuilder( "TruthCaloRingerBuilder",
                                  RingerKey       = recordable("TruthRings"),
                                  ClusterKey      = recordable("TruthClusters"),
                                  DeltaEtaRings   = [0.00325, 0.025, 0.050, 0.1, 0.1, 0.2 ],
                                  DeltaPhiRings   = [pi/32, pi/128, pi/128, pi/128, pi/32, pi/32, pi/32],
                                  NRings          = [64, 8, 8, 4, 4, 4],
                                  LayerRings      = [1,2,3,4,5,6],
                                  HistogramPath   = "Expert/TruthRinger",
                                  OutputLevel     = args.outputLevel)




if args.ntuple == 'physics':

    from CaloRec import CaloNtupleMaker
    ntuple = CaloNtupleMaker( "CaloNtupleMaker",
                              EventKey        = recordable("EventInfo"),
                              RingerKey       = recordable("Rings"),
                              TruthRingerKey  = recordable("TruthRings"),
                              ClusterKey      = recordable("Clusters"),
                              TruthClusterKey = recordable("TruthClusters"),
                              DeltaR          = 0.15,
                              DumpCells       = True,
                              OutputLevel     = args.outputLevel)

elif args.ntuple == 'raw':

    from CaloRec import RawNtupleMaker
    ntuple = RawNtupleMaker (  "RawNtupleMaker",
                               EventKey        = recordable("EventInfo"),
                               CellsKey        = recordable("Cells"),
                               EtaWindow       = 0.4,
                               PhiWindow       = 0.4,
                               OutputLevel     = args.outputLevel)

else:
    mainLogger.fatal('Invalid ntuple tuple. Choose between raw or physics.')


gun.merge(acc)
calorimeter.merge(acc)
acc+= cluster
acc+= truth_cluster
acc+= ringer
acc+= truth_ringer
acc += ntuple

acc.run(args.numberOfEvents)



# Merge all files
command = "hadd -f " + args.outputFile + ' '
for fname in outputFileList:
  command+=fname + ' '
print( command )
os.system(command)

# remove thread files
for fname in outputFileList:
  os.system( 'rm '+ fname )





