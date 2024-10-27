import sys
sys.path.append('/content/tmp/BitNet')

import subprocess



class LLMModule:
  def __init__(self, repo_id, filename):
    print("llm module of bitnet")
    
    try:
      result = subprocess.run(
        [
          'python', 
          './BitNetsetup.py', 
          '--hf-repo', 
          repo_id, 
          '--quant-type', 
          filename
        ], 
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True  # Python 3.7以上の場合。出力を文字列として取得
      )
      
      print("標準出力:\n", result.stdout)
    except subprocess.CalledProcessError as e:
      print("エラーが発生しました。")
      print("リターンコード:", e.returncode)
      print("標準出力:\n", e.stdout)
      print("標準エラー出力:\n", e.stderr)

  def infer(self, prompt):
    args = [
      "-m", 
      "models/" + "a", 
      "-q", 
      "i2_s"
    ]
    result = subprocess.run(
      [
        "python", 
        "/content/tmp/BitNet/run_inference.py"
      ]
      , capture_output=True
      , text=True
    )

    return result


# python run_inference.py -m models/Llama3-8B-1.58-100B-tokens/ggml-model-i2_s.gguf -p "Daniel went back to the the the garden. Mary travelled to the kitchen. Sandra journeyed to the kitchen. Sandra went to the hallway. John went to the bedroom. Mary went back to the garden. Where is Mary?\nAnswer:" -n 6 -temp 0
   
