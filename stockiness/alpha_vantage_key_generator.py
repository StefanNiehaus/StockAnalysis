from time import sleep


class AlphaVantageKey:
    KEYS = ['DLZDZ17ZROZZI32J', 'JMUUR8C1U3W2I6G5']

    def get_key_generator(self):
        """
        Usage:
        for key in self.get_keys():
            print(key)

        :rtype: Generator object with keys.
        """
        index = 0
        while self.KEYS:
            yield self.KEYS[index]
            index = (index + 1) % len(self.KEYS)


if __name__ == '__main__':
    keys = AlphaVantageKey()
    for key in keys.get_key_generator():
        print(key)
        sleep(1)
