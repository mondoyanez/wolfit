from app.helpers import pretty_date
from datetime import datetime, timedelta


def test_now():
    assert pretty_date(datetime.utcnow()) == "just now"


def test_seconds_ago():
    assert pretty_date(datetime.utcnow() - timedelta(seconds=10)) == "10 seconds ago"


def test_minute_ago():
    assert pretty_date(datetime.utcnow() - timedelta(minutes=1)) == "a minute ago"


def test_minutes_ago():
    assert pretty_date(datetime.utcnow() - timedelta(minutes=5)) == "5 minutes ago"


def test_hour_ago():
    assert pretty_date(datetime.utcnow() - timedelta(hours=1)) == "an hour ago"


def test_hours_ago():
    assert pretty_date(datetime.utcnow() - timedelta(hours=7)) == "7 hours ago"


def test_yesterday():
    assert (pretty_date(datetime.utcnow() - timedelta(days=1))) == "Yesterday"
