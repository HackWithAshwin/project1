#import modules & all here
import telebot
import ast
import time
from telebot import types

#Bot login
bot = telebot.TeleBot("1321398275:AAGMIkUmr4a-2LoVyAYGtRn34269A4qbb4c")
A_USER = 989362465  #majordevil
B_USER = 618388309 #cybervenom
C_USER = 988768328 #anthonystark
D_USER = 907855151 #Tony Stark
E_USER = 748081205 #aksh
F_USER = 613176597 #spary
A_CHAT = '-1001327038682'

#start & help command reply (echo)
@bot.message_handler('start')
def send_welcome(message):
        bot.reply_to(message, "*Howdy, how are you doing? This is Official Bot of* @EscrowCrew *made by* @MajorDevil *to manage easy escrow's!* \n*Use* /getesc *to get free escrow service.* \n*NOTE : Don't use /getesc if you dont need escrow else it may lead to ban!*", parse_mode="Markdown")
       
@bot.message_handler('help')
def echo_all(message):
    bot.reply_to(message, "Nothing to see here? \nUse /getesc only if you need ESCROW SERVICE")
    
@bot.message_handler('donate')
def echo_all(message):
    bot.reply_to(message, "Gonna Soon be Available")
    

#@bot.message_handler('esc')
#def echo_all(message):
    #bot.send_message(ES_USER, "HELLO")

@bot.message_handler('getesc')     
def echo_message(message):
    cid = message.chat.id 
    message_text = message.text 
    user_id = message.from_user.id 
    user_name = message.from_user.first_name
    mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
    bot.reply_to(message, "*Your Request has been submitted to Admins of* @EscrowCrew!. *Soon you will get an escrow. Thanks*", parse_mode="Markdown")
    bot.send_message(cid, "*To get Escrow Faster or To Prevent Get Ignored Send Me the Following Details with* /getescrowfast.\n*For example* : \n\n`/getescrowfast \nBuyers Username : \nSellers Username : \nAmount : \nPayment Mode :` ", parse_mode="Markdown")
    bot.send_message(A_USER, "*Hello Dear* @EscrowCrew's! *Admin. This message is to inform you that* "+ mention +" * has requested for escrow. So if you have read this message then go and accept the escrow without wasting time Gendu*", parse_mode="Markdown")
    bot.send_message(B_USER, "*Hello Dear* @EscrowCrew's! *Admin. This message is to inform you that* "+ mention +" * has requested for escrow. So if you have read this message then go and accept the escrow without wasting time Gendu*", parse_mode="Markdown")
    bot.send_message(C_USER, "*Hello Dear* @EscrowCrew's! *Admin. This message is to inform you that* "+ mention +" * has requested for escrow. So if you have read this message then go and accept the escrow without wasting time Gendu*", parse_mode="Markdown")
    bot.send_message(D_USER, "*Hello Dear* @EscrowCrew's! *Admin. This message is to inform you that* "+ mention +" * has requested for escrow. So if you have read this message then go and accept the escrow without wasting time Gendu*", parse_mode="Markdown")
    #bot.send_message(E_USER, "*Hello Dear* @EscrowCrew's! *Admin. This message is to inform you that* "+ mention +" * has requested for escrow. So if you have read this message then go and accept the escrow without wasting time Gendu*", parse_mode="Markdown")
    #bot.send_message(F_USER, "*Hello Dear* @EscrowCrew's! *Admin. This message is to inform you that* "+ mention +" * has requested for escrow. So if you have read this message then go and accept the escrow without wasting time Gendu*", parse_mode="Markdown")
    bot.send_message(A_CHAT, "*Hello Dear* @EscrowCrew's! *Admin. This message is to inform you that* "+ mention +" * has requested for escrow. So if you have read this message then go and accept the escrow without wasting time Gendu*", parse_mode="Markdown")
    
@bot.message_handler('getescrowfast')
def echo_all(message):
    cid = message.chat.id 
    message_text = message.text 
    user_id = message.from_user.id 
    user_name = message.from_user.first_name
    mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
    bot.forward_message(A_USER, cid, message.message_id)
    bot.forward_message(B_USER, cid, message.message_id)
    bot.forward_message(C_USER, cid, message.message_id)
    bot.forward_message(D_USER, cid, message.message_id)
    #bot.forward_message(E_USER, cid, message.message_id)
    #bot.forward_message(F_USER, cid, message.message_id)
    bot.forward_message(A_CHAT, cid, message.message_id)
    bot.send_message(cid, "*Thankyou* "+ mention +" *For Submting Details. Please Wait For The Escrow Admin To Come Online*", parse_mode="Markdown")
    
while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=0)
    except:
        time.sleep(10)