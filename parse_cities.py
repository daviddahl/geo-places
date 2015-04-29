#!/usr/bin/env python

# GeoNames Gazetteer extract files
# ================================
# This work is licensed under a Creative Commons Attribution 3.0 License,
# see http://creativecommons.org/licenses/by/3.0/
# The Data is provided "as is" without warranty or any representation of accuracy, timeliness or completeness.


# geonameid         : integer id of record in geonames database
# name              : name of geographical point (utf8) varchar(200)
# asciiname         : name of geographical point in plain ascii characters, varchar(200)
# alternatenames    : alternatenames, comma separated, ascii names automatically transliterated, convenience attribute from alternatename table, varchar(10000)
# latitude          : latitude in decimal degrees (wgs84)
# longitude         : longitude in decimal degrees (wgs84)
# feature class     : see http://www.geonames.org/export/codes.html, char(1)
# feature code      : see http://www.geonames.org/export/codes.html, varchar(10)
# country code      : ISO-3166 2-letter country code, 2 characters
# cc2               : alternate country codes, comma separated, ISO-3166 2-letter country code, 60 characters
# admin1 code       : fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code; varchar(20)
# admin2 code       : code for the second administrative division, a county in the US, see file admin2Codes.txt; varchar(80) 
# admin3 code       : code for third level administrative division, varchar(20)
# admin4 code       : code for fourth level administrative division, varchar(20)
# population        : bigint (8 byte int) 
# elevation         : in meters, integer
# dem               : digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
# timezone          : the timezone id (see file timeZone.txt) varchar(40)
# modification date : date of last modification in yyyy-MM-dd format


import csv
import sys

csv.field_size_limit(sys.maxsize)

# create a new file to store the truncated data in:
dest = open('./out/cities-dest.json', 'w')

dest.write('window.geoPlaces = {')

lol = list(csv.reader(open('./cities1000.txt', 'rb'), delimiter='\t'))

for row in lol:
    # row[1] place_name
    # row[4] lat
    # row[5] long
    # row[8] country
    # row[10] admin/state/province
    # cast and round the long/lat to 1 place:

    geo_lat = "%.1f" % float(row[4])
    geo_long = "%.1f" % float(row[5])
    geo_key = "%s__%s" % (geo_lat, geo_long)
    record = "'%s':['%s','%s','%s']," % (geo_key, row[1], row[8], row[10])
    dest.write(record)

dest.write('};')
dest.close()
