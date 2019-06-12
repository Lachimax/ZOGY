import zogy
import astropy.io.fits as fits
import os

directory = '/home/lachlan/ZOGY/data/'

# file = fits.open(directory + 'FRB-181112--Host-FORS2.2018-12-03T02:00:57.814_SCIENCE_REDUCED_IMG_trim.fits',
#                  mode='update')
# file[1].header = file[0].header
# file.close()

# file[0].header['SATURATE'] = 65535
# file[0].header['RDNOISE'] = 2.7


# file = fits.open(directory + 'FRB-181112--Host-FORS2.2018-12-03T02:10:12.158_SCIENCE_REDUCED_IMG_trim.fits',
#                  mode='update')
# file[0].header['SATURATE'] = 65535
# file[0].header['RDNOISE'] = 2.7
# file[1].header = file[0].header
# file.close()

zogy.optimal_subtraction(
    new_fits=directory + 'g_1.fits',
    ref_fits=directory + 'g_2.fits',
    telescope='VLT')
