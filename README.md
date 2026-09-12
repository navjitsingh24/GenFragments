Different MC gen fragments for pp and pPb at different energies. Use CMSSW_9_4_11 release and create Configuration/GenProduction/python directories inside src

PYTHIA CP5/ HERWIG CH3 cmsDriver commands:

GEN-SIM: cmsDriver.py Configuration/GenProduction/python/fragment.py --fileout file:filename_GENSIM.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 94X_mc2017_realistic_forppRef5TeV --beamspot Realistic5TeVppCollision2017 --step GEN,SIM --geometry DB:Extended --era Run2_2017_ppRef --no_exec

DIGI-RECO: cmsDriver.py step1 --filein "dbs:/GEN_SIM_database/" --fileout file:filename_DR.root --mc --eventcontent RAWSIM --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_forppRef5TeV_v1 --beamspot Realistic5TeVppCollision2017 --step DIGI,L1,DIGI2RAW,HLT:PRef --geometry DB:Extended --era Run2_2017_ppRef --no_exec

AODSIM: cmsDriver.py step2 --filein "dbs:/DIGI_RECO_database/" --fileout file:filename_AOD.root --mc --eventcontent AODSIM --datatier AODSIM --conditions 94X_mc2017_realistic_forppRef5TeV_v1 --step RAW2DIGI,L1Reco,RECO,RECOSIM,EI --geometry DB:Extended --era Run2_2017_ppRef --no_exec

miniAOD: cmsDriver.py step1 --filein "dbs:/AOD_database/" --fileout file:filename_miniAOD.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 94X_mc2017_realistic_forppRef5TeV --step PAT --geometry DB:Extended --era Run2_2017_ppRef --no_exec
