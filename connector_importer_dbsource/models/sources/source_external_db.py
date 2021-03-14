# Author: Simone Orsi
# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import base64

from odoo import api, fields, models

from ...utils.import_utils import CSVReader, guess_csv_metadata


class ExternalDBSource(models.Model):
    _name = "import.source.external.db"
    _inherit = "import.source"
    _description = "External DB import source"
    _source_type = "external_db"
    _reporter_model = "reporter.csv"

    csv_file = fields.Binary("CSV file")

    _csv_reader_klass = CSVReader

    @property
    def _config_summary_fields(self):
        _fields = super()._config_summary_fields
        print("-----------_fields:: ", _fields)
        return _fields + [
            "csv_file",
        ]

    def _get_lines(self):
        return [{
            "id": "xxx.111",
            "name": "2222222",
            "_line_nr": 1,
        },
        {
            "id": "xxx.222",
            "name": "333333333333",
            "_line_nr": 3,
        }]
