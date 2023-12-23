# [ ________________________XIAOMI_USER-AGENTS________________________________] #
#________________________________________________________________________________#

# [ _____________DETAILS________________] #
#This Script is written by : PrinceHamzaYT
#AUTHER : PrinceHamzaYT
# [ _____________MODULES________________] #
import random
import os
import string
# [ _____________COLOURS________________] #
P = '\x1b[1;97m';M = '\x1b[1;91m';H = '\x1b[1;92m';K = '\x1b[1;93m';B = '\x1b[1;94m';U = '\x1b[1;95m';O = '\x1b[1;96m';N = '\x1b[0m';A = '\x1b[1;90m'
BN = '\x1b[1;107m';BBL = '\x1b[1;106m';BP = '\x1b[1;105m';BB = '\x1b[1;104m';BK = '\x1b[1;103m';BH = '\x1b[1;102m';BM = '\x1b[1;101m';BA = '\x1b[1;100m'
# [ _____________LOGO________________] #
os.system('clear')
logo = (f'''\x1b[1;92m
    ██████  ██████  ██ ███    ██  ██████ ███████ 
    ██   ██ ██   ██ ██ ████   ██ ██      ██      
    ██████  ██████  ██ ██ ██  ██ ██      █████   
    ██      ██   ██ ██ ██  ██ ██ ██      ██      
    ██      ██   ██ ██ ██   ████  ██████ ███████ \x1b[0m
 
╭──────────  \x1b[1;92m•\x1b[1;91m•\x1b[1;96m• \x1b[0mPrince Command \x1b[1;96m•\x1b[1;91m•\x1b[1;92m• \x1b[0m ─────────────╮
│           WELCOME TO PRINCE COMMAND             │
╰─────────────────────────────────────────────────╯
 
  ╭─────  \x1b[1;92m•\x1b[1;91m•\x1b[1;96m• \x1b[0mDEVELOVER INFORMATION \x1b[1;96m•\x1b[1;91m•\x1b[1;92m• \x1b[0m ─────╮
  │         Auther :  Prince Hamza YT         │
  ╰───────────────────────────────────────────╯
     ╭──────  \x1b[1;92m•\x1b[1;91m•\x1b[1;96m• \x1b[0m Xiaomi-UA \x1b[1;96m•\x1b[1;91m•\x1b[1;92m• \x1b[0m  ──────────╮
     │      Xiaomi-USER-AGENT-SCRIPT         │
     ╰───────────────────────────────────────╯''')
     
