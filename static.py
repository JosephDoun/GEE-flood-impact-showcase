from typing import Any, Tuple

import geopandas as gpd

from matplotlib import pyplot as plt
from matplotlib import patches


class StaticVisualizer:
    """
    
    Helper class for static visualizations
    of vectorized results.
    
    Main use is to properly create maps without
    clogging the main notebook with technical code.
    
    # TODO
    # Perhaps add basemap tiles
    # for user orientation & placement.
    
    """
    def __init__(self,
                 ax_title:  str='',
                 crs:       int=4326,
                 figsize: Tuple=(15, 25)):
        
        self.crs     = crs

        (self.fig,
         self.ax)    = plt.subplots(figsize=figsize)
        
        self.handles = []
        self.legend  = self.ax.legend(loc='upper left')
        
        self.ax.set_title(ax_title, fontsize=20)
        
    def __call__(self, gdf: gpd.GeoDataFrame, **kwds: Any):
        
        zorder = (
            kwds['zorder']
            if 'zorder' in kwds.keys()
            else None
        )

        gdf = gdf.to_crs(self.crs)
        gdf.plot(ax=self.ax,
                 label=kwds['label'],
                 color=kwds['color'],
                 edgecolor=kwds['ec'],
                 ls=kwds['ls'],
                 lw=kwds['lw'],
                 zorder=zorder)
        
        if 'text' in kwds.keys():
            
            self.ax.annotate(kwds['text'],
                             xy=(gdf.centroid[0].x,
                                 gdf.centroid[0].y),
                             ha='center',
                             va='center',
                             **{'fontsize': 12})
        else:
            self.__update_legend(kwds)
        
        return self.fig

    def __update_legend(self, kwds):
        self.legend.remove()
        self.handles.append(
            patches.Patch(facecolor=kwds['color'],
                          ec=kwds['ec'],
                          lw=1,
                          label=kwds['label'],
                          ls=kwds['ls'])
        )
        
        self.legend = self.ax.legend(handles=[
            *self.ax.get_legend_handles_labels()[0],
            *self.handles
        ], title='Legend', loc=2)
