import sys
import os
import unittest
from app import app

sys.path.append(os.path.realpath('.'))
from api.db.scheduler import *  # download_and_cache_images


class TestSchedular(unittest.TestCase):
    def setUp(self):
        # ==============================#
        # We just grab the quick looks as the full files are quite large
        # ==============================#

        self.remote_file_list = [
            'http://copernicus.nci.org.au/data/Sentinel-2/MSI/L1C/2017/2017-10/20S165E-25S170E/S2B_MSIL1C_20171031T230849_N0206_R101_T58KEB_20171110T181705.png',
            'http://copernicus.nci.org.au/data/Sentinel-2/MSI/L1C/2017/2017-11/20S150E-25S155E/S2B_MSIL1C_20171116T000209_N0206_R030_T56KPA_20171116T010224.png',
            'http://copernicus.nci.org.au/data/Sentinel-2/MSI/L1C/2017/2017-11/20S130E-25S135E/S2B_MSIL1C_20171110T011709_N0206_R088_T53KMQ_20171110T042558.zip',
            'http://copernicus.nci.org.au/data/Sentinel-1/C-SAR/SLC/2017/2017-10/15N115E-10N120E/S1A_IW_SLC__1SDV_20171008T215507_20171008T215534_018727_01F993_8525.png',
            'http://copernicus.nci.org.au/data/Sentinel-3/SLSTR/SL_2_WST___/2017/2017-11/2017-11-15/S3A_SL_2_WST____20171115T044905_20171115T045205_20171115T063536_0180_024_261_4499_MAR_O_NR_002.png']

    #@unittest.skip('Skip this test')
    def test_download_and_cache_images(self):
        app.logger.debug('Unittest :: download_and_cache_images for files :: {}'.format(self.remote_file_list))
        download_and_cache_images(self.remote_file_list)


    @unittest.skip('Skip this test')
    def test_sync_nci_to_pawsey(self):
        """

        :return:
        """
        app.logger.debug('Unittest :: test_sync_nci_to_pawsey :: {}'.format(self.remote_file_list))
        sync_nci_to_pawsey(last_published_list=self.remote_file_list)



    def test_push_cache_to_pawsey(self):
        """

        :return:
        """
        push_cache_to_pawsey(dry_run=False)