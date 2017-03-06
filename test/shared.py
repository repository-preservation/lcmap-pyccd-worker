import os
import pytest

@pytest.fixture(scope="session")
def set_environment():
    os.environ['LPW_RABBIT_HOST']        = 'localhost'
    os.environ['LPW_RABBIT_PORT']        = '5672'
    os.environ['LPW_RABBIT_QUEUE']       = 'unit.lcmap.changes.worker'
    os.environ['LPW_RABBIT_EXCHANGE']    = 'unit.lcmap.changes.worker'
    os.environ['LPW_RABBIT_SSL']         = 'False'
    os.environ['LPW_TILE_SPEC_HOST']     = 'localhost'
    os.environ['LPW_TILE_SPEC_PORT']     = '5678'
    os.environ['LPW_LOG_LEVEL']          = 'INFO'
    os.environ['LPW_RESULT_ROUTING_KEY'] = 'change-detection-result'
    return os.environ

tile_spec_keys = {'data_shape', 'data_mask', 'tags', 'tile_y', 'data_type', 'tile_x', 'band_spectrum',
                  'band_product', 'satellite', 'band_category', 'instrument', 'name', 'shift_y',
                  'pixel_x', 'band_short_name', 'data_fill', 'band_name', 'shift_x', 'data_scale',
                  'data_range', 'data_units', 'band_long_name', 'pixel_y', 'ubid', 'wkt', 'resample_method'}

spect_map_keys = {'blue', 'green', 'nir', 'swir2', 'thermal', 'red', 'cfmask', 'swir1'}

good_input_data = {'algorithm': 'lcmap-pyccd:1.0.3.b1',
                   'tile_update_requested': '2017-02-28T04:35:46.023Z',
                   'tile_x': -1821585,
                   'tile_y': 2891595,
                   'inputs_url': 'http://lcmap-test.cr.usgs.gov:80/landsat/tiles?x=-1851585&y=2870805&acquired=1980-01-01/2015-12-31&ubid=LANDSAT_4/TM/cfmask&ubid=LANDSAT_4/TM/sr_band1&ubid=LANDSAT_4/TM/sr_band2&ubid=LANDSAT_4/TM/sr_band3&ubid=LANDSAT_4/TM/sr_band4&ubid=LANDSAT_4/TM/sr_band5&ubid=LANDSAT_4/TM/sr_band7&ubid=LANDSAT_4/TM/toa_band6&ubid=LANDSAT_5/TM/cfmask&ubid=LANDSAT_5/TM/sr_band1&ubid=LANDSAT_5/TM/sr_band2&ubid=LANDSAT_5/TM/sr_band3&ubid=LANDSAT_5/TM/sr_band4&ubid=LANDSAT_5/TM/sr_band5&ubid=LANDSAT_5/TM/sr_band7&ubid=LANDSAT_5/TM/toa_band6&ubid=LANDSAT_7/ETM/cfmask&ubid=LANDSAT_7/ETM/sr_band1&ubid=LANDSAT_7/ETM/sr_band2&ubid=LANDSAT_7/ETM/sr_band3&ubid=LANDSAT_7/ETM/sr_band4&ubid=LANDSAT_7/ETM/sr_band5&ubid=LANDSAT_7/ETM/sr_band7&ubid=LANDSAT_7/ETM/toa_band6'}

