python multi_choice.py \
    --do_predict \
    --model_name_or_path ./chinese-macbert-base1 \
    --test_file ../preprocess/test.json \
    --output_dir ./chinese-macbert-base/multiple-choice \
    --cache_dir ./cache \
    --context_file ${1}  \
    --pad_to_max_length \
    --max_seq_length 512 \
    --output_file ./output/chinese-macbert-base/predict_multi_choice_test.json