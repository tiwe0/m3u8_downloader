from collections import namedtuple
import itertools
EXTINF = namedtuple("EXTINF", ["index", "duration", "ts"])

class M3U8:
    def __init__(self, file_handler_or_text):
        self._build(file_handler_or_text)

    def _build(self, file_handler_or_text):
        if isinstance(file_handler_or_text, str):
            text = file_handler_or_text
        else:
            text = file_handler_or_text.read()
        m3u8_list = [line.strip() for line in text.split("#")]
        self.m3u8_extinf_list = self._parse_extinf(m3u8_list)
        self.m3u8_ext_x_key_dict = self._parse_ext_x_key(m3u8_list)

    @staticmethod
    def _parse_ext_x_key(m3u8_list: list):
        m3u8_ext_x_key_dict = {}
        for line in m3u8_list:
            if 'EXT-X-KEY' in line:
                key_details_list = line.split(':')[-1].split(',')
                for kv in key_details_list:
                    key, val = kv.split('=')
                    m3u8_ext_x_key_dict[key] = val.replace('"', '')
        return m3u8_ext_x_key_dict

    @staticmethod
    def _parse_extinf(m3u8_list: list):
        tmp = [line.split(':')[-1].split(',\n') for line in m3u8_list if 'EXTINF' in line]
        result = []
        for i in zip(itertools.count(1), tmp):
            result.append(EXTINF(i[0], i[1][0], i[1][1]))
        return result

    @property
    def ext_x_key(self):
        return self.m3u8_ext_x_key_dict

    @property
    def extinf(self):
        return self.m3u8_extinf_list