simplified_detect_results = {'processing_mask': [True, False, True, False, False, True, False, False, True, False, True, True, True, True, True, True, False, False, False, False, False, False, True, True, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, False, False, False, True, True, True, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, True, False, True, True, False, True, True, True, True, False, True, False, True, True, True, True, True, True, False, False, True, False, True, False, False, False, True, False, True, True, True, True, False, True, True, False, True, True, False, True, True, False, True, False, False, False, True, False, False, False, True, True, False, True, False, True, True, True, True, True, False, False, True, True, False, True, True, True, True, True, True, True, True, False, True, False, True, True, False, True, False, False, True, True, False, False, True, False, False, True, False, True, True, True, False, True, True, True, True, True, False, False, True, True, True, True, True, True, False, False, True, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, False, True, True, True, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, True, True, False, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, False, False, True, False, False, False, False, True, False, False, True, False, True, True, False, False, True, True, True, False, True, False, True, False, True, True, True, True, False, True, False, False, False, True, True, True, True, True, True, False, True, True, False, False, False, False, True, True, False, True, True, True, True, False, True, True, True, True, False, True, True, True, True, False, True, False, False, True, False, True, True, True, True, False, False, False, True, False, False, True, False, True, False, False, True, False, False, True, True, True, True, True, True, True, True, True, True, False, True, False, True, True, False, True, False, True, True, True, False, False, False, False, True, True, False, True, True, True, True, True, True, True, True, False, False, True, False, True, True, False, True, True, True, False, False, False, False, True, True, False, True, True, True, False, False, False, True, False, True, True, True, True, False, False, True, False, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, True, False, False, True, True, True, True, True, True, True, False, True, False, True, True, False, False, True, True, False, True, True, True, True, False, False, True, True, False, True, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, True, False, False, False, False, False, True, False, False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, False, True, False, True, True, True, True, True, True, True, True, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, True, True, True, True, False, False, False, True, True, False, False, False, True, False, True, True, True, False, False, True, False, False, True, True, False, True, True, False, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, False, False, False, True, False, True, False, True, False, False, False, False, True, False, False, False, False, True, False, True, False, False, True, True, False, True, False, True, True, False, True, False, False, False, True, False, True, True, False, False, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, False, False, True, False, True, False, False, True, False, False, True, True, True, False, True, False, False, True, True, True, True, False, False, True, False, True, False, False, False, False, False, False, True, True, False, True, True, True, True, True, False, True, True, False, True, True, True, False, True, True, True, True, True, True, False, True, False, False, False, True, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, True, True, False, True, True, True, False, True, True, True, False, True, False, True, False, True, False, False, False, False, True, False, False, False, True, False, True, False, True, True, True, True, True, False, True, True, True, False, True, True, True, False, True, True, True, True, True, True, False, False, True, True, False, True, False, False, False, False, True, False, True, True, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, True, False, True, False, False, False, False, False, False, True, True, True, True, False, True, True, False, False, True, False, True, True, True, False, True, True, True, True, False, True, False, True, True, False, True, True, True, True, True, True, True, True, True, True, False, True, False, False, True, True, False, False, True, True, True, False, False, True, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, True, True, True, True, False, True, True, False, False, True, False, True, False, False, True, True, True, True, False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, False, False, True, True, True, True, False, True, True, False, False, True, False, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, True, False, True, False, True, False, True, True, False, True, True, True, False, True, True, True, True, True, True, False, True, True, False, False, False, True, True, False, True, True, True, True, False, True, True, False, False, True, True, False, False, True, False, False, False, True, True, False, False, False, False, False, False, False, False, True, True, False, False, True, True, True, True, False, True, True, True, False, True, False, False, False, True, False, False, True, True, False, False, False, False, True, False, True, False, False, True, False, True, True, True, True, False, True, True, False, False, False, True, False, True, False, True, False, True, True, True, False, True, False, False, True, True, True, False, True, True, False, False, False, True, False, False, True, False, True, False, False, True, False, False, True, True, True, True, False, False, True, True, False, True, True, False, False, True, True, False, True, True, True, False, False, True, False, True, True, True, True, False, True, True, True, True, True, True, False, False, False, True, True, True, True, True, False, True, True, False, True, True, True, True, False, False, False, True, True, False, False, False, True, False, False, False, False, False, False, True, True, False, True, True, True, False, True, False, True, False, True, True, False, True, False, True, False, False, False, False, False, False, True, True, False, True, True, True, False, True, False, False, True, False, True, True, False, True, False, False, False, False, True, False, False, True, False, False, True, False, False, True, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, True, True, False, False, True, False, True, False, True, False, True, False, False, True, True, True, True, True, False, True, True, False, True, False, True, False, True, True, True, True, True, True, True, False, True, True, True, True, False, True, False, False, True, False, True, False, True, False, True, True, False, False, True, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, True, False, True, False, False, False, False, False, False, False, True, True, False, True, False, True, False, True, False, True, True, True, True, False, False, False, True, False, True, False, True, True, True, True, False, True, True, True, False, True, False, True, False, False, True, True, True, False, True, False, False, True, False, False, False, True, True, False, False, False, False, False, False, False, False, True, False, False, True, False, True, False, True, False, True, True, True, True, False, False, True, True, False, False, False, True, False, True, True, False, False, True, False, False, True, False, False, False, False, True, False, False, True, False, True, False, False, False, False, False, True, False, True, False, True, False, True, True, True, True, True, False, False, False, False, False, False, False, True, False, False, True, False, True, False, False, False], 'procedure': 'standard_procedure', 'algorithm': 'lcmap-pyccd:1.0.3.b1', 'change_models': [{'swir2': {'rmse': 211.57041788682182, 'intercept': 28261.094185275411, 'coefficients': [-0.03569286930194155, -380.48694994646155, -57.647640677187482, 0.0, 0.0, -26.763540685547589, 36.67161569001383]}, 'start_day': 724134.0, 'nir': {'rmse': 171.76575578304917, 'intercept': 38239.050874202512, 'coefficients': [-0.049659792746157248, -270.19344924210202, 12.600794076936181, 0.0, 0.0, 4.0185577033542845, 1.7435620268380883]}, 'red': {'rmse': 160.74750329979821, 'intercept': 39360.55177101888, 'coefficients': [-0.051845546567530598, -294.01194369150141, -97.785013644296853, 0.0, 0.0, -6.1698583273900054, 22.056554437485048]}, 'num_coefficients': 8, 'swir1': {'rmse': 209.33242133612009, 'intercept': 22514.645146633404, 'coefficients': [-0.027274822701503526, -340.5344401990003, -68.789208531205162, 0.0, 0.0, -30.773750176595598, 31.04983959486783]}, 'break_day': 735766.0, 'thermal': {'rmse': 563.74087595504, 'intercept': -36691.152109953793, 'coefficients': [0.053268513652848216, -1896.2246692693777, 144.70065017941184, 0.0, 0.0, 59.84697201764957, -99.934482619544326]}, 'change_probability': 0, 'median_resids': [2.7981208813748495, 3.8965176985339887, 2.7463956584220734, 0.49512156864083828, 0.21415936386186413, 11.795049873680712], 'blue': {'rmse': 138.2848514496535, 'intercept': 34272.569135164907, 'coefficients': [-0.045645151591280367, -126.65476500089233, -40.090517455533082, 0.0, 0.0, -1.515593522960706, 12.31552607786384]}, 'green': {'rmse': 150.30355017096156, 'intercept': 43064.034900307015, 'coefficients': [-0.057242588690418719, -209.27393916941733, -55.275915930928818, 0.0, 0.0, -0.0, 12.344104764850767]}, 'end_day': 735766.0, 'observation_count': 793}]}
