import json
from app import create_app
from app.aceest import calc_bmi

def test_health_ok():
    app = create_app()
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"

def test_members_list():
    app = create_app()
    client = app.test_client()
    r = client.get("/members")
    assert r.status_code == 200
    data = r.get_json()
    assert "members" in data and isinstance(data["members"], list)

def test_members_create_validation():
    app = create_app()
    client = app.test_client()
    r = client.post("/members", data=json.dumps({}), content_type="application/json")
    assert r.status_code == 400

def test_members_create_ok():
    app = create_app()
    client = app.test_client()
    r = client.post("/members", data=json.dumps({"name": "Casey"}), content_type="application/json")
    assert r.status_code == 201
    assert r.get_json()["name"] == "Casey"

def test_calc_bmi():
    assert calc_bmi(70, 175) == 22.86
