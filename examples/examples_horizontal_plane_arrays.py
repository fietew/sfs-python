"""Generates sound fields for various arrays and virtual source types."""

import numpy as np
import matplotlib.pyplot as plt
import sfs


dx = 0.1  # secondary source distance
N = 30  # number of secondary sources
f = 1000  # frequency
pw_angle = 20  # traveling direction of plane wave
xs = [-1.5, 0.2, 0]  # position of virtual monopole
tapering = sfs.tapering.kaiser  # tapering window
xnorm = [1, 1, 0]  # normalization point for plots
x = np.arange(-2.5, 2.5, 0.02)  # spatial grid
y = np.arange(-1, 2.5, 0.02)  # spatial grid
acenter = [0.3, 0.7, 0]  # center and normal vector of array
anormal = sfs.util.normal(np.radians(35), np.radians(90))

# angular frequency
omega = 2 * np.pi * f
# normal vector of plane wave
npw = sfs.util.normal(np.radians(pw_angle), np.radians(90))


def compute_and_plot_soundfield(title):
    """Compute and plot synthesized sound field."""
    twin = tapering(a)
    p = sfs.mono.synthesized.generic(omega, x0, d * twin * a0, x, y, 0,
                                     source=sourcetype)

    plt.figure(figsize=(15, 15))
    sfs.plot.soundfield(p, x, y, xnorm)
    sfs.plot.loudspeaker_2d(x0, n0, twin)
    sfs.plot.virtualsource_2d(xs)
    sfs.plot.virtualsource_2d(xs, npw, type='plane')
    plt.title(title)
    plt.grid()
    plt.savefig(title + '.png')


# linear array, secondary point sources, virtual monopole
x0, n0, a0 = sfs.array.linear(N, dx, center=acenter, n0=anormal)

sourcetype = sfs.mono.source.point
a = sfs.mono.drivingfunction.source_selection_point(n0, x0, xs)

d = sfs.mono.drivingfunction.wfs_3d_point(omega, x0, n0, xs)
compute_and_plot_soundfield('linear_ps_wfs_3d_point')

d = sfs.mono.drivingfunction.wfs_25d_point(omega, x0, n0, xs, xref=xnorm)
compute_and_plot_soundfield('linear_ps_wfs_25d_point')

d = sfs.mono.drivingfunction.wfs_2d_point(omega, x0, n0, xs)
compute_and_plot_soundfield('linear_ps_wfs_2d_point')

# linear array, secondary line sources, virtual line source
sourcetype = sfs.mono.source.line
d = sfs.mono.drivingfunction.wfs_2d_line(omega, x0, n0, xs)
compute_and_plot_soundfield('linear_ls_wfs_2d_line')


# linear array, secondary point sources, virtual plane wave
sourcetype = sfs.mono.source.point
a = sfs.mono.drivingfunction.source_selection_plane(n0, npw)

d = sfs.mono.drivingfunction.wfs_3d_plane(omega, x0, n0, npw)
compute_and_plot_soundfield('linear_ps_wfs_3d_plane')

d = sfs.mono.drivingfunction.wfs_25d_plane(omega, x0, n0, npw, xref=xnorm)
compute_and_plot_soundfield('linear_ps_wfs_25d_plane')

d = sfs.mono.drivingfunction.wfs_2d_plane(omega, x0, n0, npw)
compute_and_plot_soundfield('linear_ps_wfs_2d_plane')


# non-uniform linear array, secondary point sources
x0, n0, a0 = sfs.array.linear_nested(N, dx/2, dx, center=acenter, n0=anormal)

d = sfs.mono.drivingfunction.wfs_25d_point(omega, x0, n0, xs, xref=xnorm)
a = sfs.mono.drivingfunction.source_selection_point(n0, x0, xs)
compute_and_plot_soundfield('linear_nested_ps_wfs_25d_point')

d = sfs.mono.drivingfunction.wfs_25d_plane(omega, x0, n0, npw, xref=xnorm)
a = sfs.mono.drivingfunction.source_selection_plane(n0, npw)
compute_and_plot_soundfield('linear_nested_ps_wfs_25d_plane')


# random sampled linear array, secondary point sources
x0, n0, a0 = sfs.array.linear_random(N, dx/2, 1.5*dx, center=acenter,
                                     n0=anormal)

d = sfs.mono.drivingfunction.wfs_25d_point(omega, x0, n0, xs, xref=xnorm)
a = sfs.mono.drivingfunction.source_selection_point(n0, x0, xs)
compute_and_plot_soundfield('linear_random_ps_wfs_25d_point')

d = sfs.mono.drivingfunction.wfs_25d_plane(omega, x0, n0, npw, xref=xnorm)
a = sfs.mono.drivingfunction.source_selection_plane(n0, npw)
compute_and_plot_soundfield('linear_random_ps_wfs_25d_plane')


# rectangular array, secondary point sources
x0, n0, a0 = sfs.array.rectangular(N//2, dx, N, dx, center=acenter, n0=anormal)
d = sfs.mono.drivingfunction.wfs_25d_point(omega, x0, n0, xs, xref=xnorm)
a = sfs.mono.drivingfunction.source_selection_point(n0, x0, xs)
compute_and_plot_soundfield('rectangular_ps_wfs_25d_point')

d = sfs.mono.drivingfunction.wfs_25d_plane(omega, x0, n0, npw, xref=xnorm)
a = sfs.mono.drivingfunction.source_selection_plane(n0, npw)
compute_and_plot_soundfield('rectangular_ps_wfs_25d_plane')


# circular array, secondary point sources
x0, n0, a0 = sfs.array.circular(N, 1, center=acenter)
d = sfs.mono.drivingfunction.wfs_25d_point(omega, x0, n0, xs, xref=xnorm)
a = sfs.mono.drivingfunction.source_selection_point(n0, x0, xs)
compute_and_plot_soundfield('circular_ps_wfs_25d_point')

d = sfs.mono.drivingfunction.wfs_25d_plane(omega, x0, n0, npw, xref=xnorm)
a = sfs.mono.drivingfunction.source_selection_plane(n0, npw)
compute_and_plot_soundfield('circular_ps_wfs_25d_plane')