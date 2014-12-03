import logging

from pyleus.storm import SimpleBolt

log = logging.getLogger('rsum_results')


class ComputeRSumBolt(SimpleBolt):

    def process_tuple(self, tup):
        if len(tup.values):
            ip, count = tup.values
            log.debug("%s: %d", ip, count)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        filename='/tmp/rsum_results.log',
        format="%(message)s",
        filemode='a',
    )

    ComputeRSumBolt().run()
