#!/bin/bash

## python environment steps

############### Activate Environment
## 1. Check virtualenv installed 
sudo apt install python3-virtualenv


## 2. Ensure your in the correct directory
echo $PWD


## 3. run command with desire python version / venv name
virtualenv -p /usr/bin/python3.8  .venv


## 4. Activate venv
source .venv/bin/activate

## 5. install requirements
pip3 install -r requirements.txt

## 6. confirm correct python
type python3

############### Activate Environment

############### Deativate Environment

## 5. print local module list into requirement.txt 
pip3 freeze --local >requirements.txt

## 6. leave virtual environment
deactivate 

############### Deativate Environment