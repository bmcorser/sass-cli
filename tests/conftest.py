import pytest
import tempfile


@pytest.fixture()
def output_dir():
    return tempfile.mkdtemp()
