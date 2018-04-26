from __future__ import print_function

import numpy as np

import mesh.patch as patch
from util import msg

def init_data(my_data, rp):
    """ initialize the Kelvin-Helmholtz problem """

    msg.bold("initializing the sedov problem...")

    # make sure that we are passed a valid patch object
    if not isinstance(my_data, patch.CellCenterData2d):
        print(my_data.__class__)
        msg.fail("ERROR: patch invalid in sedov.py")


    # get the density, momenta, and energy as separate variables
    dens = my_data.get_var("density")
    xmom = my_data.get_var("x-momentum")
    ymom = my_data.get_var("y-momentum")
    ener = my_data.get_var("energy")

    # initialize the components, remember, that ener here is rho*eint
    # + 0.5*rho*v**2, where eint is the specific internal energy
    # (erg/g)
    dens[:,:] = 1.0
    xmom[:,:] = 0.0
    ymom[:,:] = 0.0

    rho_1 = rp.get_param("kh.rho_1")
    v_1   = rp.get_param("kh.v_1")
    rho_2 = rp.get_param("kh.rho_2")
    v_2   = rp.get_param("kh.v_2")

    gamma = rp.get_param("eos.gamma")

    xmin = rp.get_param("mesh.xmin")
    xmax = rp.get_param("mesh.xmax")

    ymin = rp.get_param("mesh.ymin")
    ymax = rp.get_param("mesh.ymax")

    myg = my_data.grid

    rhom = (rho_1 - rho_2)*0.5
    vm = (v_1 - v_2)*0.5
    dy = 0.025
    w0 = 0.01
    vbulk = rp.get_param("kh.vbulk")
    
    #regions
    idy1 = np.logical_and(myg.y2d >= 0, myg.y2d < 0.25)
    idy2 = np.logical_and(myg.y2d >= 0.25, myg.y2d < 0.5)
    idy3 = np.logical_and(myg.y2d >= 0.5, myg.y2d < 0.75)
    idy4 = np.logical_and(myg.y2d >= 0.75, myg.y2d < 1.0)

    # region 1
    dens[idy1] = rho_1 - rhom*np.exp((myg.y2d[idy1]-0.25)/dy)
    xmom[idy1] = v_1 - vm*np.exp((myg.y2d[idy1]-0.25)/dy)
    # region 2
    dens[idy2] = rho_2 + rhom*np.exp((0.25-myg.y2d[idy2])/dy)
    xmom[idy2] = v_2 + vm*np.exp((0.25-myg.y2d[idy2])/dy)
    # region 3
    dens[idy3] = rho_2 + rhom*np.exp((myg.y2d[idy3]-0.75)/dy)
    xmom[idy3] = v_2 + vm*np.exp((myg.y2d[idy3]-0.75)/dy)
    # region 4
    dens[idy4] = rho_1 - rhom*np.exp((0.75-myg.y2d[idy4])/dy)
    xmom[idy4] = v_1 - vm*np.exp((0.75-myg.y2d[idy4])/dy)

    ymom[:,:] = w0*np.sin(4*np.pi*myg.x2d) + vbulk

    p = 2.5
    xmom[:,:] *= dens
    ymom[:,:] *= dens
    ener[:,:] = p/(gamma-1.0) + 0.5*(xmom[:,:]**2+ymom[:,:]**2)/dens[:,:]

def finalize():
    """ print out any information to the user at the end of the run """
    pass
