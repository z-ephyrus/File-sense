from main.scanner import scanfile

def test_nonexistent_file():
    result = scanfile("fakefile.irng")
    assert "error" in result
