



def parse_0x13(packet):
    return [packet[1:]]


#def parse_0x58(packet):
#    pass

def parse_0x8f2a(packet):
    pass


NOTES = """
Command Packet 0x38: Request Satellite System Data
--------------------------------------------------

Early version of this command only accepted a single Sat PRN
while newer versions also have Length and Data fields. 
Python-TSIP suports only the old version of command
packet 0x38.

"""



PACKETS = {
    0x13: (parse_0x13,
           ['packet'],
           'Parsing error'),
    0x1e: ('B',
           ['reset_mode'],
           ' Clear Battery Backup then Reset command'),
    0x1f: ('',
           [],
           ' Request Software Versions command'),
    0x21: ('',
           [],
           ' Request Current Time command'),
    0x23: ('fff',
           ['x',
            'y',
            'z'],
           'Initial Position (XYZ ECEF) command'),
    0x24: ('',
           [],
           'Request GPS Receiver Position Fix Mode command'),
    0x25: ('',
           [],
           'Initiate Soft Reset & Self Test command'),
    0x26: ('',
           [],
           'Request Health command'),
    0x27: ('',
           [],
           'Request Signal Levels command'),
    0x2b: ('fff',
           ['latitude',
            'longitude',
            'altitude'],
            'Initial Position (Latitude, Longitude, Altitude)'),
    0x2d: ('',
           [],
           'Request Oscillator Offset command'),
    0x2e: ('fh',
           ['time_of_week',
            'week_number'],
           'Set GPS time'),
    0x31: ('fff',
           ['x',
            'y',
            'z'],
           'Accurate Initial Position (XYZ ECEF) command'),
    0x32: ('fff',
           ['latitude',
            'longitude',
            'altitude'],
           'Accurate Initial Position (Latitude, Longitude, Altitude)'),
    0x35: ('BBBB',
           ['position',
            'velocity',
            'timing',
            'auxilliary_pseudo_range_measurements'],
           'Set Request I/O Options command'),
    0x37: ('',
           [],
           'Request Status and Values of Last Position and Velocity command'),
    0x38: ('BBB',
           ['operation',
            'type_of_data',
            'sat_prn'],
           'Request/Load Satellite System Data command'),
    0x3a: ('B',
           ['satellite'],
           'Request Last Raw Measurement command'),
    0x3c: ('B',
           ['satellite'],
            'Request Current Satellite Tracking Status command'),
    0x41: ('fhf',
           ['time_of_week',
            'week_number',
            'utc_offset'],
           'GPS Time report'),
    0x42: ('ffff',
           ['x',
            'y',
            'z',
            'time_of_fix'],
           'Single-Precision Position Fix, XYZ ECEF report'),
    0x43: ('fffff',
           ['x_velocity',
            'y_velocity',
            'z_velocity',
            'bias_rate',
            'time_of_fix'],
            'Velocity Fix XYZ ECEF report'),
    0x45: ('BBBBBBBBBB',
           ['navproc_major_version',
            'navproc_minor_version',
            'navproc_month',
            'navproc_day',
            'navproc_year',
            'sigproc_major_revision',
            'sigproc_minor_revision',
            'sigproc_month',
            'sigproc_day',
            'sigproc_year'],
           'Software Version Information report'),
    0x46: ('BB',
           ['status_code',
            'health_battery_antenna_feedline_fix_fault'],
           'Health of Receiver report'),
    0x47: ('',
           [],
           'Signal Levels for all Satellites report'),
    0x4a: ('fffff',
           ['latitude',
            'longitude',
            'altitude',
            'clock_bias',
            'time_of_fix'],
           'Single Precision LLA Position Fix report'),
    0x4b: ('BBB',
           ['machine_id',
            'status1',
            'status2'],
           'Machine/ Code ID and Additional Status report'),
    0x4d: ('f',
           ['offset'],
           'Oscillator Offset report'),
    0x4e: ('c',
           ['response'],
           'Response to Set GPS Time report'),
    0x55: ('BBBB',
           ['position','velocity','timing','auxilliary_pseudo_range_measurements'],
           'I/O Options report'),
    0x56: ('fffff',
           ['east_velocity',
            'north_velocity',
            'up_velocity',
            'clock_bias_rate',
            'time_of_fix'],
           'Velocity Fix, East-North-Up (ENU) report'),
    0x57: ('BBfh',
           ['source_of_information',
            'mfg_diagnostics',
            'time_of_last_fix',
            'week_of_last_fix'],
           'Information About Last Computed Fix'),
#    0x58: (parse_0x58,
#           ['operation',
#            'type_of_data',
#            'sat_prn',
#            'length',
#            'data'],
#           'Satellite System Data from Receiver report'),
    0x5a: ('BBBBBfffd',
           ['satellite_prn_number',
            '_r1',
            '_r2',
            '_r3',
            'integer_msec_of_pseudorange',
            'signal_level',
            'code_phase',
            'doppler',
            'time_of_measurement'],
           'Raw Measurement Data'),
    0x5c: ('BBBBffffB',
           ['satellite_prn_number',
            'channel_bits',
            'acquisition_flag',
            'ephemiris_flag',
            'signal_level',
            'gps_time_of_last_measurement',
            'elevation',
            'azimuth',
            '_r2'],
           'Satellite Tracking Status report'),
    0x69: ('B',
           ['receiver_mode'],
           'Receiver Acquisition Sensitivity Mode report'),
    0x6d: ('Bffff',
           ['dimension',
            'pdop',
            'hdop',
            'vdop',
            'tdop'],
           'All-In-View Satellite Selection report'),
    0x82: ('B',
           ['correction_status'],
           'SBAS Correction Status report'),
    0x83: ('ddddf',
           ['x',
            'y',
            'z',
            'clock_bias',
            'time_of_fix'],
           'Double-Precision XYZ Position Fix and Bias Information report'),
    0x84: ('ddddf',
           ['latitude',
            'longitude',
            'altitude',
            'clock_bias',
            'time_of_fix'],
           'Double-Precision LLA Position Fix and Bias Information report'),
    0x89: ('BB',
           ['receiver_mode',
           '_r1'],
           'Receiver Acquisition Sensitivity Mode report'),
    0xbb: ('',
           [],
           'Set Receiver Configuration command'),
    0xbc: ('',
           [],
           'Set Port Configuration command'),
    0x1c01: ('',
           [],
           'Firmware version command'),
    0x1c03: ('',
           [],
           'Hardware component version command'),
    0x1c81: ('BBBBBBHp',
           ['_reserved',
            'major_version',
            'minor_version',
            'build_number',
            'month',
            'day',
            'year',
            '_l',
            'product_name'],
           'Firmware version report'),
    0x1c83: ('IBBHBHp',
           ['serial_number',
            'build_day',
            'build_month',
            'build_year',
            'build_hour',
            'hardware_code',
            'length',
            'hardware_id'],
           'Hardware component version report'),
    0x8e15: ('',
           [],
           'Request current Datum values command'),
    0x8e26: ('',
           [],
           'Write Configuration to NVS command'),
    0x8e41: ('',
           [],
           'Request Manufacturing Paramaters command'),
    0x8e42: ('',
           [],
           'Stored Production Parameters command'),
    0x8e45: ('B',
           ['segment_id'],
            'Revert Configuration Segment to Default Settings and Write to NVS command'),
    0x8e4a: ('BBBdI',
           ['pps_driver_switch',
            '_r1',
            'pps_polarity',
            'pps_offset_or_cable_delay',
            'bias_uncertainty_threshold'],
            'Set PPS Characteristics'),
    0x8e4c: ('B',
           ['segment_id'],
           'Write Configuration Segment to NVS command'),
    0x8e4e: ('B',
           ['pps_driver_switch'],
           'Set PPS output option command'),
#    0x8ea0: ('B?',
#           ['flag',
#            'value'],
#           'Set DAC Value command'),
    0x8ea2: ('B',
           ['utc_gps_time'],
            'UTC/GPS Timing command'),
    0x8ea3: ('B',
           ['disciplining_command'],
            'Issue Oscillator Disciplining command'),
    0x8ea5: ('HH',
           ['automatic_output_packets',
            '_r1'],
           'Packet Broadcast Mask command'),
    0x8ea6: ('B',
           ['self_survey_command'],
            'Self-Survey command'),
    0x8ea8: ('B',
           ['type'],
           'Request Disciplining Parameters command'),
    0x8ea9: ('BBII',
           ['self_survey_enable',
            'position_save_flag',
            'self_survey_length',
            '_r1'],
           'Self-Survey Parameters command'),
    0x8eab: ('B',
           ['request_type'],
           'Request Primary Timing Packet command'),
    0x8eac: ('B',
           ['request_type'],
           'Request Supplementary Timing Packet command'),
    0x8f15: ('bddddd',
           ['datum_index',
            'dx',
            'dy',
            'dz',
            'a_axis',
            'eccentricity_squared'],
           'Current Datum Values report'),
    0x8f17: ('chfffff',
           ['gridzone_designation',
            'gridzone',
            'northing',
            'easting',
            'altitude',
            'clock_bias',
            'time_of_fix'],
           'UTM Single Precision Output report'),
    0x8f18: ('chddddf',
           ['gridzone_designation',
            'gridzone',
            'northing',
            'easting',
            'altitude',
            'clock_bias',
            'time_of_fix'],
           'UTM Double Precision Output report'),
    0x8f20: ('BhhhHiIiBBBBBBh',
           ['_r1',
            'east_velocity',
            'north_velocity',
            'up_velocity',
            'time_of_week',
            'latitude',
            'longitude',
            'altitude',
            'velocity_scaling',
            '_r2',
            'datum',
            'fix_dimension_alt_hold_filtered',
            'num_svs',
            'utc_offset',
            'week'],
           'Last Fix with Extra Information report (binary fixed point)'),
    0x8f21: ('BHHHHhB',
           ['format_type',
            'east_uncertainty',
            'north_uncertainty',
            'vertical_uncertainty',
            'time_uncertainty',
            'east_north_correlation',
            'fix_age'],
           'Request Accuracy Information report'),
    0x8f23: ('IHBBIIihhhH',
           ['fix_time',
            'week_number',
            'leap_second_offset',
            'fix_available_dgps_2d_velocity_scale',
            'latitude',
            'longitude',
            'altitude',
            'velocity_east',
            'velocity_north',
            'velocity_up',
            '_r1'],
           'Request Last Compact Fix Information report'),
    0x8f26: ('',
           [],
           'Non-Volatile Memory Status report'),
    0x8f2a: (parse_0x8f2a,
           ['_r1',
            '_r2',
            'gps_week_number',
            'gps_millisecond',
            'fractional_gps_nanosecond',
            'altitude',
            'receiver_status_code',
            'receiver_health',
            '_r3',
            'channel_tracking_information'],
           'Fix and Channel Tracking Info report (Type 1)'),
    0x8f2b: ('BBHIiIiiiiBBB',
           ['_r1',
            '_r2',
            'gps_week_number',
            'gps_millisecond',
            'latitude',
            'longitude',
            'altitude',
            'east_west_velocity',
            'north_south_velocity',
            'up_down_velocity',
            'receiver_status_code',
            'receiver_health',
            '_r3'],
           'Fix and Channel Tracking Info report (Type 2)'),
    0x8f4a: ('BBBdI',
           ['_r1',
            '_r2',
            'polarity',
            'pps_offset_or_cable_delay',
            '_r3'],
           'Copernicus II GPS Receiver Cable Delay and POS Polarity'),
    0x8f4f: ('',
           [],
           'Set PPS width report'),
    0x8fab: ('IHhBBBBBBH',
           ['time_of_week',
            'week_number',
            'utc_offset',
            'timing_flag',
            'seconds',
            'minutes',
            'hours',
            'day_of_month',
            'month',
            'year'],
           'Primary Timing Packet report'),
    0x8fac: ('BBBIHHBBBBffI',
           ['receiver_mode',
            'disciplining_mode',
            'self_survey_progress',
            'holdover_duration',
            'critical_alarms',
            'minor_alarms',
            'gps_decoding_status',
            'disciplining_activity',
            'spare_status1',
            'spare_status2',
            'pps_offset',
            'clock_offset',
            'dac_value'],
           'Supplemental Timing Packet'),
    0x8ea800: ('ff',
           ['time_constant',
            'damping_factor'],
           'Set Disciplining Parameters command (Type 0)'),
    0x8ea801: ('fff',
           ['oscillator_gain_constant',
            'minimum_control_voltage',
            'maximum_control_voltage'],
           'Set Disciplining Parameters command (Type 1)'),
    0x8ea802: ('ff',
           ['jam_sync_threshold',
            'maximum_frequency_offset'],
           'Set Disciplining Parameters command (Type 2)'),
    0x8ea803: ('f',
           ['initial_dc_voltage'],
           'Set Disciplining Parameters command (Type 3)')
}
"""
The `PACKETS` table contains the packet structure as
a ``(format, attributes, doc)`` tuple. 

The `format` is a either `struct` format _without_ the leading DLE,
without the packet ID and without the trailing DLE, ETX; or
a custom function that parses this packet into a list of values. 
"""


