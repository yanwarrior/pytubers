import os
import pyautogui as gui
import pafy
import sys
import tkinter, tkinter.filedialog
import time

print("""
PYTUBE - Youtube Video Downloader (1.0.0)
_Yanwar Solahudin yanwarsolahudin@gmail.com
--------------------------------------------
""")

def select_directory():
	"""Seleksi direktori tempat menyimpan video"""
	root = tkinter.Tk()
	title = "Pilih direktori untuk menyimpan video"
	dirname = tkinter.filedialog.askdirectory(parent=root,
		initialdir="/", title=title)
	if len(dirname) > 0:
		return dirname


def sanitize_file(filename):
	forbiden_char = [ ":", "*", "?", "<", ">", "|"]
	for fc in forbiden_char:
		if fc in filename:
			filename = filename.replace(fc,"-")
	return filename


def loading_bar(total, recvd, ratio, rate, eta):
	"""Menampilkan loading bar di command line."""
	sys.stdout.write("\reta {}% Sedang mengunduh...".format(int(eta)))
	sys.stdout.flush()


def unduh_video(url_video, direktori):
	"""Mengunduh video youtube"""
	try:
		if direktori:
			video = pafy.new(url_video)

			# tampilkan judul video
			print("Title\t: {}".format(video.title))

			# tampilkan rating video
			print("Rating\t: {}".format(video.rating))

			# tampilkan author video
			print("Author\t: {}".format(video.author))

			# tampilkan panjang durasi video
			print("Length\t: {}".format(video.length))
			print()

			# mengunduh dengan menampilkan loading bar
			best_video = video.getbest()
			file_video = direktori+sanitize_file(video.title)+"."+best_video.extension
			
			filename = best_video.download(
				filepath=file_video,
				quiet=True, callback=loading_bar)
			
			# open direktori tempat menyimpan video hasil unduhan
			print("Unduhan Selesai")
			time.sleep(1)
			os.startfile(direktori)
		else:
			raise Exception("Program Terhenti")
	except Exception as e:
		print("\nTerjadi kesalahan saat mengunduh video, cek url video !")


def pytube_action():
	# input url
	url_youtube = gui.prompt("Masukan URL Youtube")

	# jika inputan url dicancel
	if not url_youtube:
		exit(0)

	direktori = select_directory()

	# jika ada, setuju mengunduh ?
	setuju = gui.confirm("Yakin ingin mengunduh ?")

	if setuju.upper() == "OK":
		# jika setuju
		if direktori:
			if not direktori.endswith("/") :
				direktori += "/"
			unduh_video(url_youtube, direktori)
			#print(direktori)
		else:
			print("Terjadi Kesalan pada direktori")
			exit(0)
	else:
		exit(0)


if __name__ == '__main__':
	try:
		pytube_action()
	except KeyboardInterrupt:
		print("\nProgram Terhenti")
