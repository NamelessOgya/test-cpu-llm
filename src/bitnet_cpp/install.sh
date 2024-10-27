mkdir /content/test-cpu-llm/tmp
cd /content/test-cpu-llm/tmp

git clone --recursive https://github.com/microsoft/BitNet.git
cd BitNet

conda create -n bitnet-cpp python=3.9
conda activate bitnet-cpp
pip install -r requirements.txt

