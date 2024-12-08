#!/bin/bash

package_name=$1
sudo apt-get update
sudo apt-get install python3.10-venv
cd ./env && python3 -m venv ./testvenv
source ./testvenv/bin/activate \
&& cd ../ \
&& sed -i 's/\r//' ./src/${package_name}/install.sh \
&& ./src/${package_name}/install.sh