print(logo)
print(60*'─')
x1 = 'FBDV/Redmi 01A;FBSV/10';x2 = 'FBDV/Xiaomi Redmi 1;FBSV/4.2.1';x3 = 'FBDV/21061119DG;FBSV/11';x4 = 'FBDV/22011119UY;FBSV/12';x5 = 'FBDV/22041219NY;FBSV/12';x6 = 'FBDV/220333QBI;FBSV/12';x7 = 'FBDV/21061119BI;FBSV/11';x8 = 'FBDV/22011119TI;FBSV/11';x9 = 'FBDV/22041219I;FBSV/11';x10 = 'FBDV/220233L2C;FBSV/11';x11 = 'FBDV/220333QL;FBSV/11';x12 = 'FBDV/Redmi 10I;FBSV/7.0.1';x13 = 'FBDV/Redmi 10S;FBSV/9.3.3';x14 = 'FBDV/M2004J7AC;FBSV/10';x15 = 'FBDV/M2004J7BC;FBSV/10';x16 = 'FBDV/Redmi 11 lite;FBSV/7.1.1';x17 = 'FBDV/22071219AI;FBSV/12';x18 = 'FBDV/Redmi 11X;FBSV/10';x19 = 'FBDV/23053RN02A;FBSV/13';x20 = 'FBDV/23076RN4BI;FBSV/13';x21 = 'FBDV/2212ARNC4L;FBSV/12';x22 = 'FBDV/23100RN82L;FBSV/13';x23 = 'FBDV/Redmi 19049;FBSV/10';x24 = 'FBDV/HM 1S ;FBSV/4.4.4';x25 = 'FBDV/wt88047;FBSV/5.1.1';x26 = 'FBDV/HM 2A;FBSV/4.4.4';x27 = 'FBDV/Redmi 3;FBSV/5.1.1';x28 = 'FBDV/Redmi 3S;FBSV/6.0.1';x29 = 'FBDV/Redmi 3X;FBSV/6.0.1';x30 = 'FBDV/Redmi 4;FBSV/7.1.2';x31 = 'FBDV/Redmi 4 Prime;FBSV/7.1.2';x32 = 'FBDV/Redmi 4 Pro;FBSV/9';x33 = 'FBDV/Redmi 41224;FBSV/10';x34 = 'FBDV/Redmi 4A;FBSV/7.1.2';x35 = 'FBDV/Redmi 4X;FBSV/7.1.2';x36 = 'FBDV/Redmi 5;FBSV/7.1.2';x37 = 'FBDV/Redmi 5 Plus;FBSV/8.1';x38 = 'FBDV/Redmi 5 pro;FBSV/7.1.2';x39 = 'FBDV/Redmi 5A;FBSV/7.1.2';x40 = 'FBDV/Redmi 5Plus;FBSV/7.1.1';x41 = 'FBDV/Redmi 5pro;FBSV/7.1.2';x42 = 'FBDV/Redmi 5S;FBSV/10.0.1';x43 = 'FBDV/Redmi 6;FBSV/8.1.0';x44 = 'FBDV/Redmi 6 Pro;FBSV/9';x45 = 'FBDV/Redmi 6 Pro Extreme;FBSV/9';x46 = 'FBDV/Redmi 6A;FBSV/9';x47 = 'FBDV/Redmi 6A;FBSV/9';x48 = 'FBDV/Redmi 6Pro;FBSV/8.1';x49 = 'FBDV/Redmi 7;FBSV/9';x50 = 'FBDV/Redmi 7 Pro;FBSV/8.1';x51 = 'FBDV/Redmi 7A;FBSV/10';x52 = 'FBDV/Redmi 7I;FBSV/7.1.1';x53 = 'FBDV/Redmi 8;FBSV/10';x54 = 'FBDV/Redmi 85781;FBSV/10';x55 = 'FBDV/Redmi 8A;FBSV/9';x56 = 'FBDV/Redmi 8A Dual;FBSV/9';x57 = 'FBDV/Redmi 8A Pro;FBSV/9';x58 = 'FBDV/M2004J19C;FBSV/11';x59 = 'FBDV/M2010J19SI;FBSV/11';x60 = 'FBDV/Redmi 9 Prime;FBSV/10';x61 = 'FBDV/Redmi 9 Pro;FBSV/7.1.2';x62 = 'FBDV/Redmi 99070;FBSV/10';x63 = 'FBDV/M2006C3LG;FBSV/10';x64 = 'FBDV/Redmi 9AT;FBSV/10';x65 = 'FBDV/M2006C3MG;FBSV/10';x66 = 'FBDV/M2006C3MNG;FBSV/10';x67 = 'FBDV/Redmi 9Prime;FBSV/11.1.1';x68 = 'FBDV/Redmi 9pro;FBSV/7.1.2';x69 = 'FBDV/M2010J19SY;FBSV/10';x70 = 'FBDV/Redmi 9T NFC;FBSV/11';x71 = 'FBDV/220733SG;FBSV/12';x72 = 'FBDV/220733SFG;FBSV/12';x73 = 'FBDV/23028RN4DG;FBSV/12';x74 = 'FBDV/23028RNCAG;FBSV/13';x75 = 'FBDV/Redmi A3;FBSV/7.1.1';x76 = 'FBDV/Redmi A8;FBSV/10.0.1';x77 = 'FBDV/Redmi A90;FBSV/11.1.1';x78 = 'FBDV/Redmi Go;FBSV/8.1.0';x79 = 'FBDV/Redmi K20;FBSV/10';x80 = 'FBDV/Redmi K20 Pro;FBSV/9';x81 = 'FBDV/Redmi K20 Pro Premium Edition;FBSV/10';x82 = 'FBDV/Redmi K20Pro;FBSV/10';x83 = 'FBDV/Redmi K30;FBSV/11';x84 = 'FBDV/M1912G7BC;FBSV/10';x85 = 'FBDV/Redmi K30 5G;FBSV/11';x86 = 'FBDV/Redmi K30 Pro;FBSV/11';x87 = 'FBDV/Redmi K30 Pro Zoom;FBSV/10';x88 = 'FBDV/Redmi K30 Pro Zoom Edition;FBSV/11';x89 = 'FBDV/M2006J10C;FBSV/11';x90 = 'FBDV/Redmi K30i 5G;FBSV/10';x91 = 'FBDV/Redmi K30S;FBSV/10';x92 = 'FBDV/Redmi K30S Ultra;FBSV/11';x93 = 'FBDV/M2012K11AC;FBSV/12';x94 = 'FBDV/M2012K11AC;FBSV/12';x95 = 'FBDV/M2012K10C;FBSV/11';x96 = 'FBDV/M2012K11C;FBSV/11';x97 = 'FBDV/Redmi K40 Pro+;FBSV/11';x98 = 'FBDV/22021211RC;FBSV/13';x99 = 'FBDV/22021211RC;FBSV/12';x100 = 'FBDV/22041216I;FBSV/12';k1 = 'FBDV/Redmi Y1;FBSV/7.1.2';k2 = 'FBDV/Redmi Y1 Lite;FBSV/7.1.2.';k3 = 'FBDV/Redmi Note 5A;FBSV/7.1.2'
y1 = 'FBDV/23013RK75C;FBSV/13';y2 = 'FBDV/22127RK46C;FBSV/13';y3 = 'FBDV/23078RKD5C;FBSV/14';y4 = 'FBDV/22122RK93C;FBSV/13';y5 = 'FBDV/HM NOTE 1W;FBSV/4.4.2';y6 = 'FBDV/Redmi Note 1;FBSV/7.1.2';y7 = 'FBDV/M2101K7AI;FBSV/11';y8 = 'FBDV/M2103K19G;FBSV/11';y9 = 'FBDV/XIG02;FBSV/11';y10 = 'FBDV/Redmi Note 10 Lite;FBSV/10';y11 = 'FBDV/M2101K6G;FBSV/12';y12 = 'FBDV/Redmi Note 10 Pro Max;FBSV/11';y13 = 'FBDV/Redmi Note 10S;FBSV/12';y14 = 'FBDV/M2103K19Y;FBSV/11';y15 = 'FBDV/M2103K19I;FBSV/11';y16 = 'FBDV/M2003J15SC;FBSV/10';y17 = 'FBDV/Redmi Note 11;FBSV/12';y18 = 'FBDV/2201117TG;FBSV/12';y19 = 'FBDV/21091116AC;FBSV/11';y20 = 'FBDV/2201116TG;FBSV/11';y21 = 'FBDV/2201116SG;FBSV/12';y22 = 'FBDV/21091116UC;FBSV/13';y23 = 'FBDV/2201116SI;FBSV/12';y24 = 'FBDV/22087RA4DI;FBSV/11';y25 = 'FBDV/22041219C;FBSV/12';y26 = 'FBDV/2201116SC;FBSV/11';y27 = 'FBDV/Redmi Note 11R;FBSV/12';y28 = 'FBDV/22095RA98C;FBSV/12';y29 = 'FBDV/2201117SI;FBSV/11';y30 = 'FBDV/22031116BG;FBSV/11';y31 = 'FBDV/21091116AI;FBSV/11';y32 = 'FBDV/22041216C;FBSV/13';y33 = 'FBDV/22041216UC;FBSV/13';y34 = 'FBDV/23021RAAEG;FBSV/13';y35 = 'FBDV/22101316UP;FBSV/12';y36 = 'FBDV/22101316G;FBSV/12';y37 = 'FBDV/22101316UC;FBSV/13';y38 = 'FBDV/22101320C;FBSV/12';y39 = 'FBDV/22101316UCP;FBSV/12';y40 = 'FBDV/22101316UG;FBSV/12';y41 = 'FBDV/23076RA4BC;FBSV/13';y42 = 'FBDV/2303ERA42L;FBSV/13';y43 = 'FBDV/23049RAD8C;FBSV/13';y44 = 'FBDV/23054RA19C;FBSV/13';y45 = 'FBDV/Redmi Note 13;FBSV/13';y46 = 'FBDV/2312DRAABC;FBSV/13';y47 = 'FBDV/2312DRA50C;FBSV/13';y48 = 'FBDV/23090RA98C;FBSV/13';y49 = 'FBDV/RedMi Note 15 Pro;FBSV/9';y50 = 'FBDV/Redmi Note 16 Pro;FBSV/9';y51 = 'FBDV/Redmi Note 1LTE;FBSV/8.1.0';y52 = 'FBDV/Redmi Note 2;FBSV/5.0.2';y53 = 'FBDV/Redmi Note 27;FBSV/5.0.2';y54 = 'FBDV/Redmi Note 3;FBSV/6.0.1';y55 = 'FBDV/Redmi Note 3 Pro;FBSV/7.0';y56 = 'FBDV/Redmi Note 4;FBSV/6.0';y57 = 'FBDV/Redmi Note 4 Pro;FBSV/9';y58 = 'FBDV/Redmi Note 4A;FBSV/7.1.2';y59 = 'FBDV/HM NOTE 1LTE;FBSV/4.4.4';y60 = 'FBDV/Redmi Note 4X;FBSV/6.0';y61 = 'FBDV/Redmi Note 5;FBSV/9';y62 = 'FBDV/Redmi Note 5 Pro;FBSV/9';y63 = 'FBDV/Redmi Note 5A;FBSV/7.1.2';y64 = 'FBDV/Redmi Note 5A Lite;FBSV/11';y65 = 'FBDV/Redmi Note 5A Prime;FBSV/7.1.2';y66 = 'FBDV/Redmi note 6;FBSV/11.0.1';y67 = 'FBDV/Redmi Note 6 Pro;FBSV/8.1.0';y68 = 'FBDV/Redmi Note 6Pro;FBSV/8.1';y69 = 'FBDV/Redmi Note 7;FBSV/10';y70 = 'FBDV/Redmi Note 7 Pro;FBSV/10';y71 = 'FBDV/Redmi Note 7Pro;FBSV/9.0';y72 = 'FBDV/Redmi Note 7S;FBSV/9';y73 = 'FBDV/Redmi Note 8;FBSV/9';y74 = 'FBDV/M1908C3JGG;FBSV/11';y75 = 'FBDV/Redmi Note 8 Pro;FBSV/10';y76 = 'FBDV/Redmi Note 8T;FBSV/10';y77 = 'FBDV/Redmi Note 9;FBSV/10';y78 = 'FBDV/M2007J22C;FBSV/10';y79 = 'FBDV/Redmi Note 9 Pro;FBSV/11';y80 = 'FBDV/M2007J17C;FBSV/10';y81 = 'FBDV/Redmi Note 9 Pro Max;FBSV/10';y82 = 'FBDV/Redmi Note 95;FBSV/12';y83 = 'FBDV/Redmi Note 9S;FBSV/12';y84 = 'FBDV/Redmi Note 9T;FBSV/12';y85 = 'FBDV/M2007J22G;FBSV/11';y86 = 'FBDV/Redmi Note Prime;FBSV/8.1.0';y87 = 'FBDV/Redmi Note10 Pro;FBSV/11';y88 = 'FBDV/Redmi Note10S;FBSV/11';y89 = 'FBDV/Redmi Note10T 5G;FBSV/11';y90 = 'FBDV/Redmi Note5;FBSV/9';y91 = 'FBDV/Redmi Note7;FBSV/9.0';y92 = 'FBDV/Redmi Note7S;FBSV/9.0';y93 = 'FBDV/Redmi Note8;FBSV/11';y94 = 'FBDV/Redmi Note8T;FBSV/9.0';y95 = 'FBDV/Redmi Note9 Pro 5G;FBSV/10';y96 = 'FBDV/Redmi Note9S Pro;FBSV/10';y97 = 'FBDV/22081283G;FBSV/12';y98 = 'FBDV/Redmi Pro;FBSV/6.0';y99 = 'FBDV/Redmi S2;FBSV/9';y100 = 'FBDV/Redmi S2;FBSV/9'
xp = random.choice([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36,x37,x38,x39,x40,x41,x42,x43,x44,x45,x46,x47,x48,x49,x50,x51,x52,x53,x54,x55,x56,x57,x58,x59,x60,x61,x62,x63,x64,x65,x66,x67,x68,x69,x70,x71,x72,x73,x74,x75,x76,x77,x78,x79,x80,x81,x82,x83,x84,x85,x86,x87,x88,x89,x90,x91,x92,x93,x94,x95,x96,x97,x98,x99,x100,k1,k2,k3])
yp = random.choice([y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18,y19,y20,y21,y22,y23,y24,y25,y26,y27,y28,y29,y30,y31,y32,y33,y34,y35,y36,y37,y38,y39,y40,y41,y42,y43,y44,y45,y46,y47,y48,y49,y50,y51,y52,y53,y54,y55,y56,y57,y58,y59,y60,y61,y62,y63,y64,y65,y66,y67,y68,y69,y70,y71,y72,y73,y74,y75,y76,y77,y78,y79,y80,y81,y82,y83,y84,y85,y86,y87,y88,y89,y90,y91,y92,y93,y94,y95,y96,y97,y98,y99,y100])
xiaomi_prince = random.choice([xp,yp])

