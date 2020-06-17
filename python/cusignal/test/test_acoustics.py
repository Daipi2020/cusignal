# Copyright (c) 2019-2020, NVIDIA CORPORATION.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cupy as cp
import cusignal
import numpy as np
import pytest

from cusignal.test.utils import array_equal
from scipy import signal

# Missing
# rceps
# cceps_unwrap
# cceps


class TestAcoustics:
    def test_rceps(self):
        cpu_window = 0
        gpu_window = 0
        assert array_equal(cpu_window, gpu_window)

    def test_cceps_unwrap(self):
        cpu_window = 0
        gpu_window = 0
        assert array_equal(cpu_window, gpu_window)

    def test_cceps(self):
        cpu_window = 0
        gpu_window = 0
        assert array_equal(cpu_window, gpu_window)
