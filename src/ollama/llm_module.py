from llm_module_base import LLMModuleBase 
from llama_cpp        import Llama
from llm_module_base import LLMModuleBase 
import ollama

class LLMModule(LLMModuleBase):
  def __init__(self, repo_id, filename):
    # lamma_cppを使ってモデルをダウンロード
    self.llm = Llama.from_pretrained(
        repo_id=repo_id,
        filename=filename,
        verbose=False,
        cache_dir="./tmp"
    )
    modelfile=f'''
    FROM {"models--" + repo_id.replace("/", "--")}
    '''
    
    # この部分でcommection errorとなる。  
    # なんでconnectionが必要？
    ollama.create(model='example', modelfile=modelfile)
    

  def infer(self, prompt):

    return self.llm(
      prompt,
      max_tokens=32,
      stop=["Q:", "\n"],
      echo=True
    )["choices"][0]["text"]


