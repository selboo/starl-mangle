#!/usr/bin/env python
#coding=utf-8
import logging
import os.path
import re
import sys
import telnetlib
from compiler.ast import Print
from types import BooleanType
import os,time,paramiko,optparse

debugging = 0

log = logging.getLogger()
#hdlr = logging.StreamHandler( sys.stdout )
#formatter = log.Formatter( '%(asctime)s %(levelname)s %(message)s' )
#hdlr.setFormatter( formatter )
#log.addHandler( hdlr )

hdlr = logging.StreamHandler( sys.stdout )
formatter = logging.Formatter( '%(asctime)s %(levelname)s %(message)s', '%T' )
hdlr.setFormatter( formatter )
log.addHandler( hdlr )


swcorehost = "192.168.192.1"
morestr = "--More--"
morestr_asa = "<--- More --->"
endstr = ">"
#change_switchip = raw_input( "please enter switchip (192.168.192.1-6): " )
#change_port = raw_input( "please enter port (0/1-24) : " )
#change_vlan = raw_input( "please enter vlan (3,4,100,50,60,250,): " )

'''初始化telnet信息'''
ciscoSpstr = '\x08\x08\x08\x08\x08\x08\x08\x08\x08        \x08\x08\x08\x08\x08\x08\x08\x08\x08'


_mac_address_re = re.compile( "([0-9A-Fa-f]{4}.[0-9A-Fa-f]{4}.[0-9A-Fa-f]{4})" )
_vlan_num_re = re.compile( "Vlan\d{1,3}" )
#_faEth_re = re.compile( '(FastEthernet\d*/\d*[/\d*]{0,2})' )
_faEth_re = re.compile( 'FastEthernet\d*/\d*[/\d*]{0,}' )
_interface_re = re.compile( '(Fa\d*/\d*[/\d*]{0,})' )


#_vlan_faEth_re = re.compile ( '(Vlan\d{1,3})|(FastEthernet\d*/\d*[/\d*]{0,2})' )
_vlan_faEth_re = re.compile ( 'Vlan\d{1,3}|FastEthernet\d*/\d*[/\d*]{0,}' )
_ip_mac_address_reall = re.compile( "(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})[\d\D]*([0-9A-Fa-f]{4}.[0-9A-Fa-f]{4}.[0-9A-Fa-f]{4})" )
_ip_mac_address_re = re.compile( "(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})[\d\D]*([0-9A-Fa-f]{4}.[0-9A-Fa-f]{4}.[0-9A-Fa-f]{4})" )
_ip_address_re = re.compile( "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" )
#_ip_address_re = re.compile( "\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}" )
#_ip_address_re = re.compile( "(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})" )
#_ip_address_reall = re.compile( "(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})" )
_cdp_ne_re = re.compile( "([A-Za-z]+?[0-9]{0,})[' Fas ']+?(\d*/\d*[/\d*]{0,})" )

_mac_address_table_re = re.compile( "([0-9]+?)[' ']+?([0-9A-Fa-f]{4}.[0-9A-Fa-f]{4}.[0-9A-Fa-f]{4})[\d\D]+?(Fa\d*/\d*[/\d*]{0,})" )
_cdpEntry_IP_re = re.compile( "IP address:[\d\D]+?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" )

def telnetReplaceStr ( stringSrc, strRps ):
    strNew = stringSrc.replace( strRps, '' )
    return strNew

class telnetXKCS:
    '''
    xkcs telnet class
    '''


    def __init__( self , host , userid , passwd ,  port , enpasswd , debug = debugging):
        '''
        init telnet
        '''
        self.host     = host
        self.userid   = userid
        self.passwd   = passwd
        self.port     = port
        self.enpasswd = enpasswd

        self.tn = telnetlib.Telnet()
        self.tn.set_debuglevel( debug )
        self.endstr = '>'
#        self.proxy_status = False
#        self.telnetInit()

    def telnetInit( self ):
        #print "telnet %s  " % ( host )
        self.tn.open( self.host, self.port )
        self.telnetCoreConnect()

    def telnet_switch_init( self ):
        #print "telnet %s  " % ( host )
        self.tn.open( self.host, self.port )
        self.telnetCoreConnect()
        """
        print host
        print userid
        print passwd
        print port
        """
    def telnet_switch_connect( self ):

        #tn.open( change_switchip, telnet_port )
        log.info( "telnet Core Connect starting->username" )
        self.tn.read_until( "Username:" )
        self.tn.write( self.userid + "\n" )
        log.info( "telnet Core Connect starting->username" )
        self.tn.read_until( "Password:" )
        self.tn.write( self.passwd + "\n" )
        
        self.tn.read_until( ">" )

        log.info( "telnet Core Connect done" )

    def telnetProxyConnect( self ):
        #print "proxy telnet:%s" % ( host )
        self.proxy_status = True
        self.tn.write( 'telnet %s \n' % ( self.host ) )
        self.telnetCoreConnect()

    def telnetCoreConnect( self ):

        #tn.open( change_switchip, telnet_port )
        log.info( "telnet Core Connect starting->username" )
        self.tn.read_until( "Username:" )
        self.tn.write( self.userid + "\n" )
        log.info( "telnet Core Connect starting->username" )
        self.tn.read_until( "Password:" )
        self.tn.write( self.passwd + "\n" )

        self.tn.read_until( ">" )

