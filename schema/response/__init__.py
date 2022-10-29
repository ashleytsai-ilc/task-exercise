from typing import Generic, TypeVar
from pydantic.generics import GenericModel

DataT = TypeVar('DataT')


class MultiResponse(GenericModel, Generic[DataT]):
    result: list[DataT]

class Response(GenericModel, Generic[DataT]):
    result: DataT
