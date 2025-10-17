import numpy as np
import matplotlib.pyplot as plt

file_path = '/kaggle/input/power-spectra-data/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
power_spectrum = data[:, 1]
plt.plot(ell, power_spectrum, label='Best-fit CMB Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('Power Spectrum')
plt.title('Best-fit LCDM CMB Power Spectrum')
plt.legend()
plt.show()


file_path = '/kaggle/input/power-spectra-data/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
power_spectrum = data[:, 1]
ell_limit = 50
ell_subset = ell[ell <= ell_limit]
power_spectrum_subset = power_spectrum[:len(ell_subset)]
plt.plot(ell_subset, power_spectrum_subset, label='Best-fit CMB Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('Power Spectrum')
plt.title('Best-fit LCDM CMB Power Spectrum (up to ell = 50)')
plt.legend()
plt.show()

file_path = '/kaggle/input/planck-te-power-spectrum/COM_PowerSpect_CMB-TE-full_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
te_power_spectrum = data[:, 1]
plt.plot(ell, te_power_spectrum, label='Planck TE Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('TE Power Spectrum')
plt.title('Baseline High-ell Planck TE Power Spectrum')
plt.legend()
plt.show()

file_path = '/kaggle/input/planck-te-power-spectrum/COM_PowerSpect_CMB-TE-full_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
power_spectrum = data[:, 1]
ell_limit = 50
ell_subset = ell[ell <= ell_limit]
power_spectrum_subset = power_spectrum[:len(ell_subset)]
plt.plot(ell_subset, power_spectrum_subset, label='Best-fit CMB Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('Power Spectrum')
plt.title('Best-fit LCDM CMB Power Spectrum (up to ell = 50)')
plt.legend()
plt.show()

file_path = '/kaggle/input/planck-te-power-spectrum/COM_PowerSpect_CMB-TE-full_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
power_spectrum = data[:, 1]
ell_limit = 50
ell_subset = ell[ell <= ell_limit]
power_spectrum_subset = power_spectrum[:len(ell_subset)]
window_size = 5
power_spectrum_smoothed = np.convolve(power_spectrum_subset, np.ones(window_size)/window_size, mode='valid')
plt.plot(ell_subset[:len(power_spectrum_smoothed)], power_spectrum_smoothed, label='Smoothed CMB Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('Power Spectrum')
plt.title('Smoothed LCDM CMB Power Spectrum (up to ell = 50)')
plt.legend()
plt.show()

file_path = '/kaggle/input/planck-te-power-spectrum/COM_PowerSpect_CMB-TE-full_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
power_spectrum = data[:, 1]
ell_limit = 50
ell_subset = ell[ell <= ell_limit]
power_spectrum_subset = power_spectrum[:len(ell_subset)]
window_size = 5
power_spectrum_smoothed = savgol_filter(power_spectrum_subset, window_size, 2) 
plt.plot(ell_subset, power_spectrum_smoothed, label='Smoothed CMB Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('Power Spectrum')
plt.title('Smoothed LCDM CMB Power Spectrum (up to ell = 50)')
plt.legend()
plt.show()

file_path = '/kaggle/input/planck-te-power-spectrum/COM_PowerSpect_CMB-TE-full_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
power_spectrum = data[:, 1]
ell_limit = 50
ell_subset = ell[ell <= ell_limit]
power_spectrum_subset = power_spectrum[:len(ell_subset)]
sigma = 1.0  
power_spectrum_smoothed = gaussian_filter1d(power_spectrum_subset, sigma=sigma)
plt.plot(ell_subset, power_spectrum_smoothed, label='Smoothed CMB Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('Power Spectrum')
plt.title('Gaussian Smoothed LCDM CMB Power Spectrum (up to ell = 50)')
plt.legend()
plt.show()

ell = np.arange(2, 2509) 
normalized_cmb_power_spectrum = np.loadtxt('/kaggle/input/power-spectra-data/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt')  # Replace with your data file path
plt.plot(ell, normalized_cmb_power_spectrum, label='Normalized CMB Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('Normalized C_ell')
plt.title('Best-fit LCDM CMB Power Spectrum (Planck TT,TE,EE+lowE+lensing)')
plt.legend()
plt.show()

ell = np.arange(2, 2509)  
normalized_cmb_power_spectrum = np.loadtxt('/kaggle/input/power-spectra-data/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt')  # Replace with your data file path
plt.plot(ell, normalized_cmb_power_spectrum[:, 1], label='TT') 
plt.plot(ell, normalized_cmb_power_spectrum[:, 2], label='TE') 
plt.plot(ell, normalized_cmb_power_spectrum[:, 3], label='EE') 
plt.plot(ell, normalized_cmb_power_spectrum[:, 4], label='BB')  
plt.plot(ell, normalized_cmb_power_spectrum[:, 5], label='PP')  
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('Normalized C_ell')
plt.title('Best-fit LCDM CMB Power Spectrum (Planck TT,TE,EE+lowE+lensing)')
plt.legend()
plt.show()

file_path = '/kaggle/input/planck-tt-power-spectrum/COM_PowerSpect_CMB-TT-full_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
tt_power_spectrum = data[:, 1]
plt.plot(ell, tt_power_spectrum, label='Planck TT Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('TT Power Spectrum')
plt.title('Baseline High-ell Planck TT Power Spectrum')
plt.legend()
plt.show()

file_path = '/kaggle/input/planck-tt-power-spectrum/COM_PowerSpect_CMB-TT-full_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
power_spectrum = data[:, 1]
ell_limit = 50
ell_subset = ell[ell <= ell_limit]
power_spectrum_subset = power_spectrum[:len(ell_subset)]
plt.plot(ell_subset, power_spectrum_subset, label='Best-fit CMB Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('Power Spectrum')
plt.title('Best-fit LCDM CMB Power Spectrum (up to ell = 50)')
plt.legend()
plt.show()

file_path = '/kaggle/input/planck-ee-power-spectrum/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
ee_power_spectrum = data[:, 1]
plt.plot(ell, ee_power_spectrum, label='Planck EE Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('EE Power Spectrum')
plt.title('Baseline High-ell Planck EE Power Spectrum')
plt.legend()
plt.show()

file_path = '/kaggle/input/planck-te-power-spectrum/COM_PowerSpect_CMB-TE-full_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
te_power_spectrum = data[:, 1]
plt.plot(ell, te_power_spectrum, label='Planck TE Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('TE Power Spectrum')
plt.title('Baseline High-ell Planck TE Power Spectrum')
plt.legend()
plt.show()

file_path = '/kaggle/input/planck-te-power-spectrum/COM_PowerSpect_CMB-TE-full_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
power_spectrum = data[:, 1]
ell_limit = 50
ell_subset = ell[ell <= ell_limit]
power_spectrum_subset = power_spectrum[:len(ell_subset)]
plt.plot(ell_subset, power_spectrum_subset, label='Best-fit CMB Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('Power Spectrum')
plt.title('Best-fit LCDM CMB Power Spectrum (up to ell = 50)')
plt.legend()
plt.show()

file_path = '/kaggle/input/planck-te-power-spectrum/COM_PowerSpect_CMB-TE-full_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
power_spectrum = data[:, 1]
ell_limit = 50
ell_subset = ell[ell <= ell_limit]
power_spectrum_subset = power_spectrum[:len(ell_subset)]
window_size = 20
power_spectrum_smoothed = np.convolve(power_spectrum_subset, np.ones(window_size)/window_size, mode='valid')
plt.plot(ell_subset[:len(power_spectrum_smoothed)], power_spectrum_smoothed, label='Smoothed CMB Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('Power Spectrum')
plt.title('Smoothed LCDM CMB Power Spectrum (up to ell = 50)')
plt.legend()
plt.show()

file_path = '/kaggle/input/planck-binned-tt-power-spectrum/COM_PowerSpect_CMB-TT-binned_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
binned_tt_power_spectrum = data[:, 1]
plt.plot(ell, binned_tt_power_spectrum, label='Planck Binned TT Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('Binned TT Power Spectrum')
plt.title('Baseline High-ell Planck Binned TT Power Spectrum')
plt.legend()
plt.show()


file_path = '/kaggle/input/planck-eb-power-spectrum/COM_PowerSpect_CMB-low-ell-EB-full_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
eb_power_spectrum = data[:, 1]
plt.plot(ell, eb_power_spectrum, label='Planck EB Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('EB Power Spectrum')
plt.title('Low-ell Planck EB Power Spectrum')
plt.legend()
plt.show()

file_path = '/kaggle/input/low-ell-planck-bb-power-spectrum/COM_PowerSpect_CMB-low-ell-BB-full_R3.01.txt'
data = np.loadtxt(file_path)
ell = data[:, 0]
bb_power_spectrum = data[:, 1]
plt.plot(ell, bb_power_spectrum, label='Planck BB Power Spectrum')
plt.xlabel('Multipole Moment (ell)')
plt.ylabel('BB Power Spectrum')
plt.title('Low-ell Planck BB Power Spectrum')
plt.legend()
plt.show()

