# coding: utf-8

"""
    Kipartman

    Kipartman api specifications

    OpenAPI spec version: 1.0.0
    Contact: --
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PartAttachement(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'source_name': 'str',
        'storage_path': 'str',
        'id': 'int',
        'description': 'str'
    }

    attribute_map = {
        'source_name': 'source_name',
        'storage_path': 'storage_path',
        'id': 'id',
        'description': 'description'
    }

    def __init__(self, source_name=None, storage_path=None, id=None, description=None):
        """
        PartAttachement - a model defined in Swagger
        """

        self._source_name = None
        self._storage_path = None
        self._id = None
        self._description = None

        if source_name is not None:
          self.source_name = source_name
        if storage_path is not None:
          self.storage_path = storage_path
        self.id = id
        if description is not None:
          self.description = description

    @property
    def source_name(self):
        """
        Gets the source_name of this PartAttachement.

        :return: The source_name of this PartAttachement.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this PartAttachement.

        :param source_name: The source_name of this PartAttachement.
        :type: str
        """

        self._source_name = source_name

    @property
    def storage_path(self):
        """
        Gets the storage_path of this PartAttachement.

        :return: The storage_path of this PartAttachement.
        :rtype: str
        """
        return self._storage_path

    @storage_path.setter
    def storage_path(self, storage_path):
        """
        Sets the storage_path of this PartAttachement.

        :param storage_path: The storage_path of this PartAttachement.
        :type: str
        """

        self._storage_path = storage_path

    @property
    def id(self):
        """
        Gets the id of this PartAttachement.

        :return: The id of this PartAttachement.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PartAttachement.

        :param id: The id of this PartAttachement.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this PartAttachement.

        :return: The description of this PartAttachement.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PartAttachement.

        :param description: The description of this PartAttachement.
        :type: str
        """

        self._description = description

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PartAttachement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
