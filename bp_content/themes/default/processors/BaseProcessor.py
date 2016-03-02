from bp_content.themes.default.handlers import models

class BaseProcessor(object):
    def __init__(self, data):
        self._data = data

    # Quick initial sanity check of data. If this is no less expensive then processing the data it could either just
    # return true or preprocess it.
    def handles_format(self):
        return False

    # process data
    def process(self):
        raise NotImplementedError('Processing of this format not implemented.')

    def storeDataPoint(self, path, value, units):
        path = models.DataPath.get_or_insert(path,units=units)
        data = models.DataPoint(path=path.key, value=value, when=self._data['time'])
        data.put()
