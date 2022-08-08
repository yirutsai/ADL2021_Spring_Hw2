import json
import sys
import os
import logging
from argparse import ArgumentParser, Namespace
from pathlib import Path
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

def main(args):
    for split in ["train", "eval"]:
        with open(args.data_dir / f"{split}.json","r") as f:
            data = json.load(f)
        with open(args.output_dir/f"{split}.json","w") as f:
            json.dump({"data":data},f,ensure_ascii=False,indent=2)
            logging.info(f"preprocessed saved at {str((args.output_dir/f'{split}.json').resolve())}")
    with open(args.data_dir / f"test.json","r") as f:
        data = json.load(f)
    for i in range(len(data)):
        data[i]["tags"] = ["O" for _ in range(len(data[i]["tokens"]))]
    with open(args.output_dir/f"test.json","w") as f:
        json.dump({"data":data},f,ensure_ascii=False,indent=2)
        logging.info(f"preprocessed saved at {str((args.output_dir/f'{split}.json').resolve())}")    
        


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "--data_dir",
        type=Path,
        help="Directory to the dataset.",
        default="../data/slot/",
    )
    parser.add_argument("--rand_seed", type=int, help="Random seed.", default=13)
    parser.add_argument(
        "--output_dir",
        type=Path,
        help="Directory to save the processed file.",
        default="../preprocess/slot/",
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    main(args)