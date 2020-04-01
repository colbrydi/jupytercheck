MODULENAME = answercheck.py 

help:
	@echo ""
	@echo "Welcome to the jupyter test project!!!"
	@echo "To generate project documentation use:"
	@echo "	make doc"
	@echo ""
	@echo "To Lint the project use:"
	@echo "	make lint"
	@echo ""
	@echo "To run unit tests use:"
	@echo "	make test"
	@echo ""
	

doc:
	pdoc --force --html --output-dir ./docs $(MODULENAME)

lint:
	pylint $(MODULENAME)

test:
	pytest 

.PHONY: init doc lint test 
