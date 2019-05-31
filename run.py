import zogy
import astropy.io.fits as fits

directory = '/home/lachlan/Data/FRB181112/FORS2/MJD58455/3-trimmed_with_python/science/g_HIGH/'

file = fits.open(directory + 'FRB-181112--Host-FORS2.2018-12-03T01:34:13.651_SCIENCE_REDUCED_IMG_trim.fits',
                 mode='update')
file[0].header['SATURATE'] = 65535
file[0].header['RDNOISE'] = 2.7
file.close()

file = fits.open(directory + 'FRB-181112--Host-FORS2.2018-12-03T01:43:06.901_SCIENCE_REDUCED_IMG_trim.fits',
                 mode='update')
file[0].header['SATURATE'] = 65535
file[0].header['RDNOISE'] = 2.7
file.close()

zogy.optimal_subtraction(
    new_fits=directory + 'FRB-181112--Host-FORS2.2018-12-03T01:34:13.651_SCIENCE_REDUCED_IMG_trim.fits',
    ref_fits=directory + 'FRB-181112--Host-FORS2.2018-12-03T01:43:06.901_SCIENCE_REDUCED_IMG_trim.fits')
