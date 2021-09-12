import vcr

from umm.cli.client import umm_request
from umm.server.utils import setup_folder


@vcr.use_cassette()
def test_umm_request():
    setup_folder()
    resp = umm_request([])
    assert resp == {"commands": []}
