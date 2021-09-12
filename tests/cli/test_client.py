import vcr

from umm.cli.client import umm_request


@vcr.use_cassette()
def test_umm_request():
    resp = umm_request([])
    assert resp == {"commands": []}
