from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LookupResponse(_message.Message):
    __slots__ = ("price", "volume")
    PRICE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    price: int
    volume: int
    def __init__(self, price: _Optional[int] = ..., volume: _Optional[int] = ...) -> None: ...
