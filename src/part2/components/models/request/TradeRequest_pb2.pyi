from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TradeRequest(_message.Message):
    __slots__ = ("stockName", "itemSize", "type")
    STOCKNAME_FIELD_NUMBER: _ClassVar[int]
    ITEMSIZE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    stockName: str
    itemSize: int
    type: str
    def __init__(self, stockName: _Optional[str] = ..., itemSize: _Optional[int] = ..., type: _Optional[str] = ...) -> None: ...
