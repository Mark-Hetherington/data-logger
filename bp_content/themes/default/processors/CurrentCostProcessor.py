from XmlDataProcessor import XMLDataProcessor


class CurrentCostProcessor(XMLDataProcessor):
    def handles_format(self):
        XMLDataProcessor.handles_format(self)
        return self._xml is not None and self._xml.find('src') is not None and self._xml.find('src').text == 'CC128-v1.51'

    def process(self):
        sensor_id = self._xml.find('id').text
        type = self._xml.find('type').text
        if type != '1':
            raise ValueError('Sensor type "' + type + '" not supported.')
        channel_index = 1
        while (not self._xml.find('ch' + str(channel_index)) is None):
            channel = self._xml.find('ch' + str(channel_index))
            self.storeDataPoint('CC128/'+sensor_id+'/ch'+str(channel_index),int(channel.find('watts').text), 'W')
            channel_index += 1