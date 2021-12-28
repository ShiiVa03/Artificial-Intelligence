class AlreadyExistsException(Exception):
    pass

class CourierAlreadyExistsException(AlreadyExistsException):
    pass

class StreetDoesntExistException(Exception):
    pass

class TimeFormatError(Exception):
    pass


class TransportException(Exception):
    pass

class TransportWeightException(TransportException):
    pass