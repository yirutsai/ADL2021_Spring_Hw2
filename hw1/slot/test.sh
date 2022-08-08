python slot.py \
    --model_name_or_path bert-base-cased1 \
    --do_predict \
    --test_file ../preprocess/slot/test.json \
    --train_file ../preprocess/slot/train.json \
    --cache_dir ./cache \
    --output_dir bert-base-cased1 \