from pickle import TRUE


class Config(object):
    """Base Configuration"""


class ProductionConfig(Config):
    """Production Configuration"""


class DevelopmentConfig(Config):
    """Development Configuration"""


class TestingConfig(Config):
    """Testing Configuration"""

    TESTING = True
