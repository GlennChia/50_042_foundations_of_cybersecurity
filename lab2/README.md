# 1. Installations

For this lab, we need the `pwn` library which allows us to connect to the server to send and receive messages 

## 1.1 The Windows way (No Ubuntu) - does not work

<u>**1. Install `pwntools`**</u> 

https://pypi.org/project/pwntools/

- This is the way to get `pwn` to work on Windows 

Note: We have to upgrade pip first (Use the terminal as an Admin)

![](assets/01.PNG)

Actual installation (Don't do this because the package is outdated)

![](assets/02.PNG)

**This installs the package (Later we find that this is not the legit one). We then get an error "No module named '_curses'"**

METHOD 1 (Recommmended)

Link: https://github.com/pmbarrett314/curses-menu/issues/18

Run `pip install windows-curses`

METHOD 2 (Not recommended)

Link: https://www.lfd.uci.edu/~gohlke/pythonlibs/#curses

- Download the version of curses that corresponds to your Windows and version of Python, and then pip install the whl file with the python you plan on using.
- In my case, I am using Windows 10 and Python 3.7. Hence, I choose `curses‑2.2.1+utf8‑cp37‑cp37m‑win_amd64.whl`

<u>**2. After that when we run the code again we have another error**</u>

Error: `SyntaxError: invalid syntax: "def goto((r, c)):"`

Solution: Reinstall pwntools

Link: https://github.com/arthaud/python3-pwntools/issues/3

```
pip3 install git+https://github.com/arthaud/python3-pwntools.git
```

**3. Finally after this stage I get an error `ModuleNotFoundError: No module named 'fcntl'`**

Link:https://stackoverflow.com/questions/1422368/fcntl-substitute-on-windows

https://github.com/cs01/gdbgui/issues/18

https://stackoverflow.com/questions/1422368/fcntl-substitute-on-windows

Basically no fix at this stage as the solution stated has an invalid link

## 1.2  The windows way with Ubuntu app

<u>**Step 1**</u>

Initially when I was installed the Ubuntu app, I was stuck at the phrase `Installing, this may take a few minutes...`

https://askubuntu.com/questions/966184/new-installation-of-windows-10-and-ubuntu-from-windows-store-error

1. From the search, find `PowerShell`

2. Enter this command in `PowerShell` 

   ```shell
   Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
   ```

![](assets/03.PNG)

<u>**Step 2**</u>

I start with a fresh install of the Ubuntu app from the Microsoft Store. 

![](assets/04.PNG)

Step 3: Enter a username and password

![](assets/05.PNG)

Step 4: Run the following commands

1. `sudo apt-get update`
   ![](assets/06.PNG)
2. Install pip with `sudo apt install python-pip`
   ![](assets/07.PNG)
   If successful we will get the screenshot below. Verify with `pip -V`
   ![](assets/08.PNG)
3. Install pip3 with `sudo apt install python3-pip`
   ![](assets/09.PNG)
   If successful
   ![](assets/10.PNG)
4. Once done, we can cd into the folder with the bash installation file and run it with `sudo ./install.sh`
   ![](assets/11.PNG)
   If successful, we should see 
   ![](assets/12.PNG)

# 2. Running the functions

## 2.1 Running the first function - sol1()

Function

```python
def sol1():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("1")  # select challenge 1

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    print(challenge)
    # decrypt the challenge here
    solution = int(0).to_bytes(7408, 'big')
    conn.send(solution)
    message = conn.recvline()
    message = conn.recvline()
    if b'Congratulations' in message:
        print(message)
    conn.close()

```

We run the function with `python3 lab2Client.py`

![](assets/13.PNG)

```
b"->..-O2\x0cO|uYIX\t\tcKYO2FXcK2I2.>_O2.tO\x0cO2;IE2I2|OI\x0c2->..-O2 >\x0c-2;tc2;IE2-csO|\t<'2OsO\x0c'2cKO2;tc2-ccVO|2I.2tO\x0cp2<F.2_cE.2ce2I--2<'2tO\x0c\t \x0cIK|_c.tO\x0cp2IK|2.tO\x0cO2;IE2Kc.t>K 2.tI.2EtO2;cF-|2Kc.2tIsO\t >sOK2.c2.tO2Yt>-|W22cKYO2EtO2 IsO2tO\x0c2I2->..-O2YIX2ce2\x0cO|\tsO-sO.p2;t>Yt2EF>.O|2tO\x0c2Ec2;O--2.tI.2EtO2;cF-|2KOsO\x0c2;OI\x0c\tIK'.t>K 2O-EOW22Ec2EtO2;IE2I-;I'E2YI--O|2->..-O2\x0cO|uYIXW\t\tcKO2|I'2tO\x0c2_c.tO\x0c2EI>|2.c2tO\x0cp2Yc_Op2->..-O2\x0cO|uYIXp2tO\x0cO\t>E2I2X>OYO2ce2YIVO2IK|2I2<c..-O2ce2;>KOW22.IVO2.tO_2.c2'cF\x0c\t \x0cIK|_c.tO\x0cp2EtO2>E2>--2IK|2;OIVp2IK|2.tO'2;>--2|c2tO\x0c2 cc|W\tEO.2cF.2<Oec\x0cO2>.2 O.E2tc.p2IK|2;tOK2'cF2I\x0cO2 c>K p2;I-V\tK>YO-'2IK|2{F>O.-'2IK|2|c2Kc.2\x0cFK2cee2.tO2XI.tp2c\x0c2'cF2_I'\teI--2IK|2<\x0cOIV2.tO2<c..-Op2IK|2.tOK2'cF\x0c2 \x0cIK|_c.tO\x0c2;>--\t O.2Kc.t>K W22IK|2;tOK2'cF2 c2>K.c2tO\x0c2\x0ccc_p2|cKv.2ec\x0c O.\t.c2EI'p2 cc|u_c\x0cK>K p2IK|2|cKv.2XOOX2>K.c2OsO\x0c'2Yc\x0cKO\x0c2<Oec\x0cO\t'cF2|c2>.W\t\t>2;>--2.IVO2 \x0cOI.2YI\x0cOp2EI>|2->..-O2\x0cO|uYIX2.c2tO\x0c2_c.tO\x0cp2IK|\t IsO2tO\x0c2tIK|2cK2>.W\t\t.tO2 \x0cIK|_c.tO\x0c2->sO|2cF.2>K2.tO2;cc|p2tI-e2I2-OI FO2e\x0cc_2.tO\ts>--I Op2IK|2RFE.2IE2->..-O2\x0cO|uYIX2OK.O\x0cO|2.tO2;cc|p2I2;c-e\t_O.2tO\x0cW22\x0cO|uYIX2|>|2Kc.2VKc;2;tI.2I2;>YVO|2Y\x0cOI.F\x0cO2tO2;IEp\tIK|2;IE2Kc.2I.2I--2Ie\x0cI>|2ce2t>_W\t\t3 cc|u|I'p2->..-O2\x0cO|uYIXp32EI>|2tOW\t\t3.tIKV2'cF2V>K|-'p2;c-eW3\t\t3;t>.tO\x0c2I;I'2Ec2OI\x0c-'p2->..-O2\x0cO|uYIXf3\t\t3.c2_'2 \x0cIK|_c.tO\x0cvEW3\t\t3;tI.2tIsO2'cF2 c.2>K2'cF\x0c2IX\x0ccKf3\t\t3YIVO2IK|2;>KOW22'OE.O\x0c|I'2;IE2<IV>K u|I'p2Ec2Xcc\x0c2E>YV\t \x0cIK|_c.tO\x0c2>E2.c2tIsO2Ec_O.t>K 2 cc|p2.c2_IVO2tO\x0c2E.\x0ccK O\x0cW3\t\t3;tO\x0cO2|cOE2'cF\x0c2 \x0cIK|_c.tO\x0c2->sOp2->..-O2\x0cO|uYIXf3\t\t3I2 cc|2{FI\x0c.O\x0c2ce2I2-OI FO2eI\x0c.tO\x0c2cK2>K2.tO2;cc|W22tO\x0c2tcFEO\tE.IK|E2FK|O\x0c2.tO2.t\x0cOO2-I\x0c O2cIVu.\x0cOOEp2.tO2KF.u.\x0cOOE2I\x0cO2RFE.\t<O-c;W22'cF2EF\x0cO-'2_FE.2VKc;2>.p32\x0cOX->O|2->..-O2\x0cO|uYIXW\t\t.tO2;c-e2.tcF t.2.c2t>_EO-ep2;tI.2I2.OK|O\x0c2'cFK 2Y\x0cOI.F\x0cOW22;tI.2I\tK>YO2X-F_X2_cF.teF-p2EtO2;>--2<O2<O..O\x0c2.c2OI.2.tIK2.tO2c-|\t;c_IKW22>2_FE.2IY.2Y\x0cIe.>-'p2Ec2IE2.c2YI.Yt2<c.tW22Ec2tO2;I-VO|\tec\x0c2I2Etc\x0c.2.>_O2<'2.tO2E>|O2ce2->..-O2\x0cO|uYIXp2IK|2.tOK2tO\tEI>|p23EOO2->..-O2\x0cO|uYIXp2tc;2X\x0cO..'2.tO2e-c;O\x0cE2I\x0cO2I<cF.2tO\x0cOW\t;t'2|c2'cF2Kc.2-ccV2\x0ccFK|W22>2<O->OsOp2.ccp2.tI.2'cF2|c2Kc.\ttOI\x0c2tc;2E;OO.-'2.tO2->..-O2<>\x0c|E2I\x0cO2E>K >K W22'cF2;I-V2 \x0cIsO-'\tI-cK 2IE2>e2'cF2;O\x0cO2 c>K 2.c2EYtcc-p2;t>-O2OsO\x0c'.t>K 2O-EO2cF.\ttO\x0cO2>K2.tO2;cc|2>E2_O\x0c\x0c'W3\t\t->..-O2\x0cO|uYIX2\x0cI>EO|2tO\x0c2O'OEp2IK|2;tOK2EtO2EI;2.tO2EFK<OI_E\t|IKY>K 2tO\x0cO2IK|2.tO\x0cO2.t\x0ccF t2.tO2.\x0cOOEp2IK|2X\x0cO..'2e-c;O\x0cE\t \x0cc;>K 2OsO\x0c';tO\x0cOp2EtO2.tcF t.p2EFXXcEO2>2.IVO2 \x0cIK|_c.tO\x0c2I\te\x0cOEt2KcEO I'W22.tI.2;cF-|2X-OIEO2tO\x0c2.ccW22>.2>E2Ec2OI\x0c-'2>K2.tO\t|I'2.tI.2>2EtI--2E.>--2 O.2.tO\x0cO2>K2 cc|2.>_OW22IK|2Ec2EtO2\x0cIK\te\x0cc_2.tO2XI.t2>K.c2.tO2;cc|2.c2-ccV2ec\x0c2e-c;O\x0cEW22IK|2;tOKOsO\x0c\tEtO2tI|2X>YVO|2cKOp2EtO2eIKY>O|2.tI.2EtO2EI;2I2E.>--2X\x0cO..>O\x0c2cKO\teI\x0c.tO\x0c2cKp2IK|2\x0cIK2Ie.O\x0c2>.p2IK|2Ec2 c.2|OOXO\x0c2IK|2|OOXO\x0c2>K.c\t.tO2;cc|W\t\t_OIK;t>-O2.tO2;c-e2\x0cIK2E.\x0cI> t.2.c2.tO2 \x0cIK|_c.tO\x0cvE2tcFEO2IK|\tVKcYVO|2I.2.tO2|cc\x0cW\t\t3;tc2>E2.tO\x0cOf3\t\t3->..-O2\x0cO|uYIXp32\x0cOX->O|2.tO2;c-eW223EtO2>E2<\x0c>K >K 2YIVO2IK|\t;>KOW22cXOK2.tO2|cc\x0cW3\t\t3->e.2.tO2-I.Ytp32YI--O|2cF.2.tO2 \x0cIK|_c.tO\x0cp23>2I_2.cc2;OIVp2IK|\tYIKKc.2 O.2FXW3\t\t.tO2;c-e2->e.O|2.tO2-I.Ytp2.tO2|cc\x0c2EX\x0cIK 2cXOKp2IK|2;>.tcF.\tEI'>K 2I2;c\x0c|2tO2;OK.2E.\x0cI> t.2.c2.tO2 \x0cIK|_c.tO\x0cvE2<O|p2IK|\t|OscF\x0cO|2tO\x0cW22.tOK2tO2XF.2cK2tO\x0c2Y-c.tOEp2|\x0cOEEO|2t>_EO-e2>K\ttO\x0c2YIXp2-I>|2t>_EO-e2>K2<O|2IK|2|\x0cO;2.tO2YF\x0c.I>KEW\t\t->..-O2\x0cO|uYIXp2tc;OsO\x0cp2tI|2<OOK2\x0cFKK>K 2I<cF.2X>YV>K 2e-c;O\x0cEp\tIK|2;tOK2EtO2tI|2 I.tO\x0cO|2Ec2_IK'2.tI.2EtO2YcF-|2YI\x0c\x0c'\tKc2_c\x0cOp2EtO2\x0cO_O_<O\x0cO|2tO\x0c2 \x0cIK|_c.tO\x0cp2IK|2EO.2cF.2cK2.tO\t;I'2.c2tO\x0cW\t\tEtO2;IE2EF\x0cX\x0c>EO|2.c2e>K|2.tO2Yc..I Ou|cc\x0c2E.IK|>K 2cXOKp2IK|\t;tOK2EtO2;OK.2>K.c2.tO2\x0ccc_p2EtO2tI|2EFYt2I2E.\x0cIK O2eOO->K 2.tI.\tEtO2EI>|2.c2tO\x0cEO-ep2ct2|OI\x0cp2tc;2FKOIE'2>2eOO-2.cu|I'p2IK|2I.\tc.tO\x0c2.>_OE2>2->VO2<O>K 2;>.t2 \x0cIK|_c.tO\x0c2Ec2_FYtW22EtO2YI--O|\tcF.p23 cc|2_c\x0cK>K p32<F.2\x0cOYO>sO|2Kc2IKE;O\x0cW22Ec2EtO2;OK.2.c2.tO\t<O|2IK|2|\x0cO;2<IYV2.tO2YF\x0c.I>KEW22.tO\x0cO2-I'2tO\x0c2 \x0cIK|_c.tO\x0c2;>.t\ttO\x0c2YIX2XF--O|2eI\x0c2csO\x0c2tO\x0c2eIYOp2IK|2-ccV>K 2sO\x0c'2E.\x0cIK OW\t\t3ctp2 \x0cIK|_c.tO\x0cp32EtO2EI>|p23;tI.2<> 2OI\x0cE2'cF2tIsOW3\t\t3.tO2<O..O\x0c2.c2tOI\x0c2'cF2;>.tp2_'2Yt>-|p32;IE2.tO2\x0cOX-'W\t\t3<F.p2 \x0cIK|_c.tO\x0cp2;tI.2<> 2O'OE2'cF2tIsOp32EtO2EI>|W\t\t3.tO2<O..O\x0c2.c2EOO2'cF2;>.tp32_'2|OI\x0cW\t\t3<F.p2 \x0cIK|_c.tO\x0cp2;tI.2-I\x0c O2tIK|E2'cF2tIsOW3\t\t3.tO2<O..O\x0c2.c2tF 2'cF2;>.tW3\t\t3ctp2<F.p2 \x0cIK|_c.tO\x0cp2;tI.2I2.O\x0c\x0c><-O2<> 2_cF.t2'cF2tIsOW3\t\t3.tO2<O..O\x0c2.c2OI.2'cF2;>.tW3\t\tIK|2EYI\x0cYO-'2tI|2.tO2;c-e2EI>|2.t>Ep2.tIK2;>.t2cKO2<cFK|2tO2;IE\tcF.2ce2<O|2IK|2E;I--c;O|2FX2\x0cO|uYIXW\t\t;tOK2.tO2;c-e2tI|2IXXOIEO|2t>E2IXXO.>.Op2tO2-I'2|c;K2I I>K2>K\t.tO2<O|p2eO--2IE-OOX2IK|2<O IK2.c2EKc\x0cO2sO\x0c'2-cF|W22.tO\ttFK.E_IK2;IE2RFE.2XIEE>K 2.tO2tcFEOp2IK|2.tcF t.2.c2t>_EO-ep2tc;\t.tO2c-|2;c_IK2>E2EKc\x0c>K W22>2_FE.2RFE.2EOO2>e2EtO2;IK.E2IK'.t>K W\t\tEc2tO2;OK.2>K.c2.tO2\x0ccc_p2IK|2;tOK2tO2YI_O2.c2.tO2<O|p2tO2EI;\t.tI.2.tO2;c-e2;IE2-'>K 2>K2>.W22|c2>2e>K|2'cF2tO\x0cOp2'cF2c-|\tE>KKO\x0cp2EI>|2tOW22>2tIsO2-cK 2EcF t.2'cFW22.tOK2RFE.2IE2tO2;IE2 c>K \t.c2e>\x0cO2I.2t>_p2>.2cYYF\x0c\x0cO|2.c2t>_2.tI.2.tO2;c-e2_> t.2tIsO\t|OscF\x0cO|2.tO2 \x0cIK|_c.tO\x0cp2IK|2.tI.2EtO2_> t.2E.>--2<O2EIsO|p2Ec\ttO2|>|2Kc.2e>\x0cOp2<F.2.ccV2I2XI>\x0c2ce2EY>EEc\x0cEp2IK|2<O IK2.c2YF.\tcXOK2.tO2E.c_IYt2ce2.tO2E-OOX>K 2;c-eW22;tOK2tO2tI|2_I|O2.;c\tEK>XEp2tO2EI;2.tO2->..-O2\x0cO|uYIX2Et>K>K p2IK|2.tOK2tO2_I|O2.;c\tEK>XE2_c\x0cOp2IK|2.tO2->..-O2 >\x0c-2EX\x0cIK 2cF.p2Y\x0c'>K p2Itp2tc;\te\x0c> t.OKO|2>2tIsO2<OOKW22tc;2|I\x0cV2>.2;IE2>KE>|O2.tO2;c-eW22IK|\tIe.O\x0c2.tI.2.tO2I O|2 \x0cIK|_c.tO\x0c2YI_O2cF.2I->sO2I-Ecp2<F.2EYI\x0cYO-'\tI<-O2.c2<\x0cOI.tOW22\x0cO|uYIXp2tc;OsO\x0cp2{F>YV-'\teO.YtO|2 \x0cOI.2E.cKOE2;>.t2;t>Yt2.tO'2e>--O|2.tO2;c-evE2<O--'p2IK|\t;tOK2tO2I;cVOp2tO2;IK.O|2.c2\x0cFK2I;I'p2<F.2.tO2E.cKOE2;O\x0cO2Ec\ttOIs'2.tI.2tO2Yc--IXEO|2I.2cKYOp2IK|2eO--2|OI|W\t\t.tOK2I--2.t\x0cOO2;O\x0cO2|O-> t.O|W22.tO2tFK.E_IK2|\x0cO;2cee2.tO2;c-evE\tEV>K2IK|2;OK.2tc_O2;>.t2>.W22.tO2 \x0cIK|_c.tO\x0c2I.O2.tO2YIVO2IK|\t|\x0cIKV2.tO2;>KO2;t>Yt2\x0cO|uYIX2tI|2<\x0ccF t.p2IK|2\x0cOs>sO|p2<F.\t\x0cO|uYIX2.tcF t.2.c2tO\x0cEO-ep2IE2-cK 2IE2>2->sOp2>2;>--2KOsO\x0c2<'\t_'EO-e2-OIsO2.tO2XI.tp2.c2\x0cFK2>K.c2.tO2;cc|p2;tOK2_'2_c.tO\x0c2tIE\tec\x0c<>||OK2_O2.c2|c2EcW\t\t>.2>E2I-Ec2\x0cO-I.O|2.tI.2cKYO2;tOK2\x0cO|uYIX2;IE2I I>K2.IV>K 2YIVOE\t.c2.tO2c-|2 \x0cIK|_c.tO\x0cp2IKc.tO\x0c2;c-e2EXcVO2.c2tO\x0cp2IK|2.\x0c>O|2.c\tOK.>YO2tO\x0c2e\x0cc_2.tO2XI.tW22\x0cO|uYIXp2tc;OsO\x0cp2;IE2cK2tO\x0c2 FI\x0c|p\tIK|2;OK.2E.\x0cI> t.2ec\x0c;I\x0c|2cK2tO\x0c2;I'p2IK|2.c-|2tO\x0c2 \x0cIK|_c.tO\x0c\t.tI.2EtO2tI|2_O.2.tO2;c-ep2IK|2.tI.2tO2tI|2EI>|2 cc|u_c\x0cK>K 2.c\ttO\x0cp2<F.2;>.t2EFYt2I2;>YVO|2-ccV2>K2t>E2O'OEp2.tI.2>e2.tO'2tI|\tKc.2<OOK2cK2.tO2XF<->Y2\x0ccI|2EtO2;IE2YO\x0c.I>K2tO2;cF-|2tIsO2OI.OK\ttO\x0c2FXW22;O--p2EI>|2.tO2 \x0cIK|_c.tO\x0cp2;O2;>--2EtF.2.tO2|cc\x0cp2.tI.\ttO2_I'2Kc.2Yc_O2>KW22EccK2Ie.O\x0c;I\x0c|E2.tO2;c-e2VKcYVO|p2IK|2Y\x0c>O|p\tcXOK2.tO2|cc\x0cp2 \x0cIK|_c.tO\x0cp2>2I_2->..-O2\x0cO|uYIXp2IK|2I_2<\x0c>K >K \t'cF2Ec_O2YIVOEW22<F.2.tO'2|>|2Kc.2EXOIVp2c\x0c2cXOK2.tO2|cc\x0cp2Ec\t.tO2 \x0cO'u<OI\x0c|2E.c-O2.;>YO2c\x0c2.t\x0c>YO2\x0ccFK|2.tO2tcFEOp2IK|2I.2-IE.\tRF_XO|2cK2.tO2\x0cccep2>K.OK|>K 2.c2;I>.2FK.>-2\x0cO|uYIX2;OK.2tc_O2>K\t.tO2OsOK>K p2IK|2.tOK2.c2E.OI-2Ie.O\x0c2tO\x0c2IK|2|OscF\x0c2tO\x0c2>K2.tO\t|I\x0cVKOEEW22<F.2.tO2 \x0cIK|_c.tO\x0c2EI;2;tI.2;IE2>K2t>E2.tcF t.EW22>K\te\x0ccK.2ce2.tO2tcFEO2;IE2I2 \x0cOI.2E.cKO2.\x0ccF tp2Ec2EtO2EI>|2.c2.tO\tYt>-|p2.IVO2.tO2XI>-p2\x0cO|uYIXW22>2_I|O2Ec_O2EIFEI OE2'OE.O\x0c|I'p\tEc2YI\x0c\x0c'2.tO2;I.O\x0c2>K2;t>Yt2>2<c>-O|2.tO_2.c2.tO2.\x0ccF tW22\x0cO|uYIX\tYI\x0c\x0c>O|2FK.>-2.tO2 \x0cOI.2.\x0ccF t2;IE2{F>.O2eF--W222.tOK2.tO2E_O--\tce2.tO2EIFEI OE2\x0cOIYtO|2.tO2;c-ep2IK|2tO2EK>eeO|2IK|2XOOXO|\t|c;Kp2IK|2I.2-IE.2E.\x0cO.YtO|2cF.2t>E2KOYV2Ec2eI\x0c2.tI.2tO2YcF-|\tKc2-cK O\x0c2VOOX2t>E2ecc.>K 2IK|2<O IK2.c2E->Xp2IK|2E->XXO|2|c;K\te\x0cc_2.tO2\x0ccce2E.\x0cI> t.2>K.c2.tO2 \x0cOI.2.\x0ccF tp2IK|2;IE2|\x0cc;KO|W\t<F.2\x0cO|uYIX2;OK.2Rc'cFE-'2tc_Op2IK|2Kc2cKO2OsO\x0c2|>|2IK'.t>K \t.c2tI\x0c_2tO\x0c2I I>KW\t\n"
```

## 2.2 Running the second function - sol2()

Code

```python
def sol2():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    print('The message is: {}'. format(message))
    conn.sendline("2")  # select challenge 2

    dontcare = conn.recvuntil(':')
    print('The dontcare is: {}'.format(dontcare))
    challenge = conn.recvline()
    print('The challenge is: {}'.format(challenge))
    # some all zero mask.
    # TODO: find the magic mask!
    mask = int(0).to_bytes(len(message), 'big')
    print('The mask is: {}'.format(mask))
    message = XOR(challenge, mask)
    conn.send(message)
    message = conn.recvline()
    message = conn.recvline()
    if b'points' in message:
        print(message)
    conn.close()
```

We run the function with `python3 lab2Client.py`

![](assets/14.PNG)

# 3. Exercise 1



# 4. Exercise 2

## 4.1 Strategy

The strategy is similar to what was thought in Week 2 Lecture 1 Slide 7

- Basically we XOR the original message with our altered message. This will be the mask
- Then we XOR the mask and the challenge c (Note that the challenge is derived from the XOR of the message and the key)
- We then pass the result of the previous step to the server which returns the altered message when it XOR with the key

![](assets/15.PNG)



## 4.2 Code

![](assets/16.PNG)

## 4.3 Results

![](assets/17.PNG)

# 5. Miscellaneous

Path to the working directory

- For convenience so that we can change directory without navigating too much

```
/mnt/c/Users/Glenn/Desktop/Github/50_042_foundations_of_cybersecurity/lab2
```


