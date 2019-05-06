# Poem Modifier

Identify the nouns in a poem. Grab a dictionary. Replace each noun with one 10 entries down.

For example:

```
Mary had a little lamb,
whose fleece was white as snow.
```

becomes:

```
Mary had a little lambdoidal,
whose fley was white as snowbrush.
```

## Run

clone and grab git submodules:

```
git clone --recursive git@github.com:danemacaulay/poem-modifier.git
```

or grab them after a regular clone:

```
git submodule update --init --recursive
```


### with pipenv

```
pipenv install
pipenv shell
python -m spacy download en_core_web_sm
python modify.py
```


### or pip3/python3

```
pip install -r requirments.txt
python -m spacy download en_core_web_sm
python modify.py
```


