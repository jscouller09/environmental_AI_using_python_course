# ----------------------------------------------------------------------------------------------------------------------
# Name:         Testin
# Purpose:      Run test code during the training course
#
# Author:       james.scouller
#
# Created:      2024-08-07
# ----------------------------------------------------------------------------------------------------------------------
# global imports
import logging
from pathlib import Path
# ----------------------------------------------------------------------------------------------------------------------
# custom module imports

# ----------------------------------------------------------------------------------------------------------------------
# main code


logger = logging.getLogger(__name__)


if __name__ == '__main__':
    working_dir = Path(__file__).parent
    logger.info('Working in: {}'.format(working_dir))
    