# cursor

this proj is begain by half learning and half interest, i am interested in this because what to finally build a Thinkpad TracePoint-link curosr to use in daily life

refer:
[various hardware implementations of TrackPoint](https://deskthority.net/wiki/TrackPoint_Hardware)
[Trackpoint mod](https://www.keebtalk.com/t/trackpoint-mod/14368)
[The fundamental difference between trackpoints and joystics is that trackpoints are not physically moving, they react to pressure](https://github.com/joric/jorne/wiki/Trackpoint)



---

1.1_button-esp32-pythonInPC is using the button to contrl the cursor in PC

the Pin connections between esp32 and button are:

D2 -->VRX
D4 --> VRY
D17 --> SW(not in use)

and esp32 connect PC at COM10
![alt text](./img/346b30169b3f568504811cadf3949b5.jpg)

