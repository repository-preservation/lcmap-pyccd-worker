from pw import callback
from pw import logger
from pw import listen
from pw import open_connection
from pw import close_connection
from pw import run_http
from pw import terminate_http
from pw import HTTP_PORT
from pw import RABBIT_HOST
from pw import RABBIT_PORT
from pw import RABBIT_QUEUE
from pw import RABBIT_EXCHANGE
from pw import RESULT_ROUTING_KEY

import traceback
import sys


def main():
    conn = None
    http_process = None
    try:
        http_process = run_http(HTTP_PORT)
        conn = open_connection(RABBIT_HOST, RABBIT_PORT)
        listen(callback(RABBIT_EXCHANGE, RESULT_ROUTING_KEY), conn, RABBIT_QUEUE)
    except Exception as e:
        logger.error('Worker exception: {}'.format(e))
        traceback.print_exc(file=sys.stderr)
    finally:
        close_connection(conn)
        terminate_http(http_process)


if __name__ == "__main__":
    main()