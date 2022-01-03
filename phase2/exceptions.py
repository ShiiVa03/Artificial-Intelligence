class AlreadyExistsException(Exception):
    pass

class CourierAlreadyExistsException(AlreadyExistsException):
    pass

class StreetAlreadyExistsException(AlreadyExistsException):
    pass

class StreetDoesntExistException(Exception):
    pass

class TimeFormatError(Exception):
    pass

class TransportException(Exception):
    pass

class TransportWeightException(TransportException):
    pass

class ConnectionDistHigherThanEuclidian(Exception):
    pass

class NoAvailableCouriers(Exception):
    pass

class CircuitAlreadyInProgress(Exception):
    pass

class CircuitIsNotInProgress(Exception):
    pass

class CourierNotBusy(Exception):
    pass

class NoPathForCircuitTransport(Exception):
    pass

class NoPossibleCircuit(Exception):
    pass
