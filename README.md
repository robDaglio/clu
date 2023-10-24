# Custom Logging Utility (CLU)
Essentially, just a simple, easy-to-user logger that can be added to any project.

## Example Usage

This is a logging utility that essentially streamlines the process of creating and
initializing custom logging functionality.

The object can be initialized within a single statement. In this example, the module
resides at the root of the project and can be imported and defined like this:
```
from clu.clu import CLU

log = CLU(
        name=__name__,
        log_level='info',
        log_to_file=True,
        log_file_path='some/logging/dir',
        log_file_name='app.log'
    ).get_logger()

if __name__ == '__main__':
    log.info('This is test', extra={'id': '123'})
```