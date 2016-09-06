""" pyrho -
    a python package for reduced density matrix techniques
"""

import numpy as np
from pyrho.lib import utils

class Unitary(object):
    """A unitary evolution class
    """

    def __init__(self, hamiltonian, is_verbose=True):
        """Initialize the Unitary evolution class. 

        Parameters
        ----------
        hamiltonian : HamiltonianSystem
            An instance of the pyrho HamiltonianSystem class.
        """
        if is_verbose:
            utils.print_banner("PERFORMING UNITARY DYNAMICS")

        self.ham = hamiltonian

    def setup(self):
        pass

    def propagate(self, rho_0, t_init, t_final, dt, is_verbose=True):
        """Propagate the RDM according to Unitary dynamics.

        Parameters
        ----------
        rho_0 : np.array
            The initial RDM.
        t_init : float
            The initial time.
        t_final : float
            The final time.
        dt : float
            The timestep.
        is_verbose : bool
            Flag to indicate verbose printing.

        Returns
        -------
        times : list of floats
            The times at which the RDM has been calculated.
        rhos_site : list of np.arrays
            The RDM at each time in the site basis.
        rhos_eig : list of np.arrays
            The RDM at each time in the system eigen-basis.

        """
        times = np.arange(t_init, t_final, dt)
        rho_0_eig = self.ham.site2eig(rho_0)

        rhos_site = []
        rhos_eig = []
        for time in times:
            rho_eig = self.ham.to_interaction(rho_0_eig, time)
            rhos_eig.append(rho_eig)
            rhos_site.append(self.ham.eig2site(rho_eig))

        if is_verbose:
            print "\n--- Finished performing RDM dynamics"
        
        return times, rhos_site, rhos_eig

