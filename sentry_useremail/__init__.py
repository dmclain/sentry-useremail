try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sentry_useremail').version
except Exception, e:
    VERSION = 'unknown'
