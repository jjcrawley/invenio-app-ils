# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# invenio-app-ils is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio App ILS Records views."""

from __future__ import absolute_import, print_function

from flask import Blueprint, abort, current_app, jsonify, request
from invenio_accounts.views.rest import UserInfoView, default_user_payload
from invenio_files_rest.models import ObjectVersion
from invenio_files_rest.signals import file_downloaded
from invenio_records_rest.utils import obj_or_import_string
from invenio_records_rest.views import pass_record
from invenio_rest import ContentNegotiatedMethodView

from invenio_app_ils.documents.api import DOCUMENT_PID_TYPE
from invenio_app_ils.errors import StatsError
from invenio_app_ils.pidstore.pids import EITEM_PID_TYPE
from invenio_app_ils.signals import record_viewed


class UserInfoResource(UserInfoView):
    """Retrieve current user's information."""

    def response(self, user):
        """Return response with current user's information."""
        user_payload = default_user_payload(user)
        user_payload["roles"] = [role.name for role in user.roles]
        user_payload.update(
            dict(
                locationPid=current_app.config["ILS_DEFAULT_LOCATION_PID"],
                username=user.email
            ))
        return jsonify(user_payload), 200


def create_document_stats_blueprint(app):
    """Create document stats blueprint."""
    blueprint = Blueprint("ils_document_stats", __name__, url_prefix="")
    endpoints = app.config.get("RECORDS_REST_ENDPOINTS", [])

    def register_view(pid_type):
        options = endpoints.get(pid_type, {})
        default_media_type = options.get("default_media_type", "")
        rec_serializers = options.get("record_serializers", {})
        serializers = {
            mime: obj_or_import_string(func)
            for mime, func in rec_serializers.items()
        }

        stats_view = DocumentStatsResource.as_view(
            DocumentStatsResource.view_name.format(pid_type),
            serializers=serializers,
            default_media_type=default_media_type,
        )
        blueprint.add_url_rule(
            "{0}/stats".format(options["item_route"]),
            view_func=stats_view,
            methods=["POST"],
        )

    register_view(DOCUMENT_PID_TYPE)
    register_view(EITEM_PID_TYPE)
    return blueprint


class DocumentStatsResource(ContentNegotiatedMethodView):
    """Document stats resource."""

    view_name = "{}_stats"

    @pass_record
    def post(self, pid, record, **kwargs):
        """Send a signal to count record view for the record stats."""
        data = request.get_json()
        event_name = data.get("event")
        if event_name == "record-view":
            record_viewed.send(
                current_app._get_current_object(), pid=pid, record=record,
            )
            return self.make_response(pid, record, 202)
        elif event_name == "file-download":
            if "key" not in data:
                abort(406, "File key is required")
            if "bucket_id" not in record:
                abort(406, "Record has no bucket")
            obj = ObjectVersion.get(record["bucket_id"], data["key"])
            file_downloaded.send(
                current_app._get_current_object(), obj=obj, record=record
            )
            return self.make_response(pid, record, 202)
        return StatsError(
            description="Invalid stats event request: {}".format(event_name)
        )
