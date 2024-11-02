from llm_module_base import LLMModuleBase 
import ollama


class LLMModule(LLMModuleBase):
  def __init__(self, repo_id, filename):
    repo_id = self.repo_id
    

  def infer(self, prompt):

    return self.llm(
      prompt,
      max_tokens=32,
      stop=["Q:", "\n"],
      echo=True
    )["choices"][0]["text"]