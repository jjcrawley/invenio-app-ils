# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# invenio-app-ils is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Invenio App ILS Document Request Acccept loader JSON schema."""

from invenio_records_rest.schemas import RecordMetadataSchemaJSONV1
from marshmallow import EXCLUDE, fields

from .document_request import PhysicalItemProviderSchema


class DocumentRequestAcceptSchemaV1(RecordMetadataSchemaJSONV1):
    """Document Request Accept schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    document_pid = fields.Str()
    physical_item_provider = fields.Nested(PhysicalItemProviderSchema)
    state = fields.Str()
