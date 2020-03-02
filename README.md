# Guessing-game
A simple guessing game implementation with a test suite

This game is an extention of the simple guesisng game described [here](https://medium.com/better-programming/building-a-simple-guessing-game-in-python-e39058a8cbcf) with added modules for numbers, colours and animals. The game has three levels and tries per level are limited to three.

To run the game and the unit tests:

- Requires Python 3 environment
- Coverage package installed

To install Coverage:

```python
pip install coverage
```

Clone/download the repository. In command line:

```python
python main.py
```

To run the test suite:

```python
python -m unittest discover
coverage run -m unittest discover
coverage report -m
coverage html
```
