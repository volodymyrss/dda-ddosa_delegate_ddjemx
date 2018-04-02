import os
import ddosa
import ddjemx
import dataanalysis.caches.queue as queue

cache=queue.QueueCache(os.environ['DDA_QUEUE'])
cache.delegate_by_default=True

ddosa.CacheStack[-1].parent=cache
ddosa.CacheStack.append(cache)

class jemx_image(ddjemx.jemx_image):
    read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

class jemx_spe(ddjemx.jemx_spe):
    read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

class jemx_lcr(ddjemx.jemx_lcr):
    read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)

class spe_pick(ddjemx.spe_pick):
    read_caches=[queue.QueueCache]+list(ddosa.CatExtract.read_caches)


