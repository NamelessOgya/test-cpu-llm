from llm_module_base import LLMModuleBase 

class LLMModule(LLMModuleBase):
  def __init__(self, repo_id, filename):

    self.repo_id = repo_id
    self.filename = filename

    print("dummpy llm init")

  def infer(self, prompt):
    
    return "this is dummy output"
