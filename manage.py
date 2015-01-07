#!/usr/bin/env python
import os
import sys
import signal

if __name__ == "__main__":
    if os.environ.get('DOCKER', None) == '1':
        # Signal handler to trap SIGTERM signals sent by `docker stop` and
        # "gracefully" shutting down the server. Only installed when run inside
        # a docker container which explicitly sets the DOCKER environment
        # variable to 1.
        def quit(sig, frame):
            sys.exit()
        signal.signal(signal.SIGTERM, quit)

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
