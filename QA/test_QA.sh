python run_qa.py \
  --model_name_or_path hfl/chinese-macbert-large2 \
  --test_file ../multi_choice/output/chinese-macbert-base/predict_multi_choice_test.json \
  --context_file ${1} \
  --do_predict \
  --per_device_eval_batch_size 4 \
  --max_seq_length 512 \
  --doc_stride 120 \
  --output_dir ./hfl/chinese-macbert-large2 \
  --cache_dir ./cache \