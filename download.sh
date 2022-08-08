wget https://www.dropbox.com/s/64mvalht9c0qgw3/MC_model.zip?dl=1 -O MC_model.zip
wget https://www.dropbox.com/s/9f1hbtc4bao8rlg/QA_model.zip?dl=1 -O QA_model.zip

unzip MC_model.zip -d multi_choice
unzip QA_model -d QA

rm -rf MC_model.zip
rm -rf QA_model.zip
