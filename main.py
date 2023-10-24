from clu.clu import CLU

log = CLU(
        name=__name__,
        log_level='info',
        log_to_file=True,
        log_file_path='some/logging/dir',
        log_file_name='app.log'
    ).get_logger()

if __name__ == '__main__':
    log.info('now?', extra={'id': '123'})


