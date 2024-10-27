from llama_cpp import Llama

class LLMModule:
  def __init__(self, repo_id, filename):
    self.llm = Llama.from_pretrained(
        repo_id=repo_id,
        filename=filename,
        verbose=False
    )

  def infer(self, prompt):

    return self.llm(
      prompt,
      max_tokens=32,
      stop=["Q:", "\n"],
      echo=True
    )
