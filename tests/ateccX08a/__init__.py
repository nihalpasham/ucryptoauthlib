# -*- coding: utf-8 -*-
# pylint: disable=E1101
import gc
gc.threshold(4096)
import logging

from cryptoauthlib.device import ATECCX08A
from ateccX08a import tests_info
from ateccX08a import tests_sha
from ateccX08a import tests_random
from ateccX08a import tests_nonce
from ateccX08a import tests_read
from ateccX08a import tests_write
from ateccX08a import tests_lock
from ateccX08a import tests_verify
from ateccX08a import tests_sign
from ateccX08a import tests_selftest

log = logging.getLogger("ateccX08a")


def test(exclude=[
        # 'info',
        # 'sha',
        # 'random',
        # 'nonce',
        # 'read',
        # 'write',
        'lock',
        # 'verify',
        # 'sign',
        # 'selftest'
    ]):
    device = ATECCX08A()
    log.info("%s", device)

    if 'info' not in exclude:
        tests_info.run(device)
        log.info("INFO SUCCEDED")
    else:
        log.info("INFO SKIPPED")

    if 'sha' not in exclude:
        tests_sha.run(device)
        log.info("SHA SUCCEDED")
    else:
        log.info("SHA SKIPPED")

    if 'random' not in exclude:
        tests_random.run(device)
        log.info("RANDOM SUCCEDED")
    else:
        log.info("RANDOM SKIPPED")

    if 'nonce' not in exclude:
        tests_nonce.run(device)
        log.info("NONCE SUCCEDED")
    else:
        log.info("NONCE SKIPPED")

    if 'read' not in exclude:
        tests_read.run(device)
        log.info("READ SUCCEDED")
    else:
        log.info("READ SKIPPED")

    if 'write' not in exclude:
        tests_write.run(device)
        log.info("WRITE SUCCEDED")
    else:
        log.info("WRITE SKIPPED")

    if 'lock' not in exclude:
        tests_lock.run(device)
        log.info("LOCK SUCCEDED")
    else:
        log.info("LOCK SKIPPED")

    if 'verify' not in exclude:
        tests_verify.run(device)
        log.info("VERIFY SUCCEDED")
    else:
        log.info("VERIFY SKIPPED")

    if 'sign' not in exclude:
        tests_sign.run(device)
        log.info("SIGN SUCCEDED")
    else:
        log.info("SIGN SKIPPED")

    if 'selftest' not in exclude:
        tests_selftest.run(device)
        log.info("SELFTEST SUCCEDED")
    else:
        log.info("SELFTEST SKIPPED")

    

# import logging
# logging.basicConfig(level=logging.DEBUG)

# import ateccX08a; ateccX08a.test()
