# these imports are to provide a clean set of imports for the entire package
# ex: import cw
#     cw.send(...)
from .messaging import send
from .messaging import listen
from .messaging import open_connection
from .messaging import close_connection
from .worker import callback
from ccd import algorithm as ccd_alg_version

import sys
import logging
import os


boolean = lambda b: b.lower() in ['true', '1']

RABBIT_HOST =        os.getenv('LPW_RABBIT_HOST')
RABBIT_PORT =        int(os.getenv('LPW_RABBIT_PORT', '5672'))
RABBIT_QUEUE =       os.getenv('LPW_RABBIT_QUEUE')
RABBIT_EXCHANGE =    os.getenv('LPW_RABBIT_EXCHANGE')
RABBIT_SSL =         boolean(os.getenv('LPW_RABBIT_SSL', 'False'))
TILE_SPEC_HOST =     os.getenv('LPW_TILE_SPEC_HOST')
TILE_SPEC_PORT =     int(os.getenv('LPW_TILE_SPEC_PORT', '80'))
LOG_LEVEL =          os.getenv('LPW_LOG_LEVEL', 'INFO')
RESULT_ROUTING_KEY = ccd_alg_version

logging.basicConfig(stream=sys.stdout,
                    level=LOG_LEVEL,
                    format='%(asctime)s %(module)s::%(funcName)-20s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# default all loggers to WARNING then explictly override below
logging.getLogger("").setLevel(logging.WARNING)

# turn Pika DOWN, always want this unless there's wire level issues
logging.getLogger("pika").setLevel(logging.WARNING)

# let cw.* modules use configuration value
logger = logging.getLogger('cw')
logger.setLevel(LOG_LEVEL)
