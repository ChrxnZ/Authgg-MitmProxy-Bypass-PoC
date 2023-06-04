# auth.gg Bypass
### About the Project
This Bypass allows you to spoof the HTTP-POST request JSON response of api.auth.gg to allow immediate access.
There will be 2 versions of files, the bypass ([Bypass.py](https://github.com/ChrxnZ/Auth.GG-MitmProxy-Bypass/blob/main/src/Bypass.py)), and another file which allows you to further on spoof the HTTP-POST request JSON response ([Spoof.py](https://github.com/ChrxnZ/Auth.GG-MitmProxy-Bypass/blob/main/src/Spoof.py)).
### Background Information
This bypass was originally made over 3 months ago (which could make this the first official actual working bypass). The bypass was made alongside multiple people, consisting of Me (ChrxnZ/Pulsed#1874), [YeetDisDude](https://github.com/YeetDisDude) & [TonicBoomerKewl](https://github.com/TonicBoomerKewl).
### More Information
This project was made to be as small as possible for efficiency, in which we got it to work on a 2GB Ram + Intel Celeron Laptop, which could also perhaps make it the smallest auth.gg Bypass.
### Where the Project was found to work
We mostly tested the bypass on Mod Menus which used auth.gg's authentication system on both IOS & Android systems including:
- ZygiskPG / zyCheatsPG (Android)
- Rednick / Red16's PG3D Mod Menu (IOS)
### Notes
I will not be maintaining this project. If it gets patched, it's patched and there's nothing I will do. Also note that this bypass **was patched before in ZygiskPG by [Fedesito](https://github.com/fedes1to) using a weird system** (which i doubt you'll be able to find on the internet anywhere).
### Credits
- Idea : [TonicBoomerKewl](https://github.com/TonicBoomerKewl)
- Testing & Improvement : [YeetDisDude](https://github.com/YeetDisDude)
- Creation : Me (ChrxnZ/Pulsed#1874)
# License
### This repository is licensed under the [Creative Commons Zero v1.0 Universal (CC0-1.0) license](https://github.com/ChrxnZ/Auth.GG-MitmProxy-Bypass/blob/main/LICENSE)
This allows you to use this repository and its contents for {Commercial Use, Modification with giving credits to the original creator (Me), Distribution amongst others, and Private Use}, However, you are not given permissions to {Take liability And/Or Warranty for this original project (in other words, don't take credits), or use in trademark and/or patent purposes}.

# Setup
### Minimum Requirements
Pc/Laptop with:
- Windows 8.1-11?
- 2GB Ram
- Intel Celeron
- Python 3.7+
- MitmProxy PC Certificate & Python Module
- PyperClip Python Module

If bypass is desired to work on a mobile device:
- MitmProxy Mobile Certificate
- [Super Proxy Application](https://play.google.com/store/apps/details?id=com.scheler.superproxy) (Android)

IOS Requirements yet to come (WIP LIKELY BY YEETDISDUDE)

# Tutorial(s)
### PC
Here are the following steps to get the bypass working on PC:
- Go to Proxy settings on your PC
- Enter the address as **127.0.0.1** & the Port as **8080**
- Click Save (Internet will stop working until you run the bypass)
- Run (**Bypass.py**)
- Open either Terminal or CMD
- Perform a Paste (Ctrl + V)
- Click Enter
- Open the application which uses auth.gg Authentication
Easy as that. (Video to be made soon)
### Mobile Devices (Android)
WIP!
### Mobile & iPad Devices (IOS)
1) On your PC, open powershell and type ipconfig and get your pc's local IP
2) On your iPhone/iPad go to Settings > WiFi > Configure Proxy > Select Manual and type in your PC's ipv4 address and type 8080 for the port
3) Go to https://mitm.it and get the certificate
4) Trust the certificate and on your PC run mitmweb -s path/to/script.py
5) Open the Application which uses auth.gg and login with any username/password
