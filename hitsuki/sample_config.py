if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to "
          "a config file, don't just rename and change"
          "values here. Doing that WILL backfire on you.\n"
          "Bot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "YOUR KEY HERE"
    OWNER_ID = "YOUR ID HERE"
    OWNER_USERNAME = "YOUR USERNAME HERE"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://hzcyvgnurawrau:708ca1f465d94b0711757768554c761e244c260d8bdae6de5e80d23184cab068@ec2-54-208-233-243.compute-1.amazonaw'
    MESSAGE_DUMP = None
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []
    SUPPORT_USERS = []
    WHITELIST_USERS = []
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False
    STRICT_GBAN = False
    WORKERS = 8
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'
    CUSTOM_CMD = False
    SPAMMERS = ""
    TEMPORARY_DATA = None


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
