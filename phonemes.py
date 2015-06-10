import cv2
import numpy as np
import os
import time
import sys
import nltk

"""
Phoneme Example Translation    Phoneme Example Translation
------- ------- -----------    ------- ------- -----------
AA      odd     AA D           AE      at      AE T
AH      hut     HH AH T        AO      ought   AO T
AW      cow     K AW           AY      hide    HH AY D
B       be      B IY           CH      cheese  CH IY Z
D       dee     D IY           DH      thee    DH IY
EH      Ed      EH D           ER      hurt    HH ER T
EY      ate     EY T           F       fee     F IY
G       green   G R IY N       HH      he      HH IY
IH      it      IH T           IY      eat     IY T
JH      gee     JH IY          K       key     K IY
L       lee     L IY           M       me      M IY
N       knee    N IY           NG      ping    P IH NG
OW      oat     OW T           OY      toy     T OY
P       pee     P IY           R       read    R IY D
S       sea     S IY           SH      she     SH IY
T       tea     T IY           TH      theta   TH EY T AH
UH      hood    HH UH D        UW      two     T UW
V       vee     V IY           W       we      W IY
Y       yield   Y IY L D       Z       zee     Z IY
ZH      seizure S IY ZH ER

Files:
blair_a_i.jpg
blair_c_d_g_k_n_r_s_th_y_z.jpg
blair_e.jpg
blair_f_v_d_th.jpg
blair_l_d_th.jpg
blair_m_b_p.jpg
blair_o.jpg
blair_rest.jpg
blair_u.jpg
blair_w_q.jpg

Cross use:
AA      blair_o.jpg
AH      blair_c_d_g_k_n_r_s_th_y_z.jpg
AW      blair_c_d_g_k_n_r_s_th_y_z.jpg
B       blair_m_b_p.jpg
D       blair_c_d_g_k_n_r_s_th_y_z.jpg
EH      blair_e.jpg
EY      blair_a_i.jpg
G       blair_c_d_g_k_n_r_s_th_y_z.jpg
IH      blair_a_i.jpg
JH      blair_c_d_g_k_n_r_s_th_y_z.jpg
L       blair_l_d_th.jpg
N       blair_c_d_g_k_n_r_s_th_y_z.jpg
OW      blair_o.jpg
P       blair_m_b_p.jpg
S       blair_c_d_g_k_n_r_s_th_y_z.jpg
T       blair_l_d_th.jpg
UH      blair_c_d_g_k_n_r_s_th_y_z.jpg
V       blair_f_v_d_th.jpg
Y       blair_c_d_g_k_n_r_s_th_y_z.jpg
ZH      blair_c_d_g_k_n_r_s_th_y_z.jpg
AE      blair_a_i.jpg
AO      blair_o.jpg
AY      blair_a_i.jpg
CH      blair_c_d_g_k_n_r_s_th_y_z.jpg
DH      blair_c_d_g_k_n_r_s_th_y_z.jpg
ER      blair_u.jpg
F       blair_f_v_d_th.jpg
HH      blair_c_d_g_k_n_r_s_th_y_z.jpg
IY      blair_e.jpg
K       blair_c_d_g_k_n_r_s_th_y_z.jpg
M       blair_m_b_p.jpg
NG      blair_c_d_g_k_n_r_s_th_y_z.jpg
OY      blair_a_i.jpg
R       blair_c_d_g_k_n_r_s_th_y_z.jpg
SH      blair_c_d_g_k_n_r_s_th_y_z.jpg
TH      blair_f_v_d_th.jpg
UW      blair_u.jpg
W       blair_w_q.jpg
Z       blair_c_d_g_k_n_r_s_th_y_z.jpg
"""

## Importing all the mouth images
mouths = {}
for i in os.listdir("./mouths"):
    if i.endswith(".jpg"):
        print i
        img = cv2.imread("./mouths" + "/" + i, 0)
        mouths["" + i] = img
        continue
#print mouths

#Creating the Dictionary between phonemes and mouths
PhonemeToMouth={'AA':'blair_o.jpg',
'AH':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'AW':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'AE':'blair_a_i.jpg',
'AO':'blair_o.jpg',
'AY':'blair_a_i.jpg',
'B':'blair_m_b_p.jpg',
'CH':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'DH':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'D':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'EH':'blair_e.jpg',
'EY':'blair_a_i.jpg',
'ER':'blair_u.jpg',
'F':'blair_f_v_d_th.jpg',
'G':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'HH':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'IY':'blair_e.jpg',
'IH':'blair_a_i.jpg',
'JH':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'K':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'L':'blair_l_d_th.jpg',
'M':'blair_m_b_p.jpg',
'NG':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'N':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'OY':'blair_a_i.jpg',
'OW':'blair_o.jpg',
'P':'blair_m_b_p.jpg',
'T':'blair_l_d_th.jpg',
'R':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'SH':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'S':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'TH':'blair_f_v_d_th.jpg',
'UH':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'UW':'blair_u.jpg',
'W':'blair_w_q.jpg',
'V':'blair_f_v_d_th.jpg',
'Y':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'ZH':'blair_c_d_g_k_n_r_s_th_y_z.jpg',
'Z':'blair_c_d_g_k_n_r_s_th_y_z.j'}

#
# actualImg = mouths.itervalues().next()
#
# ## Ploting them as an animation
# for key,value in mouths.items():
#     ### Fast mouth showing
#     cv2.imshow('window', value)
#     cv2.waitKey(1)
#     time.sleep(0.2)