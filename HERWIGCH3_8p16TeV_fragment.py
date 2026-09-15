import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Herwig7Settings.Herwig7CH3TuneSettings_cfi import *
from Configuration.Generator.Herwig7Settings.Herwig7PSWeightsSettings_cfi import *
from Configuration.Generator.Herwig7Settings.Herwig7StableParticlesForDetector_cfi import *

generator = cms.EDFilter("Herwig7GeneratorFilter",
                     herwig7CH3SettingsBlock,
                         herwig7PSWeightsSettingsBlock,
                         herwig7StableParticlesForDetectorBlock,
                         configFiles = cms.vstring(),
                         crossSection = cms.untracked.double(-1),
                         dataLocation = cms.string('${HERWIGPATH:-6}'),
                         eventHandlers = cms.string('/Herwig/EventHandlers'),
                         filterEfficiency = cms.untracked.double(1.0),
                         generatorModule = cms.string('/Herwig/Generators/EventGenerator'),
                         hw_user_settings = cms.vstring(
                             'cd /',
                             'read snippets/PPCollider.in',
                             'cd /Herwig/EventHandlers',
                            'set /Herwig/EventHandlers/EventHandler:LuminosityFunction:Energy 8160.0',
        'cd /',
                            'mkdir /Herwig/Weights',
                             'cd /Herwig/Weights',
                            'create ThePEG::ReweightMinPT reweightMinPT ReweightMinPT.so',
                             'cd /Herwig/MatrixElements/',
                             'insert SubProcess:MatrixElements[0] MEQCD2to2',
                             'insert SubProcess:Preweights[0] /Herwig/Weights/reweightMinPT',
                            'cd /',
                             'set /Herwig/Cuts/JetKtCut:MinKT 15.*GeV',
                             'set /Herwig/Cuts/JetKtCut:MaxKT 8000.*GeV',
                             'set /Herwig/Cuts/Cuts:MHatMin  0.0*GeV',
                             'set /Herwig/Cuts/Cuts:X1Min    1e-07',
                             'set /Herwig/Cuts/Cuts:X2Min    1e-07',
                             'set /Herwig/Cuts/MassCut:MinM  0.0*GeV',
                             'set /Herwig/Weights/reweightMinPT:Power 4.5',
                             'set /Herwig/Weights/reweightMinPT:Scale 15*GeV'
    ),
                     parameterSets = cms.vstring(
                             'herwig7CH3PDF',
                             'herwig7CH3AlphaS',
                             'herwig7CH3MPISettings',
                             'hw_PSWeights_settings',
                             'herwig7StableParticlesForDetector',
                             'hw_user_settings',
                         ),
                     repository = cms.string('${HERWIGPATH}/HerwigDefaults.rpo'),
                        run = cms.string('InterfaceMatchboxTest'),
                         runModeList = cms.untracked.string('read,run'),
)

ProductionFilterSequence = cms.Sequence(generator)
