from collections import defaultdict
from collections import namedtuple
import logging

from pyleus.storm import SimpleBolt

log = logging.getLogger('blacklisted')

Counter = namedtuple("Counter", "ip count")


class BlackListBolt(SimpleBolt):

    OUTPUT_FIELDS = Counter

    def initialize(self):
        self.ips = defaultdict(int)
        self.blacklist = ['evil.com', 'horrible.com']

    def process_tuple(self, tup):
        if not len(tup.values):
            self.emit(("NULL", 0), anchors=[tup])
        else:
            ip, domain = tup.values
            if domain in self.blacklist:
                self.ips[ip] += 1
            log.debug("{0} {1}".format(ip, self.ips[ip]))
            self.emit((ip, self.ips[ip]), anchors=[tup])


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        filename='/tmp/blacklisted.log',
        format="%(message)s",
        filemode='a',
    )

    BlackListBolt().run()
