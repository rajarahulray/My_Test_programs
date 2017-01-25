# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 14:40:27 2017

@author: stpl
"""
from mpl_toolkits.basemap import Basemap
from matplotlib import pyplot as plt
import tkinter as t 

def map_plot(colour):
    try:
        fig = plt.figure();
        fig.canvas.set_window_title('Map_Viewer');
        
        m = Basemap(projection = 'mill', 
                    llcrnrlon = 60,
                    llcrnrlat = 4,
                    urcrnrlon = 102,
                    urcrnrlat = 38,
                    resolution = 'l',
                    );
                    
        
        
        
        ind_lat, ind_lon = 28.7041, 77.1025;
        xpt, ypt = m(ind_lon, ind_lat);
        m.plot(xpt, ypt, '{}^'.format(colour), markersize = 10, label = 'Delhi');
        m.readshapefile('D:\IND_adm_shp\IND_adm3', 'India', zorder = 2, color = 'k');
        m.bluemarble();
        plt.legend();
        plt.show();
    
    except Exception as e:
        #t.messagebox.showerror("Error", str(e));
        print("Error: ",str(e));
        r.destroy();
        exit();

r = t.Tk();

e = t.Entry(r);
e.pack();
#x = e.get();
b = t.Button(r, text = "Set Color-code", command = lambda: map_plot(e.get())).pack();
r.mainloop();