from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PredefinedFilterField")


@_attrs_define
class PredefinedFilterField:
    """Represents a predefined field of the issue. Predefined fields are always present in an issue and
            |cannot be customized in a project. For example, `project`, `created`,
            |`updated`, `tags`, and so on.

    Attributes:
        id (Union[Unset, str]):
        presentation (Union[Unset, str]):
        name (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    presentation: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        presentation = self.presentation
        name = self.name
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if presentation is not UNSET:
            field_dict["presentation"] = presentation
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["$type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        presentation = d.pop("presentation", UNSET)

        name = d.pop("name", UNSET)

        type = d.pop("$type", UNSET)

        predefined_filter_field = cls(
            id=id,
            presentation=presentation,
            name=name,
            type=type,
        )

        predefined_filter_field.additional_properties = d
        return predefined_filter_field

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