#        return tn
        log.info( "telnet Core Connect done" )

    def telnetCiscoenable( self ):

        self.endstr = '#'
        self.tn.write( "en\n" )
        '''特权密码'''
        self.tn.read_until( "Password:" )
        self.tn.write( self.enpasswd + "\n" )
        self.tn.read_until( '#' )
        log.info( "telnet Cisco Enable Mode done" )

    def telnetcmdmor( self, cmd, Save_Name = None ):
        if Save_Name == None:
            self.tn.write( cmd + '\n' )
        else:
            self.tn.write( cmd + '\n' + Save_Name + '\n' )
            self.tn.read_until( "[confirm]" )
            self.tn.write( "\n" )
            
        log.debug( "start more" )
        message = ''
        message_list = ''
        while 1:
            message = self.tn.expect( [morestr, self.endstr], 5 )
#            print "mes:", message
    #        print "me2", message[2]
            message_list += telnetReplaceStr( telnetReplaceStr( message[2], ciscoSpstr ), morestr )
            if str( message[2] ).find( self.endstr ) >= 0:
#                print "message find  # ,break"
                break
            elif str( message[2] ).find( morestr ) >= 0:
#                print "more..."
                self.tn.write( ' ' )
            elif str( message[2] ).find( morestr_asa ) >= 0:
                self.tn.write( ' ' )
        log.debug( "END message:%s" % ( message_list ) )
        return message_list

    def telnetFinal( self ):
#        if self.proxy_status:
#            self.telnetcmdmor( 'exit \n' )
        self.telnetcmdmor( 'exit \n' )
        self.tn.close()

def reSearchIPandMac( re_rule, linestr ):
    match = re_rule.findall( linestr )
    if match:
        return match[0]


def interfaceport ( arpstr ):
    ipDic = []
    for line in arpstr:
        if len( line ) < 5:
            continue
        elif line.find ( 'Protocol' ) >= 0:
            continue
        elif line.find ( endstr ) >= 0:
            continue
        else:
            interface = reSearchIPandMac( _interface_re, line )
    return interface

def switchip ( arpstr ):
    ipDic = []
    for line in arpstr:
        if len( line ) < 5:
            continue
        elif line.find ( 'Protocol' ) >= 0:
            continue
        elif line.find ( endstr ) >= 0:
            continue
        else:
            switchip = reSearchIPandMac( _cdpEntry_IP_re, line )
    if switchip == None:
        switchip = swcorehost
    return switchip


def switchinfo (interface, switchinfo):
    switchname = "core"
    for switcher, faport in switchinfo:
        if "Fa"+faport == interface:
            switchname = switcher
        else:
            continue
    return switchname

def usage():
    help_msg = '''
    --ip                   check ip  address
    --arpbind              Arp Bind
    --postbind             Cisco Ethernet Bind
    --lanid                Exchang Vlanid
    --save                 Save Switch Config
    
    --debug                debug info
    Exmaple:
    '''
    print help_msg
    print "\t%s --ip 192.168.80.100 --arpbind --postbind --vlanid 100" %sys.argv[0] 
    
def arpIpMAc( arpstr ):
    for line in arpstr:
        if len( line ) < 5:
            continue
        elif line.find ( 'Protocol' ) >= 0:
            continue
        elif line.find ( endstr ) >= 0:
            continue
        else:
            ipaddress = reSearchIPandMac( _ip_address_re, line )
            macaddress = reSearchIPandMac( _mac_address_re, line )
            vlanFaEth = reSearchIPandMac( _vlan_faEth_re, line )
    return ipaddress,macaddress,vlanFaEth

def Post_Security (macaddress, switchipadd, switchinterface):
    
    swcore.telnet_switch_init(switchipadd)
    swcore.telnetCiscoenable()
    swcore.telnetcmdmor('configure terminal')
    swcore.telnetcmdmor('interface %s' % switchinterface)
    
    swcore.telnetcmdmor('no switchport port-security violation shutdown')
    swcore.telnetcmdmor('no switchport port-security maximum 1')
    swcore.telnetcmdmor('no switchport port-security mac-address')
    swcore.telnetcmdmor('no switchport port-security')
    
    swcore.telnetcmdmor('switchport port-security')
    swcore.telnetcmdmor('switchport port-security mac-address %s' % macaddress)
    swcore.telnetcmdmor('switchport port-security maximum 1')
    swcore.telnetcmdmor('switchport port-security violation shutdown')
    
    swcore.telnetcmdmor('exit')
    swcore.telnetcmdmor('exit')
    
    Status = swcore.telnetcmdmor('show running-config interface %s' % switchinterface)
    head = '|===================Post Bind Info===================|\n'
    tail = '|====================================================|'
    message = head + Status + "\n" + tail
    return message

