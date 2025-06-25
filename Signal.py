import signal
import sys
import Colors


def signal_handler(sig, frame):
    print('\n\n' + Colors.error_pref + 'Seems like you pressed CTRL+C. Exit...')
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
