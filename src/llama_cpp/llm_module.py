from llm_module_base import LLMModuleBase 
from llama_cpp        import Llama
from llm_module_base import LLMModuleBase 

class LLMModule(LLMModuleBase):
  def __init__(self, repo_id, filename):
    self.llm = Llama.from_pretrained(
        repo_id=repo_id,
        filename=filename,
        verbose=False
    )

  def infer(self, prompt):
    llm_input = "Q:" + prompt + "A:"
    
    responce = self.llm(
      llm_input,
      max_tokens=1000,
      stop=["Q:", "\n"],
      echo=True
    )["choices"][0]["text"]

    # Q:質問文 A:返答の形で出力してくるので、返答部分のみ成形
    out = responce.split("A:")[1]
    return out
