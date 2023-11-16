import numpy as np
import colour


xy_0 = np.array([0.45986,0.41060])
xy_1 = np.array([0.31352,0.32363])

flux_0 = 100
flux_1 = 100

weight_0 = flux_0
weight_1 = flux_1

# Proportional XYZ color at flux of 1 lumen (setting Y = 1):
XYZ_0 = np.array([xy_0[0]/xy_0[1], 1, (1 - xy_0[0] - xy_0[1])/xy_0[1]])
XYZ_1 = np.array([xy_1[0]/xy_1[1], 1, (1 - xy_1[0] - xy_1[1])/xy_1[1]])

cct_0 = colour.xy_to_CCT(colour.XYZ_to_xy(XYZ_0), method='McCamy 1992')
cct_1 = colour.xy_to_CCT(colour.XYZ_to_xy(XYZ_1), method='McCamy 1992')

cct_mix = colour.xy_to_CCT(colour.XYZ_to_xy(weight_0*XYZ_0 + weight_1*XYZ_1), method='McCamy 1992')

print(cct_0)
print(cct_1)
print(cct_mix)