
from acp_times import open_time, close_time

import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.WARNING)
log = logging.getLogger(__name__)

def test_zero_km():
	assert open_time(0, 200, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-01T00:00:00'
	assert close_time(0, 200, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-01T09:00:00+00:00'

def test_200km():
	assert open_time(200, 200, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-01T13:52:56.470588+00:00'
	assert close_time(200, 200, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-01T21:30:00+00:00'

def test_205km():
	assert open_time(205, 200, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-01T13:52:56.470588'
	assert close_time(205, 200, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-01T21:40:00+00:00'

def test_300km_for_200_dist():
	assert open_time(300, 200, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-01T17:00:26.470588+00:00'
	assert close_time(300, 200, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-01T21:30:00+00:00'

def test_boundaries():
	assert open_time(300, 300, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-01T16:49:24.705882+00:00'
	assert close_time(300, 300, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-02T04:00:00+00:00'

	assert open_time(400, 400, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-01T19:45:52.941176+00:00'
	assert close_time(400, 400, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-02T10:40:00+00:00'

	assert open_time(600, 600, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-02T01:38:49.411765+00:00'
	assert close_time(600, 600, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-03T00:00:00+00:00'

	assert open_time(1000, 1000, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-02T13:24:42.352941+00:00'
	assert close_time(1000, 1000, arrow.get("2017-01-01T08:00:00+00:00")) == '2017-01-04T02:40:00+00:00'