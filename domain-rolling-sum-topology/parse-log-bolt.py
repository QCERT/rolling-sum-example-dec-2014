import logging

from pyleus.storm import SimpleBolt

log = logging.getLogger('parse')


class ParseLogBolt(SimpleBolt):

    OUTPUT_FIELDS = ["ip", "domain"]

    def process_tuple(self, tup):
        if not len(tup.values):
            entry = "nothing"
            ip = "Null"
            domain = "Null"
            self.emit((ip, domain), anchors=[tup])
        else:
            entry, = tup.values
            log.debug(entry)
            timestamp, ip, domain = entry.split('    ')
            log.debug(ip + ": " + domain)
            self.emit((ip, domain), anchors=[tup])


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        filename='/tmp/parse.log',
        format="%(message)s",
        filemode='a',
    )
    ParseLogBolt().run()
