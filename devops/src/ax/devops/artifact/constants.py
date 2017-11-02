# Copyright 2015-2016 Applatix, Inc. All rights reserved.

DEFAULT_PROCESS_INTERVAL = 86400  # one day
DEFAULT_PAGE_SIZE = 2000

MILLISECONDS_PER_SECOND = 1000  # one second
MILLISECONDS_PER_MIN = 60000  # one minute
MILLISECONDS_PER_HOUR = 3600000  # one hour
MILLISECONDS_PER_DAY = 86400000  # one day
MILLISECONDS_PER_WEEK = 604800000  # one week
MILLISECONDS_PER_MONTH = 2628000000  # one month

FLAG_NOT_DELETED = 0
FLAG_DELETED = 1  # Permanently expired (based on retention policy)
FLAG_TO_BE_DELETED = 2  # Temporarily deleted
FlAG_EXPIRED = 3  # Permanently deleted (by user)

FLAG_ALIAS = -1
FLAG_IS_ALIAS = 1
FLAG_IS_NOT_ALIAS = 0

RETENTION_TAG_DEFAULT = 'internal'
RETENTION_TAG_AX_LOG = 'ax-log'
RETENTION_TAG_AX_LOG_EXTERNAL = 'ax-log-external'
RETENTION_TAG_USER_LOG = 'user-log'
RETENTION_TAG_LONG_RETENTION = 'exported'
RETENTION_TAGS = {
    RETENTION_TAG_DEFAULT,
    RETENTION_TAG_AX_LOG,
    RETENTION_TAG_USER_LOG,
    RETENTION_TAG_LONG_RETENTION
}

ARTIFACT_TYPE_INTERNAL = 'internal'
ARTIFACT_TYPE_AX_LOG = 'ax-log'
ARTIFACT_TYPE_AX_LOG_EXTERNAL = 'ax-log-external'
ARTIFACT_TYPE_USER_LOG = 'user-log'
ARTIFACT_TYPE_EXPORTED = 'exported'


OPERATION_CREATE = 'create'
OPERATION_DELETE = 'delete'
OPERATION_RESTORE = 'restore'

ARTIFACT_DIR = '/ax/data/artifacts'

ARTIFACT_SIZE = 'artifact_size'
ARTIFACT_NUMS = 'artifact_nums'