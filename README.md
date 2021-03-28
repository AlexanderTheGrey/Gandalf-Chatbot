# Gandalf AI Chatbot

## Requirements:

Python 3.6, 3.7 or 3.8

## To install:

First make sure that pip is up to date:

python -m pip install -U pip

### Optional:

Install within a virtual environment:

python -m pip install --user pipx

pipx install virtualenv

virtualenv venv

./venv/Scripts/activate

### End of optional installation

## To install the NLP:

pip install rasa[full]

To install the NLP model:

python -m spacy download en_core_web_md

## To run:

rasa shell

## To debug:

rasa shell nlu

## To run the actions server (neccessary for full functionality of the chatbot):

Open up a new shell, separate from where you will run the rasa shell:

rasa run actions