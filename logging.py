import logging

logging.debug('This is debug line')
logging.info('This is info line')
logging.warning('This is warning line')
logging.error('This is error line')
logging.critical('This is critical line')

# Output
"""
WARNING:root:This is warning line
ERROR:root:This is error line
CRITICAL:root:This is critical line
"""