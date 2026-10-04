from fastapi.testclient import TestClient
from aiinfra.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'desired': '3', 'live': '3'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'desired': '3', 'live': '1'}).json()
    assert bad["passed"] is False
    assert "drift" in bad["failed"]
