# Author: Simone Orsi
# Copyright 2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ImportSourceConsumerMixin(models.AbstractModel):
    _inherit = "import.source.consumer.mixin"

    @api.model
    def _selection_source_ref_id(self):
        return = super()._selection_source_ref_id() + [("import.source.external.db", "External Database")]
