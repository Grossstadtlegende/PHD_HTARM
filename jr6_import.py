import RockPy3
from RockPy3.Packages.Mag.io.spinner import Jr6
import numpy as np

fhybrid = '/Users/mike/GitHub/highT_af/High_T_ARM_hTARMACQUISITION_50uT.jr6.txt'
farm = '/Users/mike/GitHub/highT_af/High_T_ARM_ARMACQUISITION_50uT.jr6.txt'
ftrm = '/Users/mike/GitHub/highT_af/High_T_ARM_TRMACQUISITION_50uT.jr6.txt'
S = RockPy3.Study
for sname in ['Va', 'Vb', 'IXD', '525', '1125', '1524']:
    s = S.add_sample(name=sname)
    if sname in ['Va', 'Vb', 'IXD']:
        s.add_to_samplegroup(gname='obs')
    if sname in ['525', '1125', '1524']:
        s.add_to_samplegroup(gname='mani')
    hyb = s.add_measurement(mtype='acquisition', ftype='jr6', fpath=fhybrid)
    hyb.add_series('HTARM')
    trm = s.add_measurement(mtype='acquisition', ftype='jr6', fpath=ftrm)
    trm.add_series('TRM')
    arm = s.add_measurement(mtype='acquisition', ftype='jr6', fpath=farm)
    arm.add_series('ARM')
    tarm = arm + trm
    tarm.add_series('T+ARM')
    harm = hyb - trm
    harm.add_series('H-TRM')
    htrm = hyb - arm
    htrm.add_series('H-ARM')

S.label_add_sname()
S.label_add_series(add_stype=True, add_sval=False, add_unit=False)

S['525'].set_plt_prop('marker', 'o')
S['1125'].set_plt_prop('marker', 's')
S['1524'].set_plt_prop('marker', '.')
print(S.info())

fig = RockPy3.Figure(columns=2)
v = fig.add_visual(visual_input=S.get_measurement(gname='mani', stype=('HTARM', 'T+ARM')), visual='acquisition',
                   title='hybrid',
                   xlabel='Temperature [C]', ylabel='Magnetic Moment $Am^2$')
v = fig.add_visual(visual_input=S.get_measurement(gname='obs', stype=('HTARM', 'T+ARM')), visual='acquisition',
                   title='hybrid',
                   xlabel='Temperature [C]', ylabel='Magnetic Moment $Am^2$')
## arms
v = fig.add_visual(visual_input=S.get_measurement(gname='mani', stype=('ARM', 'H-TRM')), visual='acquisition',
                   title='ARM',
                   xlabel='Temperature [C]', ylabel='Magnetic Moment $Am^2$')
v = fig.add_visual(visual_input=S.get_measurement(gname='obs', stype=('ARM', 'H-TRM')), visual='acquisition',
                   title='ARM',
                   xlabel='Temperature [C]', ylabel='Magnetic Moment $Am^2$')
v = fig.add_visual(visual_input=S.get_measurement(gname='mani', stype=('TRM', 'H-ARM')), visual='acquisition',
                   title='TRM',
                   xlabel='Temperature [C]', ylabel='Magnetic Moment $Am^2$')
v = fig.add_visual(visual_input=S.get_measurement(gname='obs', stype=('TRM', 'H-ARM')), visual='acquisition',
                   title='TRM',
                   xlabel='Temperature [C]', ylabel='Magnetic Moment $Am^2$')
fig.show(set_xlim=[0, None], save_path='Desktop')

fig = RockPy3.Figure(columns=2)
v = fig.add_visual(visual_input=S['525'], visual='acquisition', title='525', xlabel='Temperature [C]',
                   ylabel='Magnetic Moment $Am^2$')
v = fig.add_visual(visual_input=S['Va'], visual='acquisition', title='Va', xlabel='Temperature [C]',
                   ylabel='Magnetic Moment $Am^2$')
v = fig.add_visual(visual_input=S['1125'], visual='acquisition', title='1125', xlabel='Temperature [C]',
                   ylabel='Magnetic Moment $Am^2$')
v = fig.add_visual(visual_input=S['Vb'], visual='acquisition', title='Vb', xlabel='Temperature [C]',
                   ylabel='Magnetic Moment $Am^2$')
v = fig.add_visual(visual_input=S['1524'], visual='acquisition', title='1524', xlabel='Temperature [C]',
                   ylabel='Magnetic Moment $Am^2$')
v = fig.add_visual(visual_input=S['IXD'], visual='acquisition', title='IXd', xlabel='Temperature [C]',
                   ylabel='Magnetic Moment $Am^2$')
fig.show(set_xlim=[0, None], save_path='Desktop', append='samples')
