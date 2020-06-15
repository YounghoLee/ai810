# MIMIC-III Waveform Database
* https://physionet.org/content/mimic3wdb/1.0/

## wget
*  wget -r -N -c -np https://physionet.org/files/mimic3wdb-matched/1.0/p00/

```
225G    physionet.org/files/mimic3wdb-matched/1.0/p00
210G    physionet.org/files/mimic3wdb-matched/1.0/p01
257G    physionet.org/files/mimic3wdb-matched/1.0/p02
78G     physionet.org/files/mimic3wdb-matched/1.0/p03
265G    physionet.org/files/mimic3wdb-matched/1.0/p04
296G    physionet.org/files/mimic3wdb-matched/1.0/p05
278G    physionet.org/files/mimic3wdb-matched/1.0/p06
260G    physionet.org/files/mimic3wdb-matched/1.0/p07
274G    physionet.org/files/mimic3wdb-matched/1.0/p08
276G    physionet.org/files/mimic3wdb-matched/1.0/p09

Sum : 2,419G
```

## Direcotry
```
1.0/
 |- p00/
   |- p000020/
   |- p000030/
   |- p000033/
   ...
 |- p01/
   |- p010013/
   ...
```

## File List

```
$ ls -alh 1.0/p00/p000020/
total 33M
drwxrwxr-x    2 irteam irteam 4.0K Jun 13 21:28 .
drwxrwxr-x 1246 irteam irteam  32K Jun 13 21:28 ..
-rw-rw-r--    1 irteam irteam  15K Jan  1  2000 3544749_0001.dat
-rw-rw-r--    1 irteam irteam  223 Jan  1  2000 3544749_0001.hea
-rw-rw-r--    1 irteam irteam  496 Jan  1  2000 3544749_0002.dat
-rw-rw-r--    1 irteam irteam  226 Jan  1  2000 3544749_0002.hea
-rw-rw-r--    1 irteam irteam   32 Jan  1  2000 3544749_0003.dat
-rw-rw-r--    1 irteam irteam  223 Jan  1  2000 3544749_0003.hea
-rw-rw-r--    1 irteam irteam 1.5K Jan  1  2000 3544749_0004.dat
-rw-rw-r--    1 irteam irteam  238 Jan  1  2000 3544749_0004.hea
-rw-rw-r--    1 irteam irteam  28M Jan  1  2000 3544749_0005.dat
-rw-rw-r--    1 irteam irteam  247 Jan  1  2000 3544749_0005.hea
-rw-rw-r--    1 irteam irteam  30K Jan  1  2000 3544749_0006.dat
-rw-rw-r--    1 irteam irteam  128 Jan  1  2000 3544749_0006.hea
-rw-rw-r--    1 irteam irteam  88K Jan  1  2000 3544749_0007.dat
-rw-rw-r--    1 irteam irteam  183 Jan  1  2000 3544749_0007.hea
-rw-rw-r--    1 irteam irteam 5.2M Jan  1  2000 3544749_0008.dat
-rw-rw-r--    1 irteam irteam  130 Jan  1  2000 3544749_0008.hea
-rw-rw-r--    1 irteam irteam  160 Jul  1  2017 3544749_layout.hea : ECG 신호 5 개 (I, II, III, AVR 및 "V"), 호흡 신호 및 PPG 신호가 기록
-rw-rw-r--    1 irteam irteam  39K Jan  1  2000 3544749n.dat
-rw-rw-r--    1 irteam irteam 2.8K Jun 13 21:22 index.html
-rw-rw-r--    1 irteam irteam  246 Jul  1  2017 p000020-2183-04-28-17-47.hea : https://physionet.org/physiotools/wag/header-5.htm#sect5
-rw-rw-r--    1 irteam irteam  802 Jul  1  2017 p000020-2183-04-28-17-47n.hea : HR, SpO2 등
-rw-rw-r--    1 irteam irteam  155 Aug  4  2017 RECORDS
```

### File
```
cat physionet.org/files/mimic3wdb-matched/1.0/p00/p000030/3524877_0001.hea
3524877_0001 2 125 450000 12:22:07.132
3524877_0001.dat 80 23/mV 8 0 -72 -26051 0 II
3524877_0001.dat 80 82/mV 8 0 2 15998 0 V


/usr/local/bin/rdsamp -r physionet.org/files/mimic3wdb-matched/1.0/p00/p000030/p000030-2172-10-16-12-22.hea -p -v | head -n5
   Elapsed time      II       V
      (seconds)    (mV)    (mV)
          0.000  -3.130   0.024
          0.008  -3.130   0.012
	  ...

/usr/local/bin/rdsamp -r physionet.org/files/mimic3wdb-matched/1.0/p00/p000030/p000030-2172-10-16-12-22n.hea -p -v | head -n5
   Elapsed time      HR   PULSE    RESP    SpO2  NBPSys NBPDias NBPMean
      (seconds)   (bpm)   (bpm)    (pm)     (%)  (mmHg)  (mmHg)  (mmHg)
          0.000  80.700  74.500  21.000  96.000       -       -       -
         60.000  84.000  62.300  23.200  95.900       -       -       -
        120.000  81.100  65.100  20.000  95.500       -       -       -

```

