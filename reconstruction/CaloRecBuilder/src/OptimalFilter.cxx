#include "OptimalFilter.h"
#include "CaloCell/RawCell.h"

using namespace Gaugi;


OptimalFilter::OptimalFilter( std::string name ) : 
  IMsgService(name),
  AlgTool()
{
  declareProperty( "Weights"    , m_ofweights={}  );
  declareProperty( "OutputLevel", m_outputLevel=1 );
}



OptimalFilter::~OptimalFilter()
{}


StatusCode OptimalFilter::initialize()
{
  setMsgLevel(m_outputLevel);
  return StatusCode::SUCCESS;
}


StatusCode OptimalFilter::finalize()
{
  return StatusCode::SUCCESS;
}



StatusCode OptimalFilter::executeTool( const xAOD::EventInfo * /*evt*/, Gaugi::EDM *edm ) const
{

  auto *cell = static_cast<xAOD::RawCell*>(edm);

	auto pulse = cell->pulse();
	float energy=0.0;

  //float avgmu = evt->avgmu();

	if( m_ofweights.size() != pulse.size() ){
		MSG_ERROR( "The ofweights size its different than the pulse size." );
		return StatusCode::FAILURE;
	}else{
		for( unsigned sample=0; sample < pulse.size(); ++sample) 
			energy += pulse[sample]*m_ofweights[sample];
	}

	cell->setEnergy(energy);
	return StatusCode::SUCCESS;
}


