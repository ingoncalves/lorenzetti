#ifndef CaloCell_h
#define CaloCell_h

/** simulator includes **/
#include "CaloCell/enumeration.h"
#include "CaloCell/RawCell.h"
#include "GaugiKernel/EDM.h"
#include "GaugiKernel/macros.h"


namespace xAOD{
  
  class CaloCell: public Gaugi::EDM
  {  
    public:

      /** Constructor **/
      CaloCell()=default;
      
      /** Contructor **/
      CaloCell( float eta, float phi, float deta, float dphi, 
                CaloSampling::CaloSample sample, CaloSampling::CaloLayer layer,
                CaloSampling::CaloSection section);

      /** Destructor **/
      ~CaloCell()=default;
      /*! Cell eta center */
      PRIMITIVE_SETTER_AND_GETTER( float, m_eta, setEta, eta );
      /*! Cell phi center */
      PRIMITIVE_SETTER_AND_GETTER( float, m_phi, setPhi, phi );
      /*! Cell delta eta */
      PRIMITIVE_SETTER_AND_GETTER( float, m_deta, setDeltaEta , deltaEta);
      /*! Cell delta phi */
      PRIMITIVE_SETTER_AND_GETTER( float, m_dphi, setDeltaPhi, deltaPhi );
      /*! Cell energy **/
      PRIMITIVE_SETTER_AND_GETTER( float, m_energy, setEnergy, energy );
      /*! Tranverse energy */
      PRIMITIVE_SETTER_AND_GETTER( float, m_et, setEt, et );

      /*! Cell sampling id */
      PRIMITIVE_SETTER_AND_GETTER( CaloSampling::CaloSample  , m_sample , setSample   , sample  );
      /*! Cell layer id */
      PRIMITIVE_SETTER_AND_GETTER( CaloSampling::CaloLayer   , m_layer  , setLayer    , layer   );
      /*! Cell section id */
      PRIMITIVE_SETTER_AND_GETTER( CaloSampling::CaloSection , m_section, setSection  , section );

      /*! Get the associated Raw information */ 
      const xAOD::RawCell* parent() const;
      /*! Set the associated Raw information */ 
      void setParent( const xAOD::RawCell* );


    private:
 
      /*! id sample */
      CaloSampling::CaloSample m_sample;
      /*! id layer */
      CaloSampling::CaloLayer m_layer;
      /*! id section */
      CaloSampling::CaloSection m_section;


      /*! eta center */
      float m_eta;
      /*! phi center */
      float m_phi;
      /*! delta eta */
      float m_deta;
      /*! delta phi */
      float m_dphi;
      /*! Energy */
      float m_energy;
      /*! Transverse energy*/
      float m_et;

      /*! Associated raw information */
      const xAOD::RawCell *m_parent;
  };

}
#endif
