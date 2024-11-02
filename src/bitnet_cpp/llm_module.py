import sys
sys.path.append('/content/tmp/BitNet')

from llm_module_base import LLMModuleBase 

import subprocess

def run_command(command):
    try:
      process = subprocess.Popen(
          command,
          stdout=subprocess.PIPE,
          stderr=subprocess.PIPE,
          text=True,
          cwd="./tmp/BitNet"
      )
      
      output = []  # 標準出力を格納するリスト
      # 出力をリアルタイムで表示
      for line in process.stdout:
          print(line, end='')  # ノートブックに出力
          output.append(line)  # 出力をリストに追加

      # エラー出力を表示
      stderr = process.stderr.read()
      if stderr:
          print(stderr)

      process.wait()  # プロセスが終了するのを待つ
    except subprocess.CalledProcessError as e:
      print("エラーが発生しました。")
    return process.returncode, ''.join(output)  # 戻り値をタプルとして返す

class LLMModule(LLMModuleBase):
  def __init__(self, repo_id, filename):
    print("llm module of bitnet")
    try:
      result_code, result_output = run_command(
        [
          'python', 
          'setup_env.py', 
          '--hf-repo', 
          repo_id, 
          '--quant-type', 
          filename
        ]
      )
      print("終了コード:", result_code)
      print("標準出力:\n", result_output)  # ここで標準出力を表示
    except subprocess.CalledProcessError as e:
      print("エラーが発生しました。")

    self.repo_id = repo_id
    self.filename = filename

  def infer(self, prompt):
    result_code, result_output = run_command(
      [
        "python",
        "run_inference.py",
        "-m",
        f"models/{self.repo_id.split('/')[1]}/ggml-model-{self.filename}.gguf",#todo: 後で自動生成
        "-p",
        prompt,
        "-n", 
        "30", 
        "-temp",
        "0"
      ]
    )

    return result_output


# python run_inference.py -m models/Llama3-8B-1.58-100B-tokens/ggml-model-i2_s.gguf -p "Daniel went back to the the the garden. Mary travelled to the kitchen. Sandra journeyed to the kitchen. Sandra went to the hallway. John went to the bedroom. Mary went back to the garden. Where is Mary?\nAnswer:" -n 6 -temp 0
   
