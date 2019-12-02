# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# invenio-app-ils is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio App ILS."""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()

invenio_db_version = ">=1.0.4,<1.1.0"
invenio_search_version = "1.2.3,<1.3.0"

tests_require = [
    "check-manifest>=0.35",
    "coverage>=4.4.1",
    "isort>=4.3.11",
    "mock>=2.0.0",
    "pydocstyle>=2.0.0",
    "pytest-cov>=2.5.1",
    "pytest-invenio>=1.2.1,<1.3.0",
    "pytest-mock>=1.6.0",
    "pytest-pep8>=1.0.6",
    "pytest-random-order>=0.5.4",
    "pytest>=3.8.1,<4",
]

extras_require = {
    "docs": ["Sphinx>=1.5.1"],
    "lorem": ["lorem>=0.1.1 "],
    "tests": tests_require,
    "elasticsearch6": [
        "invenio-search[elasticsearch6]>={}".format(invenio_search_version),
    ],
    "elasticsearch7": [
        "invenio-search[elasticsearch7]>={}".format(invenio_search_version),
    ],
    "postgresql": [
        "invenio-db[postgresql,versioning]{}".format(invenio_db_version),
    ],
    "mysql": [
        "invenio-db[mysql,versioning]{}".format(invenio_db_version),
    ],
    "sqlite": [
        "invenio-db[versioning]{}".format(invenio_db_version),
    ],
    "vocabulary": [
        "pycountry>=19.8.18",
    ],
}

extras_require["all"] = []
for name, reqs in extras_require.items():
    if name in (
        "mysql",
        "posgresql",
        "sqlite",
        "elasticsearch6",
        "elasticsearch7",
        "vocabulary",
    ):
        continue
    extras_require["all"].extend(reqs)

setup_requires = ["Babel>=2.4.0", "pytest-runner>=3.0.0,<5"]

