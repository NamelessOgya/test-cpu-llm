from abc import ABC, abstractmethod
import time
import psutil
import os

class LLMModuleBase(ABC):
  @abstractmethod
  def infer(self, prompt):
    '''
      モデル固有の推論コード
      各ロジックのLLMModuleにて実装
    '''
    pass

  def monitor_memory(self):
    """メモリ使用量を監視し、最大メモリ使用量を記録するジェネレータ"""
    process = psutil.Process(os.getpid())
    max_memory = 0
    while True:
        current_memory = process.memory_info().rss  # 現在のRSSメモリ使用量
        max_memory = max(max_memory, current_memory)
        yield max_memory
        time.sleep(1)  # 監視の間隔を調整

  
  def infer_with_metrics(self, prompt):
    '''
      実行時間とメモリ消費量をはかりつつ、
      推論を実行する。
    '''
    memory_monitor = self.monitor_memory()
    start_time = time.time()

    result = self.infer(prompt)

    max_memory_usage = next(memory_monitor)
    end_time = time.time()
    execution_time = end_time - start_time

    return {
      "time"  : execution_time,
      "memory": max_memory_usage / (1024 ** 3),#GB
      "result": result
    }