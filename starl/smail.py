#!/usr/bin/env python
#_*_encoding:utf-8_*_
# encoding:utf-8
import os,sys,optparse
import email,smtplib,mimetypes
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import encoders
import email.mime.text
import email.mime.multipart

from starl.models import *

mail_int = Site.objects.get(id=1)

def mail_send(to_addr, subject_header, mail_msg, from_addr = mail_int.mail_user, from_user = mail_int.mail_user, from_user_pass = mail_int.mail_pass, attachment = 0, html_type = 0, mail_smtp = mail_int.mail_snmp):

	message 		= MIMEMultipart()
	message['To'] 		= to_addr
	message['From']		= from_addr
	message['Subject']	= subject_header

	if not html_type:
		if mail_msg:
			if os.path.isfile(mail_msg):
				txt = open(mail_msg, 'rb')
				message.attach(MIMEText(txt.read(), 'plain', 'utf-8'))
				txt.close()
			else:
				message.attach(MIMEText(mail_msg, 'plain', 'utf-8'))

	else:
		if mail_msg:
			if os.path.isfile(mail_msg):
				html = open(mail_msg, 'rb')
				message.attach(MIMEText(html.read(), 'html', 'utf-8'))
				html.close()
			else:
				message.attach(MIMEText(mail_msg, 'html', 'uft-8'))

	if attachment:
		ctype, encoding = mimetypes.guess_type(attachment)
#		print ctype, encoding
		maintype, subtype = ctype.split('/', 1)
#		print maintype, subtype
		fp = open(attachment, 'rb')
		msg = MIMEBase(maintype, subtype)
		msg.set_payload(fp.read())
		fp.close()
		encoders.encode_base64(msg)
		msg.add_header("Content-Disposition", "attachment", filename = attachment)
		message.attach(msg)

	s = smtplib.SMTP(mail_smtp, 25)
	s.login(from_user, from_user_pass)
	#s.set_debuglevel(1)
	s.sendmail(from_addr, to_addr, message.as_string())
	s.quit()

def usage():
	help_msg = '''
	--from		-f	mail from address.
	--user		-u	the user mail from.
	--password	-p	the user pass mail from.
	--to		-t	mail to address.
	--subject	-s	mail subject.
	--message	-m	mail message.
	--attach	-a	the attachment file.
	--smtp			the smtp server.
	--html			html mail type, default = disable.
	version	0.1		author dave.
	Example:
	'''
	#print help_msg
	#print "\t%s --smtp 'mail.cdcgames.net' -f 'pengtao.wang@cdcgames.net' -u 'username' -p 'userpass' -t 'bj_ywgroup@cdcgames.net' -s 'Are you free tonight' -m 'Are you free tonight?' -a 'file_name'"  %sys.argv[0]

def Test():
	Test = "mailsend.py  --smtp 'mail.starl.com.cn' -f 'guocan.xu@starl.com.cn' -u 'guocan.xu' -p 'Aa123456' -t 'xuguocan@gmail.com' -s 'zhuti' -m 'neirong'"
	
def main():
	opt = optparse.OptionParser()
	opt.add_option('--from_addr',	'-f', default = '')
	opt.add_option('--user',	'-u')
	opt.add_option('--password',	'-p')
	opt.add_option('--to_addr',	'-t')
	opt.add_option('--subject',	'-s')
	opt.add_option('--message',	'-m')
	opt.add_option('--attach',	'-a')
	opt.add_option('--html', default = 0)
	opt.add_option('--smtp', default = 'mail.cdcgames.net')
	opt.add_option('--port', default = '25')
	options, arguments = opt.parse_args()

	def debug_info():
		print 'From_addr:\t',	options.from_addr
		print 'From_user:\t',	options.user
		print 'From_pass:\t',	options.password
		print 'To_addr:\t',	options.to_addr
		print 'Mail_subject:\t',options.subject
		print 'Mail_message:\t',options.message
		print 'Attachment:\t',	options.attach
		print 'Html_message:\t',options.html
#	debug_info()

	if not (options.from_addr and options.to_addr and options.user and options.password and options.subject and options.message):
		#usage()
		Test()
		sys.exit(1)

	options.subject = options.subject.decode('UTF-8').encode('UTF-8')
	options.message = options.message.decode('UTF-8').encode('UTF-8')
	mail_send(options.from_addr, options.user, options.password, options.to_addr, options.subject, options.message, options.attach, options.html, options.smtp)

if __name__ == '__main__':
	main()
