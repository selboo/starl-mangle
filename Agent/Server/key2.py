import rsa

pubkey, privkey = rsa.newkeys(512)
 
pub = pubkey.save_pkcs1()
pubfile = open('r_public.pem','w+')
pubfile.write(pub)
pubfile.close()

pri = privkey.save_pkcs1()
prifile = open('r_private.pem','w+')
prifile.write(pri)
prifile.close()

