.PHONY: check-env checks test quickstart experiment clean summarize

check-env:
	python scripts/check_environment.py

checks:
	python scripts/run_checks.py

test:
	python -m pytest

quickstart:
	python examples/quick_start.py

experiment:
	python main.py

clean:
	python scripts/clean_results.py

summarize:
	python scripts/summarize_results.py

.PHONY: new-log
new-log:
	python scripts/new_experiment_log.py

.PHONY: list-results
list-results:
	python scripts/list_results.py

.PHONY: status
status:
	python scripts/project_status.py
