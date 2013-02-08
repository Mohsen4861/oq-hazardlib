# The Hazard Library
# Copyright (C) 2012 GEM Foundation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
A Magnitude Frequency Distribution (MFD) is a function that describes the rate
(per year) of earthquakes across all magnitudes.

Package `mfd` contains the basic class for MFD --
:class:`oqhazardlib.mfd.base.BaseMFD`, and three actual
implementations:
:class:`oqhazardlib.mfd.evenly_discretized.EvenlyDiscretizedMFD`
:class:`oqhazardlib.mfd.truncated_gr.TruncatedGRMFD` and
:class:`oqhazardlib.mfd.youngs_coppersmith_1985.YoungsCoppersmith1985MFD`.
"""
from oqhazardlib.mfd.evenly_discretized import EvenlyDiscretizedMFD
from oqhazardlib.mfd.truncated_gr import TruncatedGRMFD
from oqhazardlib.mfd.youngs_coppersmith_1985 import (
    YoungsCoppersmith1985MFD
)
