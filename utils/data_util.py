import csv
import pandas as pd

def make_result_csv(result_filename = "result.csv"):
  # ヘッダーを追加

  result_filename = f"./output/{result_filename}"
  with open(result_filename, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["index", "package_name", "repo_id", "filename", "result", "time"])

def get_input_data(input_csv_name="input_for_llm.csv"):
  return pd.read_csv(f"./input/{input_csv_name}")
