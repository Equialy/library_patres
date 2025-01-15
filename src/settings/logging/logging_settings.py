import os
import sys

from .log_filters import DebugWarningLogFilter, CriticalLogFilter, ErrorLogFilter

log_dir = os.path.join(os.path.dirname(__file__), "log")
os.makedirs(log_dir, exist_ok=True)

logging_config = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': '#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
        },
        'detailed': {  # Форматтер для подробного логирования
                'format': '[%(asctime)s] #%(levelname)-8s %(filename)s:'
                          '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
            },
        'formatter_1': {
            'format': '[%(asctime)s] #%(levelname)-8s %(filename)s:'
                      '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_2': {
            'format': '#%(levelname)-8s [%(asctime)s] - %(filename)s:'
                      '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_3': {
            'format': '#%(levelname)-8s [%(asctime)s] - %(message)s'
        }
    },
    'filters': {
        'critical_filter': {
            '()': CriticalLogFilter,
        },
        'error_filter': {
            '()': ErrorLogFilter,
        },
        'debug_warning_filter': {
            '()': DebugWarningLogFilter,
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'INFO',
            'stream': sys.stdout,
        },
        'info_file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(log_dir, 'info.log'),
            'mode': 'a',
            'formatter': 'detailed',
            'level': 'INFO',
        },
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'stderr': {
            'class': 'logging.StreamHandler',
        },
        'stdout': {
            'class': 'logging.StreamHandler',
            'formatter': 'formatter_2',
            'filters': ['debug_warning_filter'],
            'stream': sys.stdout
        },
        'error_file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(log_dir, 'error.log'),
            'mode': 'w',
            'level': 'DEBUG',
            'formatter': 'formatter_1',
            'filters': ['error_filter']
        },
        'critical_file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(log_dir, 'critical.log'),
            'mode': 'w',
            'formatter': 'formatter_3',
            'filters': ['critical_filter']
        }
    },
    'loggers': {
        'authors_logger': {
            'level': 'INFO',
            'handlers': ['console', 'info_file', 'error_file', 'critical_file']

        },
        'module_2': {
            'handlers': ['stdout']
        },
        'module_3': {
            'handlers': ['stderr', 'critical_file']
        }
    },
    'root': {
        'formatter': 'INFO',
        'handlers': ['console', 'info_file'],
    }
}