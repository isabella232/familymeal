#!/usr/bin/env python

"""
Project-wide application configuration.

DO NOT STORE SECRETS, PASSWORDS, ETC. IN THIS FILE.
They will be exposed to users. Use environment variables instead.
"""

import os

PROJECT_NAME = 'Family Meal'
DEPLOYED_NAME = 'familymeal'

PRODUCTION_S3_BUCKETS = ['apps.npr.org', 'apps2.npr.org']
PRODUCTION_SERVERS = ['50.112.202.166']

STAGING_S3_BUCKETS = ['tumblr-stage.npr.org']
# STAGING_SERVERS = ['54.245.198.194']
STAGING_SERVERS = ['127.0.0.1:8001']


S3_BUCKETS = []
SERVERS = []
DEBUG = True

TUMBLR_KEY = ''

PROJECT_DESCRIPTION = 'This is where the description would go.'
SHARE_URL = 'http://%s/%s/' % (PRODUCTION_S3_BUCKETS[0], DEPLOYED_NAME)

TWITTER = {
    'TEXT': PROJECT_NAME,
    'URL': SHARE_URL
}

FACEBOOK = {
    'TITLE': DEPLOYED_NAME,
    'URL': SHARE_URL,
    'DESCRIPTION': PROJECT_DESCRIPTION,
    'IMAGE_URL': '',
    'APP_ID': '138837436154588'
}

NPR_DFP = {
    'STORY_ID': '139482413',
    'TARGET': '\/news_election_results;storyid=139482413'
}

GOOGLE_ANALYTICS_ID = 'UA-5828686-4'

def configure_targets(deployment_target):
    """
    Configure deployment targets. Abstracted so this can be
    overriden for rendering before deployment.
    """
    global S3_BUCKETS
    global SERVERS
    global DEBUG
    global TUMBLR_URL
    global TUMBLR_BLOG_ID

    if deployment_target == 'production':
        S3_BUCKETS = PRODUCTION_S3_BUCKETS
        SERVERS = PRODUCTION_SERVERS
        DEBUG = False
        TUMBLR_URL = 'dinnertimeconfessional.tumblr.com'
        TUMBLR_BLOG_ID = 'dinnertimeconfessional'

    else:
        S3_BUCKETS = STAGING_S3_BUCKETS
        SERVERS = STAGING_SERVERS
        DEBUG = True
        TUMBLR_URL = 'staging-family-meal.tumblr.com'
        TUMBLR_BLOG_ID = 'staging-family-meal'

DEPLOYMENT_TARGET = os.environ.get('DEPLOYMENT_TARGET', None)

configure_targets(DEPLOYMENT_TARGET)
