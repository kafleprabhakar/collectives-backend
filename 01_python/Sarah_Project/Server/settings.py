# -----------------------------------------------------------------------------
# Settings related to server
# -----------------------------------------------------------------------------
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 2000

# -----------------------------------------------------------------------------
# Settings related to logger
# -----------------------------------------------------------------------------
# Whether print at console
LOGGING_CONSOLE_FLAG = True

# whether print at file
LOGGING_FILE_LOG = True

# Current log level
LOGGING_LEVEL = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
LOGGING_CURRENT_LEVEL = LOGGING_LEVEL[1]


# -----------------------------------------------------------------------------
# Settings related to scheduler
# -----------------------------------------------------------------------------
SCHEDULER_MODE = "interval"
SCHEDULER_INTERVAL = 10 # seconds

# -----------------------------------------------------------------------------
# Settings related to database
# -----------------------------------------------------------------------------
DATABASE_PORT = 27017
DATABASE_ADDRESS = 'localhost'