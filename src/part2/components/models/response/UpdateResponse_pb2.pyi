from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateResponse(_message.Message):
    __slots__ = ("isUpdated",)
    ISUPDATED_FIELD_NUMBER: _ClassVar[int]
    isUpdated: int
    def __init__(self, isUpdated: _Optional[int] = ...) -> None: ...
