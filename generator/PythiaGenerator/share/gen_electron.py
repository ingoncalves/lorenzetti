#!/usr/bin/env python3
from Gaugi.messenger    import LoggingLevel, Logger
from Gaugi              import GeV
import argparse
import sys,os


mainLogger = Logger.getModuleLogger("pythia")
parser = argparse.ArgumentParser(description = '', add_help = False)
parser = argparse.ArgumentParser()

#
# Mandatory arguments
#


parser.add_argument('-o','--outputFile', action='store', dest='outputFile', required = True,
                    help = "The event file generated by pythia.")

parser.add_argument('--evt','--numberOfEvents', action='store', dest='numberOfEvents', required = True, type=int, default=1,
                    help = "The number of events to be generated.")

#
# Pileup simulation arguments
#

parser.add_argument('--pileupAvg', action='store', dest='pileupAvg', required = False, type=int, default=40,
                    help = "The pileup average (default is zero).")

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




if len(sys.argv)==1:
  parser.print_help()
  sys.exit(1)

args = parser.parse_args()

minbias_file = os.environ['LZT_PATH']+'/generator/PythiaGenerator/data/minbias_config.cmnd'

from P8Kernel import EventGenerator

gen = EventGenerator( "EventGenerator", OutputFile = args.outputFile)


from PythiaGenerator import Pileup
# Generate the pileup
pileup = Pileup( "MinimumBias",
                 File           = minbias_file,
                 EtaMax         = 1.4,
                 Select         = 2,
                 PileupAvg      = args.pileupAvg,
                 BunchIdStart   = args.bc_id_start,
                 BunchIdEnd     = args.bc_id_end,
                 OutputLevel    = args.outputLevel,
                 Seed           = args.seed,
                 DeltaEta       = 0.22,
                 DeltaPhi       = 0.22,
                 )


from PythiaGenerator import ParticleGun, Particle
# Create the seed
gun = ParticleGun( "ParticleGun",
                   Eta          = 0.0,
                   #Eta          = 0.3,
                   Phi          = 1.52170894,
                   EnergyMin    = 15*GeV,
                   EnergyMax    = 100*GeV,
                   Particle     = Particle.Electron )

# Shoot an electron in the fixed direction
gen+=gun
# Add pileup around this electron
gen+=pileup
# Run!
gen.run(args.numberOfEvents)



