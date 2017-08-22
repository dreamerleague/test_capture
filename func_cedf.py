#coding: utf-8

import os,sys
import re
from PIL import Image,ImageChops


c=function(a){for(var b,c,d,e=[],f=0,g=[],h=0,i=a.length-1;h<i;h++)b=Math.round(a[h+1][0]-a[h][0]),c=Math.round(a[h+1][1]-a[h][1]),d=Math.round(a[h+1][2]-a[h][2]),g.push([b,c,d]),0==b&&0==c&&0==d||(0==b&&0==c?f+=d:(e.push([b,c,d+f]),f=0));return 0!==f&&e.push([b,c,f]),e}

e=function(a){for(var b=[[1,0],[2,0],[1,-1],[1,1],[0,1],[0,-1],[3,0],[2,-1],[2,1]],c="stuvwxyz~",d=0,e=b.length;d<e;d++)if(a[0]==b[d][0]&&a[1]==b[d][1])return c[d];return 0}

d=function(a){var b="()*,-./0123456789:?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqr",c=b.length,d="",e=Math.abs(a),f=parseInt(e/c);f>=c&&(f=c-1),f&&(d=b.charAt(f)),e%=c;var g="";return a<0&&(g+="!"),d&&(g+="$"),g+d+b.charAt(e)}



f=function(a){for(var b,f=c(Q.t("arr",a)),g=[],h=[],i=[],j=0,k=f.length;j<k;j++)b=e(f[j]),b?h.push(b):(g.push(d(f[j][0])),h.push(d(f[j][1]))),i.push(d(f[j][2]));return g.join("")+"!!"+h.join("")+"!!"+i.join("")}



[105,102,40,33,104,97,115,86,97,108,105,100,41,123,98,114,111,119,115,101,114,95,118,101,114,115,105,111,110,40,123,32,118,97,108,117,101,58,32,52,48,53,57,54,49,55,51,55,125,41,59,104,97,115,86,97,108,105,100,61,116,114,117,101,59,125]