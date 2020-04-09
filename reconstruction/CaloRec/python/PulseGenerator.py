
__all__ = ["PulseGenerator"]

from Gaugi import Logger
from Gaugi.messenger.macros import *
from RecCommon import treatPropertyValue


class PulseGenerator( Logger ):

  __allow_keys = ["OutputLevel", "NSamples", "ShaperFile"]

  def __init__( self, name, **kw ):

    Logger.__init__(self)
    import ROOT
    ROOT.gSystem.Load('liblorenzetti')
    from ROOT import RunManager, PulseGenerator
    self.__core = PulseGenerator(name)
    for key, value in kw.items():
      self.__core.setProperty( key, value )


  def core(self):
    return self.__core


  def setProperty( self, key, value ):
    if key in self.__allow_keys:
      setattr( self, '__' + key , value )
      self.core().setProperty( key, value )
    else:
      MSG_ERROR( self, "Property with name %s is not allow for PulseGenerator object", key)

 
  def getProperty( self, key ):
    if key in self.__allow_keys:
      return getattr( self, '__' + key )
    else:
      MSG_ERROR( self, "Property with name %s is not allow for PulseGenerator object", key)

     
