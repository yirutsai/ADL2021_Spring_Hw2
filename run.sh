python preprocess.py ${2} ./preprocess/test.json
cd ./multi_choice
bash test_MC.sh ${1}
cd ../QA
bash test_QA.sh ${1}
python encode.py ./hfl/chinese-macbert-large2/predict_predictions.json ${3}
