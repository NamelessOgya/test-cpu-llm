from llm_module_base import LLMModuleBase 
from llama_cpp        import Llama

class LLMModule(LLMModuleBase):
  def __init__(self, repo_id, filename):
    self.llm = Llama.from_pretrained(
        repo_id=repo_id,
        filename=filename,
        verbose=False,
        n_ctx = 4096
    )

  def infer(self, prompt, temperature=0.3):

    out = self.llm.create_chat_completion(
      messages=[
          {
              "role": "system",
              "content": "あなたは優秀なキャリアアドバイザーです。転職したいクライアントから相談を受け、クライアントにとって最適な提案を行うことでクライアントを支援します。結果は必ず日本語で出力するルールになっています。出力はjsonフォーマットでお願いします",
          },
          {"role": "user", "content": prompt},
      ],
      response_format={
          "type": "json_object",
      },
      temperature=temperature,
      max_tokens=3000
    )



    return out["choices"][0]["message"]["content"]
