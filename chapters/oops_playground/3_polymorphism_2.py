# polymorphism is a single common shared interface or a method name shared by multiple objects and the bheviour of that method depends on the implmentation done at each of those object's inheritance hierarchy chain
# all the objects have same fixed flow but different behaviours

# a single program can then make use of the common interface to write a code such that it can process multiple objects focussing on the sequence of the program rather than the implementation behviour.

# A program that processes data from different file systems or network system is a good example to see polymorphims in action


def process(input_system, processor):
    data = input_system.read()  # read method is the shared interface among different file system to read thier files. they decide what goes into the read but have agreed that they will use read as the interface

    processed_data = processor(
        data
    )  # here it is understood that processor is common to all the data coming form multiple file systems or network systems. the processor can also be based on each systems own bheviour. we can expand on that a bit later.

    result = input_system.write(
        processed_data
    )  # write is the method shared as common interface among different system. again, each one of the system has implemented their own way of doing it

    return result


# differnt systems working with single program

# a single interface contract


class ReaderWriter:  # this superclass defines the contract or the common interface that other systems promise to honour
    def read(self):
        raise NotImplementedError

    def write(self, data):
        raise NotImplementedError


# class for file reader object
class FileReader(ReaderWriter):
    def read(self): ...
    def write(self, data): ...


# class for socket reader object
class SocketReader(ReaderWriter):
    def read(self): ...
    def write(self, data): ...


# class for network reader object
class NetworkReader(ReaderWriter):
    def read(self): ...
    def write(self, data): ...


# creating the multiple distinct file objects that can be passed into the system
fr = FileReader()
sr = SocketReader()
nr = NetworkReader()


# desing the processor method to process the data
def processor(data):
    pass


#  call the the process program for all different objects
fr_result = process(fr, processor)
sr_result = process(sr, processor)
nr_result = process(nr, processor)
