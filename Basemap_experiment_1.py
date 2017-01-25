# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:20:08 2017

@author: stpl
"""

from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot as plt
#from matplotlib.patches import Polygon



#a, ax = plt.subplots();
fig = plt.figure();
fig.canvas.set_window_title('Map Viewer')
#fig.set_size_inches(25.22, 5.25);


m = Basemap(projection = 'mill', 
            llcrnrlon = 60,
            llcrnrlat = 0,
            urcrnrlon = 100,
            urcrnrlat = 40,
            resolution = 'l',
            );
            
m.drawcoastlines();
m.drawcountries(linewidth = 2);
m.drawstates(color = 'g');
m.bluemarble();

#shp = m.readshapefile('D:\IND_adm_shp\IND_adm0', 'states', drawbounds=True);
#for nshape, seg in enumerate(m.states):
#            poly = Polygon(seg, facecolor='0.75', edgecolor='k')
#            ax.add_patch(poly)


ind_lat, ind_lon = 28.7041, 77.1025;
xpt, ypt = m(ind_lon, ind_lat);
m.plot(xpt, ypt, 'r^', markersize = 10);

plt.title('Map of India');

'''for full screen...'''
#mng = plt.get_current_fig_manager()
#mng.full_screen_toggle()


plt.show();

m.readshapefile('D:\IND_adm_shp\IND_adm3', 'India', zorder = 2);