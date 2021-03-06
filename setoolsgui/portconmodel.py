# Copyright 2016, Tresys Technology, LLC
#
# This file is part of SETools.
#
# SETools is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 2.1 of
# the License, or (at your option) any later version.
#
# SETools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with SETools.  If not, see
# <http://www.gnu.org/licenses/>.
#
from collections import defaultdict

from PyQt5.QtCore import Qt

from .models import SEToolsTableModel


class PortconTableModel(SEToolsTableModel):

    """Table-based model for portcons."""

    headers = defaultdict(str, {0: "Port/Port Range", 1: "Protocol", 2: "Context"})

    def data(self, index, role):
        if self.resultlist and index.isValid():
            row = index.row()
            col = index.column()
            rule = self.resultlist[row]

            if role == Qt.DisplayRole:
                if col == 0:
                    low, high = rule.ports
                    if low == high:
                        return str(low)
                    else:
                        return "{0}-{1}".format(low, high)
                elif col == 1:
                    return str(rule.protocol)
                elif col == 2:
                    return str(rule.context)

            elif role == Qt.UserRole:
                return rule