def Arp_Bind (ip, mac):
    
    swcore.telnet_switch_init(swcorehost)
    swcore.telnetCiscoenable()
    
    ipaddress_numb = swcore.telnetcmdmor('show arp | in %s' % mac)
    ipaddress_list = _ip_address_re.findall(ipaddress_numb)
    swcore.telnetcmdmor('configure terminal')
    for iplist in ipaddress_list:
        swcore.telnetcmdmor('no arp %s' % iplist)

    Status = swcore.telnetcmdmor('arp %s %s ARPA' %(ip, mac))
    head = '|===================Arp Bind Info=======================|\n'
    tail = '|=======================================================|'
    message = head + "core(config)#" + Status + "\n" + tail
    return message

def Exchange_Vlan (vlanid, switchipadd, switchinterface):
    
    switchinterface = "Fa0/9"
    swcore.telnet_switch_init(switchipadd)
    swcore.telnetCiscoenable()
    swcore.telnetcmdmor('configure terminal')
    swcore.telnetcmdmor('interface %s' % switchinterface)
    swcore.telnetcmdmor('switchport access vlan %s' % vlanid)

    swcore.telnetcmdmor('exit')
    swcore.telnetcmdmor('exit')

    Status = swcore.telnetcmdmor('show running-config interface %s' % switchinterface)
    head = '|===================Exchang VLan Info===================|\n'
    tail = '|=======================================================|'
    message = head + Status + "\n" + tail
    return message

def Save_Switch (switchipadd):
    
    Save_Date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    
    swcore.telnet_switch_init(switchipadd)
    swcore.telnetCiscoenable()
    
    swcore.telnetcmdmor('copy running-config flash:', Save_Date + '-running-config')
    Status = swcore.telnetcmdmor('write ')
    head = '|===================Save Switch Config===================|\n'
    tail = '|=======================================================|'
    message = head + Status + "\n" + tail
    return message

def get_info (ip):
    
    ipinfo = swcore.telnetcmdmor('show arp | in %s ' % ip)
    ipaddress,macaddress,vlanFaEth = arpIpMAc( ipinfo.split( '\r\n' ) )
    
    if ( str(macaddress) != 'None' ):
        ipinfo_1 = swcore.telnetcmdmor('show mac address-table | in %s ' % macaddress)
        interface = interfaceport( ipinfo_1.split( '\r\n' ) )
    else:
        interface = 'None'
        
    if ( str(interface) != 'None' ):
        ipinfo_2 = swcore.telnetcmdmor('show cdp neighbors')
        switchcdp = _cdp_ne_re.findall(ipinfo_2)
        switchname = switchinfo(interface,switchcdp)
    else:
        switchname = 'None'
    
    if ( str(switchname) != 'None'):
        ipinfo_3 = swcore.telnetcmdmor('show cdp entry %s ' % switchname)
        switchipadd = switchip( ipinfo_3.split( '\r\n' ) )
    else:
        switchipadd = 'None'
    
    if ( str(switchipadd) != 'None'):
        if switchipadd == swcorehost:
            ipinfo_4 = swcore.telnetcmdmor( 'sh mac address-table | in %s ' % ( macaddress ) )
        else:
            swcore.telnetProxyConnect( switchipadd )
            ipinfo_4 = swcore.telnetcmdmor( 'sh mac address-table | in %s ' % ( macaddress ) )
            
        switchinfoto = _mac_address_table_re.findall( ipinfo_4 )
        vlanid,mac,switchinterface = switchinfoto[0]
    else:
        vlanid = 'None'
        switchinterface = 'None'
        
    return ip,macaddress,vlanid,switchname,switchipadd,switchinterface

if __name__ == '__main__':

    opt = optparse.OptionParser()
    opt.add_option('--ip')
    opt.add_option("--arpbind", action="store_true", dest="arpbind", default=False)
    opt.add_option('--postbind', action="store_true", dest="postbind", default=False)
    opt.add_option('--vlanid')
    opt.add_option('--debug', default = 'info')
    opt.add_option('--save', action="store_true", dest="save", default=False)
    options, arguments = opt.parse_args()
    
    if not (options.ip):
        usage()
        sys.exit(1)
        
    swcore = telnetXKCS()
    swcore.telnetInit()

    ip,macaddress,vlanid,switchname,switchipadd,switchinterface = get_info (options.ip)
    
    def debug_info():
        print '|-------------------Debug Info------------------|'
        print '| IP Address:\t\t %s\t\t|'      % ip
        print '| MAC Address:\t\t %s\t\t|'     % macaddress
        print '| VLAN Number:\t\t %s\t\t\t|'   % vlanid
        print '| Swith Name:\t\t %s\t\t|'      % switchname
        print '| Swith IP:\t\t %s\t\t|'        % switchipadd
        print '| Swith Ethernet:\t %s\t\t\t|'  % switchinterface
        print '|-----------------------------------------------|'
    debug_info()

    if options.arpbind == True:
        print Arp_Bind(ip, macaddress)
        
    if options.postbind == True:
        print Post_Security(macaddress, switchipadd, switchinterface)

    if options.vlanid != None:
        print Exchange_Vlan(options.vlanid, switchipadd, switchinterface)

    if options.save == True:
        print Save_Switch(switchipadd)

    
    
