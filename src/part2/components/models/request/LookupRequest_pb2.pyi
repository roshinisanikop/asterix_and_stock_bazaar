from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LookupRequest(_message.Message):
    __slots__ = ("stockName",)
    STOCKNAME_FIELD_NUMBER: _ClassVar[int]
    stockName: str
    def __init__(self, stockName: _Optional[str] = ...) -> None: ...
