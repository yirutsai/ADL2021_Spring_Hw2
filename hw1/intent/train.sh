python intent.py \
    --model_name_or_path bert-base-cased \
    --do_train \
    --do_eval \
    --train_file ../preprocess/intent/train.json \
    --validation_file ../preprocess/intent/eval.json \
    --output_dir bert-base-cased1 \
    --per_device_train_batch_size=8 \
    --per_device_eval_batch_size=8 \
    --gradient_accumulation_steps 8 \
    --eval_steps 100 \
    --save_steps 100 \
    --evaluation_strategy steps \
    --overwrite_output_dir \
    # --label_names=["label"] \    