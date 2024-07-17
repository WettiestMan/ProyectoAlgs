# so we don't have to worry about executing the wrong .py

PYTHON_PATH_VENV=./.venv/Scripts/python.exe
PYTHON_PATH_ENV=./.env/Scripts/python.exe

MAIN_FILE=./main.py

TEST_FILE_ONE=./TEST.md
TEST_FILE_TWO=./txt.md

all: v

v:
	$(PYTHON_PATH_VENV) $(MAIN_FILE)

e:
	$(PYTHON_PATH_VENV) $(MAIN_FILE)

vtest:
	$(PYTHON_PATH_VENV) $(MAIN_FILE) $(TEST_FILE_ONE)

etest:
	$(PYTHON_PATH_VENV) $(MAIN_FILE) $(TEST_FILE_ONE)

vsimple:
	$(PYTHON_PATH_VENV) $(MAIN_FILE) $(TEST_FILE_TWO)

esimple:
	$(PYTHON_PATH_VENV) $(MAIN_FILE) $(TEST_FILE_TWO)