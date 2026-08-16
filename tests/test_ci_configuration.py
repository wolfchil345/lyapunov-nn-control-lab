import textwrap
from pathlib import Path


def read_workflow(name: str) -> str:
    p = Path('.github') / 'workflows' / name
    assert p.exists(), f"workflow {name} missing"
    return p.read_text(encoding='utf-8')


def test_workflows_present_and_structured():
    tests = read_workflow('tests.yml')
    quality = read_workflow('quality-gate.yml')
    codeql = read_workflow('codeql.yml')

    # Tests workflow must have matrix workers and a stable aggregate job 'test'
    assert 'test-python' in tests, 'test-python job missing in Tests workflow'
    assert '\n  test:' in tests or '\n  test:' in tests, 'aggregate job id "test" missing in Tests workflow'
    assert 'matrix:' in tests and 'python-version' in tests, 'Tests matrix python versions missing'

    # Quality gate must be a single non-matrix job named 'quality-gate'
    assert 'quality-gate' in quality, 'quality-gate workflow missing'
    assert 'matrix:' not in quality, 'Quality gate should not be a matrix job'

    # CodeQL workflow must exist
    assert 'Analyze Python' in codeql or 'codeql' in codeql, 'CodeQL workflow content seems unexpected'
