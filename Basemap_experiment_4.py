# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 14:40:27 2017

@author: stpl
"""
from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot as plt

fig = plt.figure();
fig.canvas.set_window_title('Map_Viewer');

m = Basemap(projection = 'mill', 
            llcrnrlon = 60,
            llcrnrlat = 4,
            urcrnrlon = 102,
            urcrnrlat = 38,
            resolution = 'l',
            );
            
m.readshapefile('D:\IND_adm_shp\IND_adm3', 'India', zorder = 2, color = 'k');

ind_lat, ind_lon = 28.7041, 77.1025;
xpt, ypt = m(ind_lon, ind_lat);
m.plot(xpt, ypt, 'r^', markersize = 10, label = 'Delhi');
m.bluemarble();
plt.legend();
plt.show();