#!/bin/bash
#installing python environment
sudo apt update
sudo apt -y upgrade
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install -y python3.10
sudo apt install -y python3-pip
sudo apt-get install -y python3.10-venv
sudo apt install -y libgtk-3-dev