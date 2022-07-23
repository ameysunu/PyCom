import uos

class Nvs:
    def __init__(self, delimiter, file_size):
        self.max_file_size = file_size
        self.delimiter = delimiter
        self.file_path = '/flash/store.nvram'
        self.file_handle = None

    def empty(self):
        isEmpty = False
        try:
            if uos.stat(self.file_path)[6] == 0:
                isEmpty = True
        except Exception as e:
            isEmpty = True
        return isEmpty

    def full(self):
        isFull = True
        try:
            if uos.stat(self.file_path)[6] < self.max_file_size:
                isFull = False
        except Exception as e:
            isFull = False
        return isFull

    def open(self):
        if self.file_handle is None:
            self.file_handle = open(self.file_path, "a+")

    def close(self):
        if self.file_handle:
            self.file_handle.close()
            self.file_handle = None

    def store(self, data):
        if self.full():
            return False

        if self.file_handle is None:
            self.open()

        try:
            self.file_handle.write(data)
            self.file_handle.write(self.delimiter)
            self.file_handle.flush()
        except Exception as e:
            print("NVRAM: Exception storing data: " + str(e))
            return False
        return True

    def read_all(self):
        buf = ''

        if self.file_handle is None:
            self.open()

        try:
            self.file_handle.seek(0,0)
            buf = self.file_handle.read()
        except Exception as e:
            print("NVRAM: Exception reading file: " + str(e))

        return buf
