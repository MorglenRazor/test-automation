import logging


def before_all(context):
    context.config.setup_logging()
    # -- SAME-AS:
    logging.basicConfig(level=context.config.logging_level)
