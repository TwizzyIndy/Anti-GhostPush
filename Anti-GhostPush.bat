@echo off
cls
:main
echo ##################################
echo ##################################
echo # TwizzyIndy    			  	 ##
echo # MonkeyTest^&TimeService Remover##
echo ##################################
echo ##################################
echo Myanmar Online Family
echo http://mof.asia/forum.php
echo.
echo waiting device ...
adb wait-for-device
echo installing busybox ...
adb push busybox /data/local/tmp
adb shell "su -c 'chmod 777 /data/local/tmp/busybox'"
adb shell "su -c '/data/local/tmp/busybox mount -o remount,rw /system'"
adb shell "su -c 'dd if=/data/local/tmp/busybox of=/system/bin/busybox'"
adb shell "su -c 'chmod 644 /system/bin/busybox'"
echo removing unwanted files ..(1/5)
adb shell "su -c busybox 'mount -o remount,rw /system';busybox busybox chattr -i -a /system/xbin/.*;busybox busybox chattr –i -a /system/bin/daemonuis;busybox busybox chattr –i -a /system/bin/debuggerd;busybox busybox chattr –i -a /system/bin/nis;busybox chattr –i -a /system/bin/daemonnis;busybox chattr –i -a /system/bin/uis;busybox chattr –i -a /system/bin/mis;busybox chattr –i -a /system/bin/daemonmis;rm -rf /system/xbin/.*;rm /system/bin/daemonuis;rm /system/bin/uis;rm /system/bin/debuggerd;rm /system/bin/nis;rm /system/bin/daemonnis;cp /system/bin/debuggerd_test /system/bin/debuggerd"
echo removing unwanted files .. (2/5)
adb shell "su -c 'pm disable com.google.model.mi';busybox chattr –i -a /system/app/com.android.hardware.ext0.apk;rm /system/app/com.android.hardware.ext0.apk;busybox chattr –i -a /system/app/com.google.model.mi.apk;rm /system/app/com.google.model.mi.apk;busybox chattr –i -a /system/app/com.google.fk.json.slo.apk;rm /system/app/com.google.fk.json.slo.apk;busybox chattr –i -a /system/app/com.android.wp.net.log.apk;rm /system/app/com.android.wp.net.log.apk;busybox chattr –i -a /system/app/playstoreupdate.apk;rm /system/app/playstoreupdate.apk;busybox chattr -i -a /system/priv-app/playstoreupdate.apk;rm /system/priv-app/playstoreupdate.apk;busybox chattr –i -a /system/app/Models.apk;rm /system/app/Models.apk"
echo removing unwanted files .. (3/5)
adb shell "su -c 'busybox chattr -a -i /system/priv-app/Models.apk';rm /system/priv-app/Models.apk;busybox chattr -a -i /system/etc/install-recovery.sh;su -c 'pm disable com.google.fk.json.slo'"
echo removing unwanted files .. (4/5)
adb shell "busybox chattr -i -a /system/app/providerdown.apk;rm /system/app/providerdown.apk;rm /system/lib/libjackpal-androidterm4.so;rm /data/local/.usfo;busybox chattr –i -a /system/priv-app/cameraupdate.apk;busybox busybox chattr –i -a /system/priv-app/com.android.wp.net.log.apk;rm -rf /data/data/com.android.camera.update;rm -rf /data/data/com.android.wp.net.log;rm  /systam/priv-app/cameraupdate.apk;rm  /systam/priv-app/com.android.wp.net.log.apk"
echo protecting you from that thing again .. (5/5)
adb shell "su -c echo -e '\\nhttp://down.upgamecdn.com		127.0.0.1\\nhttp://massla.hdyfhpoi.com		127.0.0.1\\nhttp://u.syllyq1n.com		127.0.0.1'>>/system/etc/hosts"
echo your device will getting reboot ..
adb reboot
echo bye ..
pause
cls
goto main