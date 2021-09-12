async def test_request(app):
    params = {t: "" for t in ["python"]}
    resp = await app.get("/umm", params=params)
    # resp_json = await resp.json()
    assert resp.status == 200
