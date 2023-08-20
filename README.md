# python-crypto-simple-substitution-solver
Mono alphabetic substitution cipher

# Overview
Some random concept/collection of tools to help solve cryptograms.

# PreReqs
`pip install cipher_solver`

# Usages
`./m-sub-solver.py sub ciphertext.txt abcdefghijklmnopqrstuvwxyz wvutsrzponmlkqihgfedcbaxyj`


```
➜  python-crypto-simple-substitution-solver git:(main) ✗ ./simple-subsolver.py ciphertext.txt hear
['ciphertext.txt', 'hear']
what_to_look_for=['hear']
ciphertext='HFOBWDS wtbsfdoesksjd ji ijs mjiae (dai ditwy). Afods ks rofed\ndpficqp licqp. Toeqfwus yic lsrd vspojt uwjjid qsd ibsf. Aoll\nsjtswbicf di edwy apsfs yic lsrd ce doll O pswf rfik yic, qobs\nyicf wtbous. Yicf cjpwhhy aors jid asll.\n'
s.plaintext()='GROLATE aclertomedest si ise ysiwm (twi ticab). Wrote de normt\nthriuph fiuph. Comprave biu fent kehosc vassit pet iler. Woff\nescealiur ti mtab where biu fent um toff O hear nrid biu, pole\nbiur aclove. Biur ushaggb wone sit weff.\n'
s.decryption_key()='wytkslhpinvberoqxfjdcuagmz'
d.plaintext()='YRILATE anlertisefect co oce kcoms (tmo tonaw). Mrite fe dirst\nthrough vough. Nisgrape wou vedt behicn paccot get oler. Mivv\necnealour to staw mhere wou vedt us tivv I hear drof wou, gile\nwour anlipe. Wour uchayyw mide cot mevv.\n'
d.decryption_key()='wvjrskqponmbatiuxfedclyghz'
s.plaintext()='GRILATE adlertisevent no one knows (two today). Write ve cirst\nthrouph fouph. Disprame you fect behind mannot pet oler. Wiff\nendealour to stay where you fect us tiff I hear crov you, pile\nyour adlime. Your unhaggy wice not weff.\n'
...
```

```
➜  python-crypto-simple-substitution-solver git:(main) ✗ ./solve-cipher.sh hear

Ciphertext:
HFOBWDS wtbsfdoesksjd ji ijs mjiae (dai ditwy). Afods ks rofed
dpficqp licqp. Toeqfwus yic lsrd vspojt uwjjid qsd ibsf. Aoll
sjtswbicf di edwy apsfs yic lsrd ce doll O pswf rfik yic, qobs
yicf wtbous. Yicf cjpwhhy aors jid asll.

Plaintext:
PRIMATE almertinevest so ose wsofn (tfo tolay). Frite ve dirnt
through cough. Lingrabe you cedt kehisl bassot get omer. Ficc
esleamour to ntay fhere you cedt un ticc I hear drov you, gime
your almibe. Your ushappy fide sot fecc.
```
