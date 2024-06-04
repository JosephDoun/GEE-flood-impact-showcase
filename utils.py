import ee

def _handle_3_10_bug():
    """
    GEE module has a bug with
    regards to the python
    "collections" module for
    newer versions of python.
    
    This is a fix for it.
    "https://github.com/google/earthengine-api/issues/181"
    """
    import collections
    try:
        collections.Callable
    except AttributeError as e:
        "GEE BUG-fix for python version >= 3.10"
        collections.Callable = collections.abc.Callable
        
        
def _init_ee_instance():
    """
    Init module or Authenticate.
    """
    try:
        ee.Initialize()
    except Exception as e:
    
        ee.Authenticate()
        ee.Initialize()


_vis_params = {
        "bands": ["VH", "VV", "VV"],
        "min"  : -30,
        "max"  : -5
        }



