#!bin/python

import pandas as pd
import glob




    def read_time_series_text_files(self, path, ex=".txt"):

        """
        Reads all files with *.txt in a dir assuming they are time series.
        """

        allFiles = glob.glob(path + "/*"+ex)