facebook = f"{random.randint(120, 441)}.0.0.{random.randint(1000, 6000)}"
facebook_version = f'{random.randint(10,441)}.0.0.{random.randint(11,99)}.{random.randint(1,250)}'
fbv = random.randint(1111111, 9999999)
fbbv = random.randint(111111111, 999999999)
fbrv = random.randint(111111111, 999999999)
us_sim = random.choice(["AT&T","Airtel","T-Mobile","Verizon","Ultra Mobile","Mint Mobile","Joi","null","Ufone","Zong","Telenor","Jazz"])
density = random.choice(["2.0","2.25","2.75","3.0","3.25","3.75","4.0"])
width = random.randint(720, 1440)
height = random.randint(1080, 2560)
colour = random.choice([P,M,H,K,U,B,O,N,A])
ua = f'{colour}[FBAN/FB4A;FBAV/{facebook};FBBV/{fbv};[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};FBPN/com.facebook.katana;FBLC/en_US;FBCR/{us_sim};FBMF/Xiaomi;FBBD/Redmi;{xiaomi_prince};nullFBCA/armeabi-v7a:armeabi;FBDM/'+'{'+f'density={density},width={width},height={height};FB_FW/1;]'
print(ua)
print(60*'\x1b[0m─')
#________________________________________________________________________________#
#________________________________________________________________________________#
