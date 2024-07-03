#!/usr/bin/env python3

from GaugiKernel import LoggingLevel, Logger
from GaugiKernel import GeV
import argparse
import sys,os,traceback


mainLogger = Logger.getModuleLogger("zee")
parser = argparse.ArgumentParser(description = '', add_help = False)
parser = argparse.ArgumentParser()

#
# Mandatory arguments
#

parser.add_argument('--nov','--numberOfEvents', action='store', dest='numberOfEvents', 
                    required = False, type=int, default=1,
                    help = "The number of events to be generated.")

parser.add_argument('--eventNumber', action='store', dest='eventNumber', 
                    required = False, default=0, type=int,
                    help = "The list of numbers per event.")

parser.add_argument('--runNumber', action='store', dest='runNumber', 
                    required = False, type=int, default = 0,
                    help = "The run number.")

parser.add_argument('-o','--outputFile', action='store', dest='outputFile', required = True,
                    help = "The event file generated by pythia.")

parser.add_argument('--eta_max', action='store', dest='eta_max', required = False, type=float, default=3.2,
                    help = "The eta max used in generator.")

#
# Pileup simulation arguments
#

parser.add_argument('--pileupAvg', action='store', dest='pileupAvg', required = False, type=int, default=0,
                    help = "The pileup average (default is zero).")

parser.add_argument('--pileupSigma', action='store', dest='pileupSigma', required = False, type=int, default=0,
                    help = "The pileup sigma (default is zero).")

parser.add_argument('--bc_id_start', action='store', dest='bc_id_start', required = False, type=int, default=-21,
                    help = "The bunch crossing id start.")

parser.add_argument('--bc_id_end', action='store', dest='bc_id_end', required = False, type=int, default=4,
                    help = "The bunch crossing id end.")

parser.add_argument('--bc_duration', action='store', dest='bc_duration', required = False, type=int, default=25,
                    help = "The bunch crossing duration (in nanoseconds).")


#
# Extra parameters
#

parser.add_argument('--outputLevel', action='store', dest='outputLevel', required = False, type=int, default=0,
                    help = "The output level messenger.")

parser.add_argument('-s','--seed', action='store', dest='seed', required = False, type=int, default=0,
                    help = "The pythia seed (zero is the clock system)")

parser.add_argument('--forceForwardElectron', action='store_true', dest='forceForwardElectron',required = False, 
                    help = "Force at least one electron into forward region.")

#
# Calibration parameters
#
parser.add_argument('--zeroVertexParticles', action='store_true', dest='zeroVertexParticles',required = False, 
                    help = "Fix the z vertex position in simulation to zero for all selected particles. It is applied only at G4 step, not in generation.")



if len(sys.argv)==1:
  parser.print_help()
  sys.exit(1)

args = parser.parse_args()


try:
  
  
  from evtgen import Pythia8 
  from filters import Zee
  from GenKernel import EventTape

  tape = EventTape( "EventTape", OutputFile = args.outputFile, RunNumber = args.runNumber)
  
  main_file = os.environ['LZT_PATH']+'/generator/evtgen/data/zee_config.cmnd'

  zee = Zee( "Zee", 
            Pythia8("Generator", 
                    File=main_file, 
                    Seed=args.seed, 
                    EventNumber = args.eventNumber),
            EtaMax              = args.eta_max,
            MinPt               = 15*GeV,
            ZeroVertexParticles = args.zeroVertexParticles, #calibration use only.
            ForceForwardElectron = args.forceForwardElectron,
            OutputLevel  = args.outputLevel
           )
  tape+=zee

  if args.pileupAvg > 0:

    mb_file   = os.environ['LZT_PATH']+'/generator/evtgen/data/minbias_config.cmnd'

    from filters import Pileup
    pileup = Pileup("Pileup",
                   Pythia8("MBGenerator", File=mb_file, Seed=args.seed),
                   EtaMax         = args.eta_max,
                   Select         = 2,
                   PileupAvg      = args.pileupAvg,
                   PileupSigma    = args.pileupSigma,
                   BunchIdStart   = args.bc_id_start,
                   BunchIdEnd     = args.bc_id_end,
                   OutputLevel    = args.outputLevel,
                   DeltaEta       = 0.22,
                   DeltaPhi       = 0.22,
                  )

    tape+=pileup
  
  # Run!
  tape.run(args.numberOfEvents)

  sys.exit(0)
except  Exception as e:
  traceback.print_exc()
  mainLogger.error(e)
  sys.exit(1)