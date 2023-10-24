from clu.clu import CLU

log = CLU(
        name=__name__,
        log_level='info',
        log_to_file=True,
        log_file_path='some/dir/nested',
        log_file_name='log_file.log'
    ).get_logger()

if __name__ == '__main__':
    log.info('now?', extra={'id': '123'})
