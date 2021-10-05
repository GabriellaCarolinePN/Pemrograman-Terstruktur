Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # import library
>>> import time
>>> import datetime
>>> 
>>> # input nama user
>>> nama = input("Hallo... nama saya Mr. Kompie, nama Anda siapa? ")
Hallo... nama saya Mr. Kompie, nama Anda siapa? Gabriella
>>> 
>>> # tampilkan nama user
>>> print("Oh.. nama Anda", nama, ", nama yang bagus sekali.")
Oh.. nama Anda Gabriella , nama yang bagus sekali.
>>> 
>>> # kasih jeda 3 detik
>>> time.sleep(3)
>>> 
>>> # input tahun lahir
>>> thnLahir = int(input("BTW... " + nama + " kamu lahir tahun berapa? "))
BTW... Gabriella kamu lahir tahun berapa? 2003
>>> 
>>> # kasih jeda 3 detik
>>> time.sleep(3)
>>> 
>>> # hitung usia user
>>> skrg = datetime.datetime.now()
>>> usia = skrg.year - thnLahir
>>> 
>>> # tampilkan usia
>>> print("Hmmm... ", nama, " kamu sudah", usia, " tahun ya..")
Hmmm...  Gabriella  kamu sudah 18  tahun ya..
>>> 
>>> # kasih jeda 3 detik
>>> time.sleep(3)
>>> 
>>> # tampilkan pesan sesuai range usia
>>> if (usia > 50):
	print("Anda sudah cukup tua ya?")
	print("Jaga kesehatan ya!!")
elif (usia > 20):
	print("Ternyata Anda masih cukup muda belia")
	print("Jangan sia-siakan masa mudamu ya!!")
elif (usia > 17):
	print("Hihihi... Anda ternyata masih ABG")
	print("Mulai berpikirlah secara dewasa ya!!")
else:
	print("Oalah.. Anda masih anak-anak toh?")
	print("Jangan suka merengek-rengek minta jajan ya!!")

	
Hihihi... Anda ternyata masih ABG
Mulai berpikirlah secara dewasa ya!!
>>> 
>>> # kasih jeda 3 detik
>>> time.sleep(3)
>>> 
>>> # say goodbye
>>> print("OK.. see you later", nama, ".. senang berkenalan denganmu")
OK.. see you later Gabriella .. senang berkenalan denganmu
>>> 