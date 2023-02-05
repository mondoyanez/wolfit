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


def test_just_now():
    assert (pretty_date(datetime.utcnow() + timedelta(days=1))) == "just about now"


def test_yesterday():
    assert (pretty_date(datetime.utcnow() - timedelta(days=1))) == "Yesterday"


def test_three_days_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days=3))) == "3 days ago"


def test_two_weeks_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days=14))) == "2 weeks ago"


def test_eight_months_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days=240))) == "8 months ago"


def test_six_years_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days=2190))) == "6 years ago"
