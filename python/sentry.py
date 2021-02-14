from python.errors import SentryError

try:
	import sentry_sdk
	from sentry_sdk.integrations.flask import FlaskIntegration
	sentry_sdk.init(
		dsn="https://144df4c8a5fb47228c3d9aa75c2399da@o515423.ingest.sentry.io/5620206",
		integrations=[FlaskIntegration()],
		traces_sample_rate=1.0)
	x = 0/0
except:
	raise SentryError('Sentry failed to load.')
