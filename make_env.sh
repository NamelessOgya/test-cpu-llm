#!/bin/bash

# make virtual env / install package
sudo apt-get update
sudo apt-get install python3.10-venv
cd ./env && python3 -m venv ./testvenv
source ./testvenv/bin/activate

package_name=$1

cd ../

# インストール  
sed -i 's/\r//' ./src/${package_name}/install.sh
./src/${package_name}/install.sh