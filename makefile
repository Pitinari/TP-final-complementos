PY = python3
SRC = ./src/
GRAFOS = ./grafos/

malla:
	$(PY) $(SRC)main.py $(GRAFOS)malla.txt

2xK4:
	$(PY) $(SRC)main.py $(GRAFOS)2xK4.txt

K5:
	$(PY) $(SRC)main.py $(GRAFOS)K5.txt