DATUMS = {
    0: "0 WGS-84",
    1: "1 Tokyo",
    2: "2 North American 1927 Mean Solution (CONUS) NAS-C",
    3: "3 Alaska Canada",
    4: "4 European 1950 Mean Solution EUR-M",
    5: "5 Australian Geodetic 1966 Australia and Tasmania AUA",
    6: "6 WGS-72",
    7: "7 NAD-83",
    8: "8 NAD-02",
    9: "9 Mexican",
    10: "Hawaii",
    11: "Astronomic",
    12: "U.S. Navy",
    13: "European 1950 Mean Solution EUR-M",
    14: "Australian Geodetic 1984 Australia and Tasmania AUG",
    15: "Adindan Mean Solution (Ethiopia and Sudan) ADI-M",
    16: "Adindan Ethiopia ADI-A",
    17: "Adindan Mali ADI-C",
    18: "Adindan Senegal ADI-D",
    19: "Adindan Sudan ADI-B",
    20: "Afgooye Somalia AFG",
    21: "Ain El Abd 1970 Bahrain Island AIN-A",
    22: "Anna 1 Astro 1965 Cocos Islands ANO",
    23: "ARC 1950 Mean Solution ARF-M",
    24: "ARC 1950 Botswana ARF-A",
    25: "ARC 1950 Lesotho ARF-B",
    26: "ARC 1950 Malawi ARF-C",
    27: "ARC 1950 Swaziland ARF-D",
    28: "ARC 1950 Zaire ARF-E",
    29: "ARC 1950 Zambia ARF-F",
    30: "ARC 1950 Zimbabwe ARF-G",
    31: "ARC 1960 Mean Solution ARS",
    32: "ARC 1960 Kenya ARS",
    33: "ARC 1960 Tanzania ARS",
    34: "Ascension Island 1958 Ascension Island ASC",
    35: "Astro Beacon E 1945 Iwo Jima ATF",
    36: "Astro Tern Island (F RIG) 1961 T ern Island TRN",
    37: "Astro Dos 71 /4 St. Helena Island SHB",
    38: "Astronomical Station 1952 Marcus Island TRN",
    39: "Australian Geodetic 1966 Australia and Tasmania AUA",
    40: "Bellevue (IGN) Efate Erromango Island IBE",
    41: "Bermuda 1957 Bermuda Islands BER",
    42: "Bogota Observatory Columbia BOO",
    43: "Compo Inchauspe 1969 Argentina CAI",
    44: "Canton Astro1966 Phoenix Island CAO",
    45: "Cape South Africa CAP",
    46: "Cape Canaveral Mean Solution (Florida and Bahamas) CAC",
    47: "Carthage Tunisia CGE",
    48: "Chatham Island Astro 1971 Chatham Island (New Zealand) CHI",
    49: "Chua Astro Paraguay CHU",
    50: "Corrego Alegre Brazil COA",
    51: "Djakarta (Batavia) Sumatra (Indonesia) BAT",
    52: "Dos 1968 Gizo Island (New Georgia Islands) GIZ",
    53: "Easter Island 1967 Easter Island EAS",
    54: "European 1950 Mean Solution EUR-M",
    55: "European 1950 Cyprus EUR-E",
    56: "European 1950 Egypt EUR-F",
    57: "European 1950 England, Ireland, Scotland, Shetland Islands EUR-G",
    58: "European 1950 England, Ireland, Scotland, Shetland Islands EUR-K",
    59: "European 1950 Greece EUR-B",
    60: "European 1950 Iran EUR-H",
    61: "European 1950 Sardinia EUR-I",
    62: "European 1950 Sicily EUR-J",
    63: "European 1950 Norway and Finland EUR-C",
    64: "European 1950 Portugal and Spain EUR-D",
    65: "European 1979 Mean Solution EUS",
    66: "Gan 1970 Republic of Maldives GAA",
    67: "Geodetic Datum 1948 New Zealand GEO",
    68: "Guam 1963 Guam GUA",
    69: "Gux 1 Astro Guadalcanal Islands DOB",
    70: "Hjorsey 1955 Iceland HJO",
    71: "Hong Kong 1963 Hong Kong HKD",
    72: "Indian 1975 Thailand INH -A",
    73: "Indian India and Nepal IND-I",
    74: "Ireland 1965 Ireland IRL",
    75: "ISTS 073 Astro 1969 Diego Garcia IST",
    76: "Johnstone Island 19 61 Johnstone Island JOH",
    77: "Kandawala Sri Lanka KAN",
    78: "Kerguelen Island 1949 Kerguelen Island KEG",
    79: "Kertau 1948 West Malaysia and Singapore KEA",
    80: "Reunion Mascarene Island REU",
    81: "L.C.5 Astro 1961 Ca yman Brac Island LCF",
    82: "Liberia 1964 Liberia LIB",
    83: "Luzon Philippines LUZ-A",
    84: "Luzon Mindanao Island LUZ-B",
    85: "Mahe 1971 Mahe Island MIK",
    86: "Sel vagem Grande 1938 Salvage Islands SGM",
    87: "Massawa Eritrea (Ethiopia) MAS",
    88: "Merchich Morocco MER",
    89: "Midway Astro 1961 Midway Islands MID",
    90: "Minna Nigeria MIN-B",
    91: "Nahrwan Masirah Island (Oman) NAH-A",
    92: "Nahrwan United Arab Emirates NAH-B",
    93: "Nahrwan Saudi Arabia NAH-C",
    94: "Schwarzeck Namibia SCK",
    95: "Naparima, BWI Trinidad and Tobago NAP",
    96: "NAD 27 Western United States NAS-B",
    97: "NAD 27 Eastern United States NAS-A",
    98: "NAD 27 Alaska NAS-D",
    99: "NAD 27 Bahamas NAS-Q",
    100: "NAD 27 San Salvador NAS-R",
    101: "NAD 27 Canada NAS-E",
    102: "NAD 27 Alberta BC NAS-F",
    103: "NAD 27 East Canada NAS-G",
    104: "NAD 27 Manitoba Ontario NAS-H",
    105: "NAD 27 Northwest Terri tories Saskatchewan NAS-I",
    106: "NAD 27 Yukon NAS-J",
    107: "NAD 27 Canal Zone NAS-O",
    108: "NAD 27 Caribbean NAS-P",
    109: "NAD 27 Central America NAS-N",
    110: "NAD 27 Cuba NAS-T",
    111: "NAD 27 Greenland NAS-U",
    112: "NAD 27 Mexico NAS-V",
    113: "NAD 83 Alaska NAR-A",
    114: "NAD 83 Canada NAR-B",
    115: "NAD 83 CONUS NAR-C",
    116: "NAD 83 Mexico and Central America NAR-D",
    117: "Observatorio Meteorologico 1939 Corvo and Flores Islands (Azores) FLO",
    118: "Old Egyptian 1907 Egypt OEG",
    119: "Old Hawaiian Mean Solution OHA-M",
    120: "Old Hawaiian Hawaii OHA-A",
    121: "Old Hawaiian Kauai OHA-B",
    122: "Old Hawaiian Maui OHA-C",
    123: "Old Hawaiian Oahu OHA-D",
    124: "Oman Oman FAH",
    125: "Ordnance Survey of Great Britain Mean Solution OGB-M",
    126: "Ordnance Survey of Great Britain England OGB-M",
    127: "Ordnance Survey of Great Britain Isle of Man OGB-M",
    128: "Ordnance Survey of Great Britain Scotland and Shetland Islands OGB-M",
    129: "Ordnance Survey of Great Britain Wales OGB-M",
    130: "Pico De Las Nieves Canary Islands PLN",
    131: "Pitcairn Astro 1967 Pitcairn Island PIT",
    132: "Provisional South Chilean 1963 Southern Chile (near 53S) HIT",
    133: "Provisional South American 1956 Mean Solution (Bolivia, Ch ile, Columbia, Ecuador, Guyana, Peru, Venezuela) PRP-M",
    134: "Provisional South American 1956 Bolivia, Chile PRP-A",
    135: "Provisional South American 1956 Northern Chile (near 19S) PRP-B",
    136: "Provisional South American 1956 Southern Chile (near 43S) PRP-C",
    137: "Provisional South American 1956 Columbia PRP-D",
    138: "Provisional South American 1956 Ecuador PRP-E",
    139: "Provisional South American 1956 Guyana PRP-F",
    140: "Provisional South American 1956 Peru PRP-G",
    141: "Provisional South American 1956 Venezuela PRP-H",
    142: "Puerto Rico Puerto Rico and Virgin Islands PUR",
    143: "Quatar National Qatar QAT",
    144: "Qornoq South Greenland QUO",
    145: "Rome 1940 Sardinia MOD",
    146: "Santa Braz Sao Miguel, Santa Maria Islands (Azores) SAO",
    147: "Santo (DOS) 1952 Espirito Santo Island SAE",
    148: "Sapper Hill 1943 East Falkland Islands SAP",
    149: "South American 1969 Mean Solution (Argentina, Bolivia, Br azil, Chile, Columbia, Ecuador, Guyana, Paraguay, Peru, Trinidad Tobago, Venezuela) SAN-M",
    150: "South American 1969 Argentina SAN-A",
    151: "South American 1969 Bolivia SAN-B",
    152: "South American 1969 Brazil SAN-C",
    153: "South American 1969 Chile SAN-D",
    154: "South American 1969 Columbia, SAN-E",
    155: "South American 1969 Ecuador (Excluding Galapagos Isl a nds) SAN-F",
    156: "South American 1969 Guyana SAN-G",
    157: "South American 1969 Paraguay SAN-H",
    158: "South American 1969 Peru SAN-I",
    159: "South American 1969 Trinidad and Tobago SAN-K",
    160: "South American 1969 Venezuela SAN-L",
    161: "South Asia Singapore SOA",
    162: "Porto Santo 1936 Porto Santo and Madera Islands POS",
    163: "Graciosa Base Southwest 1948 Faial, Graciosa, Pico, San Jorg, and Terceira Islands (Azores) GRA",
    164: "Timbalai 1948 Brunei and East Malaysia (Sarawak and Sabah) TIL",
    165: "Tokyo Mean Solution (Japan, Okinawa and South Korea) TOY-M",
    166: "Tokyo South Korea TOY-B",
    167: "Tokyo Okinawa TOY-C",
    168: "Tristan Astro 1968 Tristan Da Cunha TDC",
    169: "Viti Levu 1916 Viti Levu Island (Fiji Islands) MVS",
    170: "Wake Eniwetok 1960 Marshall Islands ENW",
    171: "Zanderij Surinam ZAN",
    172: "Bukit Rimpah Bangka and Belitung Islands (Indonesia) BUR",
    173: "Camp Area Astro Camp McMurdo Area, Antarctica CAZ",
    174: "Gunung Segara Kalimantan (Indonesia) GSE",
    175: "Herat North Afghanistan HEN",
    176: "Hu-Tzu-Shan Taiwan HTN",
    179: "Tokyo GIS Coordinates TOY-B",
    }
"""
Mapping of datum value as contained in packets 0x8e15 and 0x8f15 to
their name.

Taken from Trimble Copernicus 2 - Reference Manual (Rev. 1.07) , p.144+.

Reference: DMA TR 8350.2 Second Edition, 1 Sept. 1991. DMA Technical Report, 
Department of Defense World Geodetic System 1984, Definition and Relationships 
with Local Geodetic Systems.
"""


