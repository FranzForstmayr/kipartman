# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.versioned_file_data import VersionedFileData
from .base_model_ import Model as BaseModel
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class VersionedFileStatus(BaseModel):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, source_path=None, storage_path=None, md5=None, version=None, state=None, updated=None, id=None, status=None):
        """
        VersionedFileStatus - a model defined in Swagger

        :param source_path: The source_path of this VersionedFileStatus.
        :type source_path: str
        :param storage_path: The storage_path of this VersionedFileStatus.
        :type storage_path: str
        :param md5: The md5 of this VersionedFileStatus.
        :type md5: str
        :param version: The version of this VersionedFileStatus.
        :type version: int
        :param state: The state of this VersionedFileStatus.
        :type state: str
        :param updated: The updated of this VersionedFileStatus.
        :type updated: datetime
        :param id: The id of this VersionedFileStatus.
        :type id: int
        :param status: The status of this VersionedFileStatus.
        :type status: int
        """
        self.swagger_types = {
            'source_path': str,
            'storage_path': str,
            'md5': str,
            'version': int,
            'state': str,
            'updated': datetime,
            'id': int,
            'status': int
        }

        self.attribute_map = {
            'source_path': 'source_path',
            'storage_path': 'storage_path',
            'md5': 'md5',
            'version': 'version',
            'state': 'state',
            'updated': 'updated',
            'id': 'id',
            'status': 'status'
        }

        self._source_path = source_path
        self._storage_path = storage_path
        self._md5 = md5
        self._version = version
        self._state = state
        self._updated = updated
        self._id = id
        self._status = status

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VersionedFileStatus of this VersionedFileStatus.
        :rtype: VersionedFileStatus
        """
        return deserialize_model(dikt, cls)

    @property
    def source_path(self):
        """
        Gets the source_path of this VersionedFileStatus.

        :return: The source_path of this VersionedFileStatus.
        :rtype: str
        """
        return self._source_path

    @source_path.setter
    def source_path(self, source_path):
        """
        Sets the source_path of this VersionedFileStatus.

        :param source_path: The source_path of this VersionedFileStatus.
        :type source_path: str
        """

        self._source_path = source_path

    @property
    def storage_path(self):
        """
        Gets the storage_path of this VersionedFileStatus.

        :return: The storage_path of this VersionedFileStatus.
        :rtype: str
        """
        return self._storage_path

    @storage_path.setter
    def storage_path(self, storage_path):
        """
        Sets the storage_path of this VersionedFileStatus.

        :param storage_path: The storage_path of this VersionedFileStatus.
        :type storage_path: str
        """

        self._storage_path = storage_path

    @property
    def md5(self):
        """
        Gets the md5 of this VersionedFileStatus.

        :return: The md5 of this VersionedFileStatus.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """
        Sets the md5 of this VersionedFileStatus.

        :param md5: The md5 of this VersionedFileStatus.
        :type md5: str
        """

        self._md5 = md5

    @property
    def version(self):
        """
        Gets the version of this VersionedFileStatus.

        :return: The version of this VersionedFileStatus.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this VersionedFileStatus.

        :param version: The version of this VersionedFileStatus.
        :type version: int
        """

        self._version = version

    @property
    def state(self):
        """
        Gets the state of this VersionedFileStatus.

        :return: The state of this VersionedFileStatus.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this VersionedFileStatus.

        :param state: The state of this VersionedFileStatus.
        :type state: str
        """

        self._state = state

    @property
    def updated(self):
        """
        Gets the updated of this VersionedFileStatus.

        :return: The updated of this VersionedFileStatus.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this VersionedFileStatus.

        :param updated: The updated of this VersionedFileStatus.
        :type updated: datetime
        """

        self._updated = updated

    @property
    def id(self):
        """
        Gets the id of this VersionedFileStatus.

        :return: The id of this VersionedFileStatus.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VersionedFileStatus.

        :param id: The id of this VersionedFileStatus.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def status(self):
        """
        Gets the status of this VersionedFileStatus.

        :return: The status of this VersionedFileStatus.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this VersionedFileStatus.

        :param status: The status of this VersionedFileStatus.
        :type status: int
        """

        self._status = status

