import sys
from pathlib import Path

from loguru import logger

DATA_DIR = Path.cwd() / 'project_euler/data'

logger.remove()
logger.add(
    sys.stderr,
    level='INFO',
)
