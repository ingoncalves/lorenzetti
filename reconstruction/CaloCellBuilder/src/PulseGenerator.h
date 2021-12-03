#ifndef PulseGenerator_h
#define PulseGenerator_h

#include "GaugiKernel/StatusCode.h"
#include "GaugiKernel/AlgTool.h"
#include "GaugiKernel/EDM.h"
#include "CaloCell/CaloDetDescriptor.h"
#include "TRandom3.h"


class PulseGenerator : public Gaugi::AlgTool
{

  public:
    /** Constructor **/
    PulseGenerator( std::string name );
    virtual ~PulseGenerator();
    
    virtual StatusCode initialize() override;
    virtual StatusCode finalize() override;

    virtual StatusCode execute( const xAOD::EventInfo *, Gaugi::EDM * ) const override;



  private:

    void GenerateDeterministicPulse( xAOD::CaloDetDescriptor*, std::vector<float> &pulse,  float amplitude, float phase, float lag) const;
    void AddGaussianNoise( std::vector<float> &pulse, float noiseMean, float noiseStddev) const;


    /*! Number of samples to be generated */
    int m_nsamples;
    int m_startSamplingBC;
    float m_pedestal;
    float m_deformationMean;
    float m_deformationStd;
    float m_samplingRate;
    float m_noiseMean;    
    float m_noiseStd;    

    /*! Output level message */
    int m_outputLevel;
    /*! Random generator */
    mutable TRandom3 m_rng;
};

#endif




