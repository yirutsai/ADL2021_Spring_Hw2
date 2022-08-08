python multi_choice.py \
    --do_train \
    --model_name_or_path hfl/chinese-macbert-base \
    --output_dir ./chinese-macbert-base1 \
    --train_file ../preprocess/train.json   \
    --context_file ${1}\
    --pad_to_max_length \
    --max_seq_length 512   \
    --learning_rate 3e-5   \
    --num_train_epochs 3 \
    --per_device_train_batch_size 1 \
    --do_eval \
    --validation_file ../preprocess/valid.json \
    --gradient_accumulation_steps 8 \
    --overwrite_output_dir

