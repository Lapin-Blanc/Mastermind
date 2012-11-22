# -*- coding: utf-8 -*-
#!/usr/bin/env python
import random
import cgi
import cgitb; cgitb.enable()
import game
import os
import pickle

ROOT_PATH  = os.path.dirname(__file__)
COLORS  = ["red", "green", "blue", "yellow", "black", "gray"]

def row_to_html(code_list):
    s = '<id class="row">\n'
    for c in code_list:
        s+= '<id class="c %s"></id>\n' % COLORS[c]
    s += '</id>\n'
    return s

with open(os.path.join(ROOT_PATH, "styles.css"), "r") as f:
    style = f.read()

form = cgi.FieldStorage()
game_number = form.getvalue("game_number", 0)
body = ""
result = ()
if game_number:
    with open(os.path.join(ROOT_PATH, "games", game_number+".pickle"), "r") as f:
        m = pickle.load(f)
    guess = [int(form.getvalue("g"+str(i+1))) for i in range(4)]
    result = m.guess(guess)
    
else:    
    m = game.MasterMind()
    game_number = m.id
if result==(4,0):
    body += "<h2> Victoire en %s coups </h2>" % len(m.tries)
    body += row_to_html(m.code)+"<br/>\n"
    body += "<hr />\n"

if m.over:
    action = '<h4><a href="/cgi-bin/MasterMind.py">Commencer une autre partie</a>'
else:
    action = '<input type="submit" value="valider" />'

for t in m.tries[::-1]:
    body += row_to_html(t) + "Plac&eacute;s: %s - Non plac&eacute;s: %s<br />\n" % m.check_guess(t)
 
with open(os.path.join(ROOT_PATH, "games", m.id+".pickle"), "w") as f:
    pickle.dump(m, f)

print """\
Content-Type: text/html\n"""
print """
<html>
    <head>
    <style type="text/css">
    %s
    </style>
    </head>
    <body onload="document.forms[0].elements[0].focus();">
    <h4>Master Mind</h4>
    <form method="post" enctype="multipart/form-data">
        <select name="g1">
            <option value="0">Rouge</option>
            <option value="1">Vert</option>
            <option value="2">Bleu</option>
            <option value="3">Jaune</option>
            <option value="4">Noir</option>
            <option value="5">Gris</option>
        </select>
        <select name="g2">
            <option value="0">Rouge</option>
            <option value="1">Vert</option>
            <option value="2">Bleu</option>
            <option value="3">Jaune</option>
            <option value="4">Noir</option>
            <option value="5">Gris</option>
        </select>
        <select name="g3">
            <option value="0">Rouge</option>
            <option value="1">Vert</option>
            <option value="2">Bleu</option>
            <option value="3">Jaune</option>
            <option value="4">Noir</option>
            <option value="5">Gris</option>
        </select>
        <select name="g4">
            <option value="0">Rouge</option>
            <option value="1">Vert</option>
            <option value="2">Bleu</option>
            <option value="3">Jaune</option>
            <option value="4">Noir</option>
            <option value="5">Gris</option>
        </select>
        %s
        <input type="hidden" name="game_number" value="%s" />
    </form>
    %s
    </body>
</html>
""" % (style, action, game_number, body)    
