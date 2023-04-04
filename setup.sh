#!/usr/bin/env bash
source virtualenv ~/.venv
source ~/.venv/bin/activate
#append it to bash so every shell launches with it 
echo 'source ~/.venv/bin/activate' >> ~/.bashrc
make install