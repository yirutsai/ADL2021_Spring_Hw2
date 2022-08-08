# Homework 2 ADL NTU 110 Spring
## Environment
```
conda create -n <env_name> python=3.8
conda activate <env_name>
pip install -r requirements.txt
```
### Important versions of packages
```
python=3.8
pytorch=1.10.2
```
## Reproduce
```
bash download.sh
bash ./run.sh /path/to/context.json /path/to/test.json  /path/to/pred/prediction.csv
```
## Training
If you want to have learning curve, you would need to setup the wandb environment.
### Downloading data
```
bash download_data.sh
```
### Preprocessing
```
bash preprocess.sh
```
### Context Selection
```
cd multi_choice
bash train_MC.sh /path/to/context.json
bash test_MC.sh /path/to/context.json
```
Change directory to /path/to/multi_choice.py
The model will be saved in chinese-macbert-base1
The result of ./data/test.json will be saved in ./output/chinese-macbert-base/
Please make sure the <output_dir> in train_MC.sh is equal to <model_name_or_path> in test_MC.sh.
You can run the python script taking the shell script for an example which follow the huggingface trainer argument.
<output_file> in python script is the location of output file.
[https://huggingface.co/docs/transformers/v4.18.0/en/main_classes/trainer#transformers.TrainingArguments]
If the shell script has any problem, please directly use the python script.(hope not)

### Question Answering
```
cd ../QA
bash train_QA.sh /path/to/context.json
bash test_QA.sh /path/to/context.json
python encode.py hfl/chinese-macbert-large2/predict_predictions.json /path/to/prediction
```
Change directory to /path/to/run_qa.py
The model will be saved in hfl/chinese-macbert-large2
The result will be saved in /path/to/prediction
Please make sure the <output_dir> in train_QA.sh is equal to <model_name_or_path> in test_QA.sh.
You can run the python script taking the shell script for an example which follow the huggingface trainer argument.[https://huggingface.co/docs/transformers/v4.18.0/en/main_classes/trainer#transformers.TrainingArguments]
If the shell script has any problem, please directly use the python script.(hope not)