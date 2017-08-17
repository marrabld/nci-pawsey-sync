#!/bin/bash

module load python/2.7.6
module load gdal
export PYTHONPATH=~/auscophub/lib/python2.7/site-packages:$PYTHONPATH

export outputFile=$(pwd)/listOfFiles
export searchDate="2014-01-01T00:00:00"

# grab a list of download URLs from SARA
# remember to use --jsonfeaturesfile as we can grab the physical
# path from where the quicklook is located
for i in {1..3}; do
	echo 'Sentinel-'$i
	/home/554/dm1522/auscophub/bin/auscophub_searchSara.py --sentinel $i --queryparam "geometry=POLYGON((92 29,110 29,110 6,115 6,115 11,119 11,119 22,129.28515625 22.0,129.3291015625 -25.7261540736202,141.4892558125 -25.6469489161716,-150 -90,39 -90,39 -49,75 -49,75 -2,92 -2,92 6,92 29))&publishedAfter=$searchDate" --jsonfeaturesfile $outputFile"."$i".json" &
done 

wait

# awk-ing and sed-ing to create the path
awk 'BEGIN{FS="\"quicklook\":"}{if(/"quicklook":/){print $2}}' *.json | sed -e 's, *,,g' -e 's,",,g' -e 's,\,,,g' -e 's,png,zip,g' -e 's,http://copernicus.nci.org.au/data,/g/data3/fj7/Copernicus,g'
