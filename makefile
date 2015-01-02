all:
	@echo 'Use one of the targets - runAnalysis/createTeam/examples'

runAnalysis:
	python src/main.py runAnalysis

createTeam:
	python src/main.py createTeam

examples:
	python src/main.py
