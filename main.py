import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add arguments
parser.add_argument("--package_name", type=str, help="name of package ex: llama_cpp")
parser.add_argument("--repo_id", type=str, help="name of GGUF repo ex:QuantFactory/Borea-Phi-3.5-mini-Instruct-Jp-GGUF")
parser.add_argument("--filename", type=str, help="model file name ex: Borea-Phi-3.5-mini-Instruct-Jp.Q6_K.gguf")
parser.add_argument("--input_csv_name", type=str, help="ex: sample.csv")


# Parse the arguments
args = parser.parse_args()

import sys
sys.path.append(f'./src/{args.package_name}')
sys.path.append(f'./src/common')
sys.path.append(f'./utils')


from llm_module import LLMModule
from data_util import make_result_csv, get_input_data
from timestamp_utils import get_date_str
import csv




def main(
  repo_id,
  filename,
  input_csv_name = "sample.csv"
):
  date_str = get_date_str()

  input_df = get_input_data(input_csv_name)
  input_dict = input_df.to_dict(orient="records")
  
  make_result_csv(result_filename = f"result_{input_csv_name}")
  
  # llm moduleの実体化
  llm = LLMModule(repo_id, filename)

  for n, i in enumerate(input_dict):
    # i.key() = index, input
    print(f"infer for {n} sample..")
    r = llm.infer_with_metrics(i["input"])

    with open(f"./output/result_{input_csv_name}", mode="a", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(
        [
          i["index"],
          args.package_name,
          args.repo_id,
          args.filename,
          r["result"],
          "{:.2f}".format(r["time"])
        ]
      )
    


  



if  __name__ == "__main__":
  main(
    repo_id = args.repo_id,
    filename = args.filename,
    input_csv_name = args.input_csv_name
  )