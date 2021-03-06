# -*- coding: utf-8 -*-
#
# Copyright (C) 2018-2019 CERN.
#
# invenio-app-ils is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Document schema for marshmallow loader."""

from invenio_records_rest.schemas import RecordMetadataSchemaJSONV1
from marshmallow import EXCLUDE, Schema, fields


class IdentifierSchema(Schema):
    """Identifier schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    material = fields.Str()
    scheme = fields.Str(required=True)
    value = fields.Str(required=True)


class AffiliationSchema(Schema):
    """Affiliation schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    identifiers = fields.List(fields.Nested(IdentifierSchema))
    name = fields.Str(required=True)


class AuthorSchema(Schema):
    """Author schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    affiliations = fields.List(fields.Nested(AffiliationSchema))
    alternative_names = fields.List(fields.Str())
    full_name = fields.Str(required=True)
    identifiers = fields.List(fields.Nested(IdentifierSchema))
    roles = fields.List(fields.Str())
    type = fields.Str()


class UrlSchema(Schema):
    """URL schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    description = fields.Str()
    value = fields.URL(required=True)


class AlternativeTitleSchema(Schema):
    """Alternative title schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    language = fields.Str()
    source = fields.Str()
    value = fields.Str(required=True)
    type = fields.Str()


class ConferenceInfoSchema(Schema):
    """Conference info schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    acronym = fields.Str()
    country = fields.Str()
    dates = fields.Str()
    identifiers = fields.List(fields.Nested(IdentifierSchema))
    place = fields.Str(required=True)
    series = fields.Str()
    title = fields.Str(required=True)
    year = fields.Int()


class CopyrightsSchema(Schema):
    """Copyright schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    holder = fields.Str()
    material = fields.Str()
    statement = fields.Str()
    url = fields.Str()
    year = fields.Int()


class ImprintSchema(Schema):
    """Imprint schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    date = fields.Str()
    place = fields.Str()
    publisher = fields.Str()
    reprint_date = fields.Str()


class InternalNoteSchema(Schema):
    """Internal note schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    field = fields.Str()
    user = fields.Str()
    value = fields.Str(required=True)


class KeywordSchema(Schema):
    """Keyword schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    source = fields.Str()
    value = fields.Str()


class SubjectSchema(Schema):
    """Subject schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    scheme = fields.Str(required=True)
    value = fields.Str(required=True)


class PublicationInfoSchema(Schema):
    """Publication info schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    artid = fields.Str()
    journal_issue = fields.Str()
    journal_title = fields.Str()
    journal_volume = fields.Str()
    note = fields.Str()
    pages = fields.Str()
    year = fields.Int()


class ChangeBySchema(Schema):
    """Change by schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    type = fields.Str()
    value = fields.Str()


class DocumentSchemaV1(RecordMetadataSchemaJSONV1):
    """Document schema."""

    class Meta:
        """Meta attributes for the schema."""

        unknown = EXCLUDE

    abstract = fields.Str()
    alternative_abstracts = fields.List(fields.Str())
    alternative_identifiers = fields.List(fields.Nested(IdentifierSchema))
    alternative_titles = fields.List(fields.Nested(AlternativeTitleSchema))
    authors = fields.List(fields.Nested(AuthorSchema), required=True)
    conference_info = fields.Nested(ConferenceInfoSchema)
    copyrights = fields.List(fields.Nested(CopyrightsSchema))
    created_by = fields.Nested(ChangeBySchema)
    curated = fields.Bool()
    document_type = fields.Str()
    edition = fields.Str()
    identifiers = fields.List(fields.Nested(IdentifierSchema))
    imprint = fields.Nested(ImprintSchema)
    internal_notes = fields.List(fields.Nested(InternalNoteSchema))
    keywords = fields.Nested(KeywordSchema)
    languages = fields.List(fields.Str())
    licenses = fields.List(fields.Str())
    note = fields.Str()
    number_of_pages = fields.Str()
    open_access = fields.Bool(default=True)
    other_authors = fields.Bool()
    publication_info = fields.List(fields.Nested(PublicationInfoSchema))
    publication_year = fields.Str()
    source = fields.Str()
    subjects = fields.List(fields.Nested(SubjectSchema))
    table_of_content = fields.List(fields.Str())
    tags = fields.List(fields.Str())
    title = fields.Str(required=True)
    updated_by = fields.Nested(ChangeBySchema)
    urls = fields.List(fields.Nested(UrlSchema))