install_requires = [
    "arrow>=0.15.0",
    "Flask-BabelEx>=0.9.3",
    "Flask-Debugtoolbar>=0.10.1",
    "invenio[base,auth]==3.2.0a9",
    # metadata bundle without records UI
    "invenio-indexer>=1.1.0,<1.2.0",
    "invenio-jsonschemas>=1.0.0,<1.1.0",
    "invenio-pidstore>=1.0.0,<1.1.0",
    "invenio-records-rest>=1.6.1,<1.7.0",
    "invenio-records>=1.3.0,<1.4.0",
    # upgraded packages
    "invenio-accounts-rest>=1.0.0a4,<1.1.0",
    "invenio-app>=1.2.3,<1.3.0",
    "invenio-assets>=1.1.3,<1.2.0",
    "invenio-i18n>=1.1.0,<1.2.0",
    "invenio-userprofiles>=1.0.1,<1.1.0",
    # extra
    "invenio-circulation>=1.0.0a19,<1.1.0",
    "invenio-stats>=1.0.0a15",
    "invenio-pidrelations>=1.0.0a6,<1.1.0",
    "invenio-opendefinition>=1.0.0a9,<1.1.0",
    "sentry-sdk>=0.10.2",
    # until flask-sqlalchemy is fixed
    "SQLAlchemy>=1.2.16,<1.3.0",
    # namedtuple are json serialized as dict
    "simplejson>=3",
    "invenio-files-rest>=1.0.6,<1.1.0",
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("invenio_app_ils", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="invenio_app_ils",
    version=version,
    description=__doc__,
    long_description=readme,
    tags="invenio_app_ils Invenio",
    license="MIT",
    author="CERN",
    author_email="info@inveniosoftware.org",
    url="https://github.com/invenio_app_ils/invenio_app_ils",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={
        "console_scripts": ["ils = invenio_app.cli:cli"],
        "flask.commands": [
            "demo = invenio_app_ils.cli:demo",
            "patrons = invenio_app_ils.cli:patrons",
            "setup = invenio_app_ils.cli:setup",
            'stats = invenio_stats.cli:stats',
            "vocabulary = invenio_app_ils.vocabularies.cli:vocabulary",
        ],
        "invenio_base.apps": [
            "ils_ui = invenio_app_ils.ext:InvenioAppIlsUI"
        ],
        "invenio_base.api_apps": [
            "ils_rest = invenio_app_ils.ext:InvenioAppIlsREST"
        ],
        "invenio_base.api_blueprints": [
            "ils_circulation = invenio_app_ils.circulation.views:create_circulation_blueprint",
            "ils_circulation_stats = invenio_app_ils.circulation.stats.views:create_circulation_stats_blueprint",
            "ils_relations = invenio_app_ils.records_relations.views:create_relations_blueprint",
            "ils_document_request = invenio_app_ils.records.views:create_document_request_action_blueprint",
            "ils_document_stats = invenio_app_ils.records.views:create_document_stats_blueprint",
            "ils_files = invenio_app_ils.files.views:create_files_blueprint",
        ],
        "invenio_config.module": [
            "00_invenio_app_ils = invenio_app_ils.config"
        ],
        "invenio_i18n.translations": ["messages = invenio_app_ils"],
        "invenio_jsonschemas.schemas": [
            "ils_schemas = invenio_app_ils.schemas",
            "acquisition_schemas = invenio_app_ils.acquisition.schemas"
        ],
        "invenio_search.mappings": [
            "document_requests = invenio_app_ils.mappings",
            "documents = invenio_app_ils.mappings",
            "eitems = invenio_app_ils.mappings",
            "internal_locations = invenio_app_ils.mappings",
            "items = invenio_app_ils.mappings",
            "locations = invenio_app_ils.mappings",
            "patrons = invenio_app_ils.mappings",
            "series = invenio_app_ils.mappings",
            "vocabularies = invenio_app_ils.mappings",
            "vendors = invenio_app_ils.acquisition.mappings",
            "orders = invenio_app_ils.acquisition.mappings"
        ],
        "invenio_pidstore.fetchers": [
            "docid = invenio_app_ils.pidstore.fetchers:document_pid_fetcher",
            "dreqid = invenio_app_ils.pidstore.fetchers:document_request_pid_fetcher",
            "eitmid = invenio_app_ils.pidstore.fetchers:eitem_pid_fetcher",
            "ilocid = invenio_app_ils.pidstore.fetchers:internal_location_pid_fetcher",
            "locid = invenio_app_ils.pidstore.fetchers:location_pid_fetcher",
            "patid = invenio_app_ils.pidstore.fetchers:patron_pid_fetcher",
            "pitmid = invenio_app_ils.pidstore.fetchers:item_pid_fetcher",
            "serid = invenio_app_ils.pidstore.fetchers:series_pid_fetcher",
            "vocid = invenio_app_ils.pidstore.fetchers:vocabulary_pid_fetcher",
            "acqvid = invenio_app_ils.acquisition.pidstore.fetchers:vendor_pid_fetcher",
            "acqoid = invenio_app_ils.acquisition.pidstore.fetchers:order_pid_fetcher",
        ],
        "invenio_pidstore.minters": [
            "docid = invenio_app_ils.pidstore.minters:document_pid_minter",
            "dreqid = invenio_app_ils.pidstore.minters:document_request_pid_minter",
            "eitmid = invenio_app_ils.pidstore.minters:eitem_pid_minter",
            "ilocid = invenio_app_ils.pidstore.minters:internal_location_pid_minter",
            "locid = invenio_app_ils.pidstore.minters:location_pid_minter",
            "patid = invenio_app_ils.pidstore.minters:patron_pid_minter",
            "pitmid = invenio_app_ils.pidstore.minters:item_pid_minter",
            "serid = invenio_app_ils.pidstore.minters:series_pid_minter",
            "vocid = invenio_app_ils.pidstore.minters:vocabulary_pid_minter",
            "acqvid = invenio_app_ils.acquisition.pidstore.minters:vendor_pid_minter",
            "acqoid = invenio_app_ils.acquisition.pidstore.minters:order_pid_minter",

        ],
        "invenio_access.actions": [
            "backoffice_access_action = "
            "invenio_app_ils.permissions:backoffice_access_action"
        ],
        "invenio_records.jsonresolver": [
            "document_circulation = invenio_app_ils.records.resolver.jsonresolver.document_circulation",
            "document_eitem = invenio_app_ils.records.resolver.jsonresolver.document_eitem",
            "document_item = invenio_app_ils.records.resolver.jsonresolver.document_item",
            "document_relations = invenio_app_ils.records.resolver.jsonresolver.document_relations",
            "document_request = invenio_app_ils.records.resolver.jsonresolver.document_request",
            "document_request_patron = invenio_app_ils.records.resolver.jsonresolver.document_request_patron",
            "document_stock = invenio_app_ils.records.resolver.jsonresolver.document_stock",
            "eitem = invenio_app_ils.records.resolver.jsonresolver.eitem",
            "eitem_files = invenio_app_ils.records.resolver.jsonresolver.eitem_files",
            "internal_location = invenio_app_ils.records.resolver.jsonresolver.internal_location",
            "item_document = invenio_app_ils.records.resolver.jsonresolver.item_document",
            "item_internal_location = invenio_app_ils.records.resolver.jsonresolver.item_internal_location",
            "item_loan = invenio_app_ils.records.resolver.jsonresolver.item_loan",
            "request_document = invenio_app_ils.records.resolver.jsonresolver.request_document",
            "series_relations = invenio_app_ils.records.resolver.jsonresolver.series_relations",
        ],
        "invenio_celery.tasks": [
            "indexer = invenio_app_ils.indexer"
        ]
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    python_requires=">=3",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Development Status :: 3 - Alpha",
    ],
)
