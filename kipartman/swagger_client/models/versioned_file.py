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


class VersionedFile(object):
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
        'source_path': 'str',
        'storage_path': 'str',
        'md5': 'str',
        'version': 'int',
        'state': 'str',
        'updated': 'datetime',
        'id': 'int'
    }

    attribute_map = {
        'source_path': 'source_path',
        'storage_path': 'storage_path',
        'md5': 'md5',
        'version': 'version',
        'state': 'state',
        'updated': 'updated',
        'id': 'id'
    }

    def __init__(self, source_path=None, storage_path=None, md5=None, version=None, state=None, updated=None, id=None):
        """
        VersionedFile - a model defined in Swagger
        """

        self._source_path = None
        self._storage_path = None
        self._md5 = None
        self._version = None
        self._state = None
        self._updated = None
        self._id = None

        if source_path is not None:
          self.source_path = source_path
        if storage_path is not None:
          self.storage_path = storage_path
        if md5 is not None:
          self.md5 = md5
        if version is not None:
          self.version = version
        if state is not None:
          self.state = state
        if updated is not None:
          self.updated = updated
        if id is not None:
          self.id = id

    @property
    def source_path(self):
        """
        Gets the source_path of this VersionedFile.

        :return: The source_path of this VersionedFile.
        :rtype: str
        """
        return self._source_path

    @source_path.setter
    def source_path(self, source_path):
        """
        Sets the source_path of this VersionedFile.

        :param source_path: The source_path of this VersionedFile.
        :type: str
        """

        self._source_path = source_path

    @property
    def storage_path(self):
        """
        Gets the storage_path of this VersionedFile.

        :return: The storage_path of this VersionedFile.
        :rtype: str
        """
        return self._storage_path

    @storage_path.setter
    def storage_path(self, storage_path):
        """
        Sets the storage_path of this VersionedFile.

        :param storage_path: The storage_path of this VersionedFile.
        :type: str
        """

        self._storage_path = storage_path

    @property
    def md5(self):
        """
        Gets the md5 of this VersionedFile.

        :return: The md5 of this VersionedFile.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """
        Sets the md5 of this VersionedFile.

        :param md5: The md5 of this VersionedFile.
        :type: str
        """

        self._md5 = md5

    @property
    def version(self):
        """
        Gets the version of this VersionedFile.

        :return: The version of this VersionedFile.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this VersionedFile.

        :param version: The version of this VersionedFile.
        :type: int
        """

        self._version = version

    @property
    def state(self):
        """
        Gets the state of this VersionedFile.

        :return: The state of this VersionedFile.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this VersionedFile.

        :param state: The state of this VersionedFile.
        :type: str
        """

        self._state = state

    @property
    def updated(self):
        """
        Gets the updated of this VersionedFile.

        :return: The updated of this VersionedFile.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this VersionedFile.

        :param updated: The updated of this VersionedFile.
        :type: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """
        Gets the id of this VersionedFile.

        :return: The id of this VersionedFile.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VersionedFile.

        :param id: The id of this VersionedFile.
        :type: int
        """

        self._id = id

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
        if not isinstance(other, VersionedFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
