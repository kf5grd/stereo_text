stereo_text.py
============

**stereo_text.py** is a proof of concept designed to generate blocks of text with a hidden 3d message in the form of an [autostereogram](https://en.wikipedia.org/wiki/Autostereogram).

Currently it can generate 2 different types of autostereogram:

* *Panel*: Takes text input from a file or stdin. Any text in /forward slashes/ will appear in the foreground, while any text in \backslashes\ will drop into the background. All other text will be in between. See panel_example.txt
* *SIRT (Single Image Random Text)*: Takes a depthmap input from a file or stdin. The depthmap consists of multiple lines, which must all be the same length. Each line is a series of numbers from 0 to 9, with 0 representing the lowest depth (farthest away) and 9 representing the highest depth (closest). All depths are relative to the depth before it, so any number on the depth map cannot be more than 1 higher or lower than the number before or after it. See sirt_example.txt

-----

**Installation:**

```
~/ $ git clone https://github.com/kf5grd/stereo_text.git
~/ $ cd ./stereo_text
~/stereo_text/ $ pip install .

-----

**Usage and examples:**

```
~/stereo_text/ $ stereo_text --help
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

  Generate autostereograms with text.

  Be sure to read over the readme to get a good idea of what input is
  expected.

Options:
  --help  Show this message and exit.

Commands:
  panel  Generates 2 panels, each with a slightly...
  sirt   Generates a single block of seemingly random...

~/stereo_text/ $ cat ./sirt_example.txt
00000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000
00000000011111111110000011111111110000000000000000000000000000000
00000000001111111100000001111111100000000000000000000000000000000
00000000001111111100000001111111100000111111100000000000000000000
00000000001111111100000001111111100000111111100000000000000000000
00000000001111111100000001111111100000111111100000000000000000000
00000000001111111100000001111111100000000000000000000000000000000
00000000001111111111111111111111100001111111100000000000000000000
00000000001111111100000001111111100000111111100000000000000000000
00000000001111111100000001111111100000111111100000000000000000000
00000000001111111100000001111111100000111111100000000000000000000
00000000001111111100000001111111100000111111100000000000000000000
00000000001111111100000001111111100000111111100001111000000000000
00000000011111111110000011111111110001111111110001111000000000000
00000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000
22222222222222222222222222222222222222222222222222222222222222222
22222222222222222222222222222222222222222222222222222222222222222
22222222222222222222222222222222222222222222222222222222222222222
22222222222222222222222222222222222222222222222222222222222222222
22222222211111111112222211111111112222222222222222222222222222222
22222222221111111122222221111111122222222222222222222222222222222
22222222221111111122222221111111122222111111122222222222222222222
22222222221111111122222221111111122222111111122222222222222222222
22222222221111111122222221111111122222111111122222222222222222222
22222222221111111122222221111111122222222222222222222222222222222
22222222221111111111111111111111122221111111122222222222222222222
22222222221111111122222221111111122222111111122222222222222222222
22222222221111111122222221111111122222111111122222222222222222222
22222222221111111122222221111111122222111111122222222222222222222
22222222221111111122222221111111122222111111122222222222222222222
22222222221111111122222221111111122222111111122221111222222222222
22222222211111111112222211111111112221111111112221111222222222222
22222222222222222222222222222222222222222222222222222222222222222
22222222222222222222222222222222222222222222222222222222222222222
22222222222222222222222222222222222222222222222222222222222222222
22222222222222222222222222222222222222222222222222222222222222222

~/stereo_text/ $ stereo_text sirt ./sirt_example.txt
CEOIA810Z4MH3NKCEOIA810Z4MH3NKCEOIA810Z4MH3NKCEOIA810Z4MH3NKCEOIA810Z4MH3NKCEOI
NSEI2FP5U1HJA3RNSEI2FP5U1HJA3RNSEI2FP5U1HJA3RNSEI2FP5U1HJA3RNSEI2FP5U1HJA3RNSEI
0ED9N24C61RZGXS0ED9N24C61RZGXS0ED9N24C61RZGXS0ED9N24C61RZGXS0ED9N24C61RZGXS0ED9
L9FV4WZXR1CMBS6L9FV4WZXR1CMBS6L9FV4WZXR1CMBS6L9FV4WZXR1CMBS6L9FV4WZXR1CMBS6L9FV
LQN0IVEAJC59KR8LQN0IVEAC59KR8LQN04IVEA59KR8LQN04PIVEA59KR8LQN04PIVEA59KR8LQN04P
SY6D79O5CUQ0PE2SY6D79O5CQ0PE2SY6AD79O5C0PE2SY6AQD79O5C0PE2SY6AQD79O5C0PE2SY6AQD
170J5LHKNPXVWAI170J5LHKNXVWAI170CJ5LHKNVWAI170CZJ5LHNVWAI17S0CZJ5LHNVWAI17S0CZJ
MAZ5F2NUO846RKVMAZ5F2NUO46RKVMAZJ5F2NUO6RKVMAZJL5F2NO6RKVMAYZJL5F2NO6RKVMAYZJL5
BSANP6JW42GCL0KBSANP6JW4GCL0KBSAZNP6JW4CL0KBSAZENP6J4CL0KBSIAZENP6J4CL0KBSIAZEN
DQ6NP03AIFKO2RSDQ6NP03AIKO2RSDQ6JNP03AIO2RSDQ6JBNP03AIO2RSDQ6JBNP03AIO2RSDQ6JBN
68E1OSRN0AKU9L468E1OSRN0KU9L468E1OSRN0KU9L468E1BOSR0KU9L468TE1BOSR0KU9L468TE1BO
XSYK97TBQ8DEZHUXSYK97TBQDEZHUXSYNK97TBQEZHUXSYN4K97TQEZHUXSWYN4K97TQEZHUXSWYN4K
NTFJWL415KVIXR6NTFJWL415VIXR6NTFEJWL415IXR6NTFEYJWL45IXR6NT9FEYJWL45IXR6NT9FEYJ
S5ZGDMQYKF27U91S5ZGDMQYK27U91S5ZPGDMQYK7U91S5ZPBGDMQK7U91S5JZPBGDMQK7U91S5JZPBG
PTGU32K9HWB1XEFPTGU32K9HB1XEFPTG6U32K9H1XEFPTG6SU32KH1XEFPTAG6SU32KH1XEFPTAG6SU
VR3LQZSPG1XKY92VR3LQZSPGXKY92VR35LQZSPGKY92VR35OLQZSGKY92VRT35OQZSG6KY92VRT35OQ
3GDPR604CQWNJM83GDPR604QWNJM83GDP1R604WNJM83GDP1ZR64WNJM83GDHP1R64WLNJM83GDHP1R
IBT47QFKU8NEX1JIBT47QFKU8NEX1JIBT47QFKU8NEX1JIBT47QFKU8NEX1JIBT47QFKU8NEX1JIBT4
5LMCNW3VIAUXZF65LMCNW3VIAUXZF65LMCNW3VIAUXZF65LMCNW3VIAUXZF65LMCNW3VIAUXZF65LMC
FPOUY4V08DXB7SHFPOUY4V08DXB7SHFPOUY4V08DXB7SHFPOUY4V08DXB7SHFPOUY4V08DXB7SHFPOU
GQ9J8DT4IZBE63PGQ9J8DT4IZBE63PGQ9J8DT4IZBE63PGQ9J8DT4IZBE63PGQ9J8DT4IZBE63PGQ9J
LSOT5N31Y7BZV46LSOT5N31Y7BZV46LSOT5N31Y7BZV46LSOT5N31Y7BZV46LSOT5N31Y7BZV46LSOT
Y78QTDM6RSZHO3FY78QTDM6RSZHO3FY78QTDM6RSZHO3FY78QTDM6RSZHO3FY78QTDM6RSZHO3FY78Q
FRW0ETPCNKQOI2JFRW0ETPCNKQOI2JFRW0ETPCNKQOI2JFRW0ETPCNKQOI2JFRW0ETPCNKQOI2JFRW0
QFIN2YMV45W7BK8QFIN2YMV45W7BK8QFIN2YMV45W7BK8QFIN2YMV45W7BK8QFIN2YMV45W7BK8QFIN
3RWL76U5CKJYNZ83RWL76U5CEKJYNZ83RW76U5C9EKJYNZ83R76U5C9EKJYNZ83R76U5C9EKJYNZ83R
O34IWTRULFDCB8PO34IWTRULFYDCB8PO3IWTRULF6YDCB8POIWTRULF6YDCB8POIWTRULF6YDCB8POI
A9SBMQLETCR6ZF7A9SBMQLETCHR6ZF7A9BMQLETCPHR6ZF7ABMQLEGTCPHR6F7ABMQLEGTCPHR6F7AB
2PBQS4NHWRM15J62PBQS4NHWRVM15J62PQS4NHWR3VM15J62QS4NHDWR3VM1J62QS4NHDWR3VM1J62Q
4YEQPB0HS7X9OI84YEQPB0HS7UX9OI84YQPB0HS71UX9OI84QPB0HWS71UX9I84QPB0HWS71UX9I84Q
WLF456912M0OTBUWLF456912MY0OTBUWL456912MKY0OTBUW456912MKY0OTBUW456912MKY0OTBUW4
73W14DRQPE9ZBL673W14DRQPEM9ZBL673W14DRQPEM9ZBL67W14DKRQPEM9ZL67W14DKRQPEM9ZL67W
I52HQSC90VMZ1EKI52HQSC90VFMZ1EKI5HQSC90V7FMZ1EKIHQSC9D0V7FMZEKIHQSC9D0V7FMZEKIH
NL3F4D5HA1OI8Y2NL3F4D5HA1COI8Y2NLF4D5HA1WCOI8Y2NF4D5HEA1WCOIY2NF4D5HEA1WCOIY2NF
XPHBIGWLAR1FE87XPHBIGWLARO1FE87XPBIGWLARJO1FE87XBIGWL4ARJO1F87XBIGWL4ARJO1F87XB
E8FCAB6ZQD05W7PE8FCAB6ZQDH05W7PE8CAB6ZQDYH05W7PECAB6ZUQDYH057PECAB6ZUQDYH057PEC
OY3HRBS1GJ92AW7OY3HRBS1GJ492AW7OYHRBS1GJD492AW7OHRBS13GJD492W7OHNRBS3GJD492W7OH
AJE03HLT1QOIU97AJE03HLT1PQOIU97AJE3HLT1WPQOIU97AJ3HLDT1WPQOIU7AJS3HLT1WPQOIU7AJ
JA79GUNHFOVYCS5JA79GUNHFOVYCS5JA79GUNHFOVYCS5JA79GUNHFOVYCS5JA79GUNHFOVYCS5JA79
0DI5GPFVMRK4SL30DI5GPFVMRK4SL30DI5GPFVMRK4SL30DI5GPFVMRK4SL30DI5GPFVMRK4SL30DI5
X710AD9TY48GQF6X710AD9TY48GQF6X710AD9TY48GQF6X710AD9TY48GQF6X710AD9TY48GQF6X710
04PIC6XJSZTLK1N04PIC6XJSZTLK1N04PIC6XJSZTLK1N04PIC6XJSZTLK1N04PIC6XJSZTLK1N04PI
```
