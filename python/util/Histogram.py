from collections.abc import Mapping


class Histogram(Mapping):
    """I implement a histogram, based on a dict. Thus, you can count anything
    hashable. Unlike dict, __getitem__ returns zero for a missing bucket, rather
    than raising an exception. The Container, Iterable, and Sized methods only
    consider actual buckets.
    """

    def __init__(self):
        super().__init__()
        self.dict = {}

    def count(self, bucket, n=1):
        if bucket in self.dict:
            self.dict[bucket] += n
        else:
            self.dict[bucket] = n

    def __getitem__(self, bucket):
        if bucket in self.dict:
            return self.dict.__getitem__(bucket)
        else:
            return 0

    def __len__(self):
        return self.dict.__len__()

    def __iter__(self):
        return self.dict.__iter__()

    def __str__(self):
        return self.dict.__str__()
