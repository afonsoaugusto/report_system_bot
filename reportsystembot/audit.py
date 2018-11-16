import functools
import logging
import time


#parametros de configuração do logger
def timed(logger, level=None, format='%s: %s ms'):
    if level is None:
        level = logging.DEBUG

    def decorator(fn):
        @functools.wraps(fn)
        def inner(self_bot,bot,update,*args, **kwargs):
            start = time.time()
            result = fn(self_bot,bot,update,*args, **kwargs)
            duration = time.time() - start
            print('Args ------- ', *args)
            print('self_bot ------- ', type(self_bot))
            print('Bot ------- ', type(bot))
            print('Updater -   ---- -- ',type(update))
            #print('type', [ type(x) for x in args[2]])
            logger.log(level, format, repr(fn), duration * 1000)
            return result
        return inner

    return decorator
