# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""
This module contains the definition of a base class for
initial states. An initial state might be used by a variational
form or in eoh as a trial state to evolve
"""

from typing import Optional, NoReturn
from abc import ABC, abstractmethod
from qiskit.circuit import QuantumRegister
from qiskit.aqua import AquaError  # pylint: disable=unused-import


class InitialState(ABC):
    """Base class for InitialState.

        This method should initialize the module and
        use an exception if a component of the module is not
        available.
    """

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def construct_circuit(self,
                          mode: str = 'circuit',
                          register: Optional[QuantumRegister] = None) -> NoReturn:
        """
        Construct the statevector of desired initial state.

        Args:
            mode: `vector` or `circuit`. The `vector` mode produces the vector.
                  While the `circuit` constructs the quantum circuit corresponding that
                  vector.
            register: qubits for circuit construction.

        Returns:
            QuantumCircuit or numpy.ndarray: statevector.

        Raises:
            AquaError: when mode is not 'vector' or 'circuit'.
        """
        raise NotImplementedError()

    @property
    def bitstr(self):
        """ bitstr """
        return None
