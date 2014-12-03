import logging
import random
import time
from pyleus.storm import Spout

log = logging.getLogger('rsum')


class PickLogSpout(Spout):

    OUTPUT_FIELDS = ["logEntry"]
    IP = ["127.0.0.1", "0.0.0.0", "111.222.333.444", "10.10.10.10"]
    DOMAINS = ["good.com", "fine.com", "not-bad.com",
               "nice.com", "evil.com", "horrible.com"]
    OUTPUT_FIELDS = ["logEntry"]

    def next_tuple(self):
        time.sleep(0.01)
        ip = random.choice(self.IP)
        domain = random.choice(self.DOMAINS)
        logEntry = "{}    {}    {}".format(time.time(), ip, domain)

        log.debug(logEntry)
        self.emit((logEntry,))


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        filename='/tmp/pick_log_spout.log',
        filemode='a',
    )

    PickLogSpout().run()
