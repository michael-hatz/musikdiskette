# Musikdiskette - Hör doch mal eine Diskette!
![Musikdiskette](https://schmalenstroer.net/blog/wp-content/uploads/2024/10/musikdiskette-1024x275.png)

[![Watch the video](https://www.schmalenstroer.net/musikdiskette.png)](https://www.youtube.com/watch?v=GC8M22ON5ec)

![Musikdiskette](https://schmalenstroer.net/blog/wp-content/uploads/2024/10/PXL_20241010_183401014-989x1024.jpg)


Musikdiskette ist ein Abspielgerät für Musik via Kassetten.

### Warum? 
* Endlich wieder in Diskettenstapeln und -boxen wühlen!
* Hervorragende Diskettengeräusche!
* Keine App, kein Abo, einfach nur Musik!
* Mach dich unabhängig davon, ob deine Lieblingsmusik auf Vinyl releast wurde!

## Überlegungen:
* Es macht Spaß, in Musikstapeln zu wühlen
* Es macht Spaß, analoge Medien zu benutzen
* Analoge Medien haben eine völlig andere Haptik als digitales Streaming
* Ja, ich weiß, dass Disketten digitale Medien sind
* Musik-CDs sind irgendwie unbefriedigend im Handling
* Gebrannte CDs erst recht
* Es gibt aber nicht alle Musik auf Vinyl oder nur sehr teuer

## Benötigte Hardware:
* Raspberry Pi oder vergleichbares System
* ein externes USB-Diskettenlaufwerk
* Ein Stapel Disketten
* Farbdrucker
* Disketten-Etiketten
* 3D-Drucker

## Anleitung:
* Richte Raspberry Pi wie üblich ein
* Achte drauf, dass VLC installiert ist
* Stecke USB-Diskettenlaufwerk ein
* Speichere MP3s irgendwo auf deinem Raspi
* Erstelle auf der Diskette eine "playlist.m3u8" mit der gewünschten Musik
* Achte darauf, dass die Playlist absolute Pfade nutzt
* Installiere alle nötigen Python-Importe
* Starte die musicdiskette.py und schau, ob alles funktioniert
* Richte in der rc.local ein, dass das Skript beim Booten automatisch startet
* Öffne die InDesign-Vorlage und erstelle dir Diskettencover passend zu deiner Musik
* 3D-Drucke Ständer
* 3D-Drucke Button
* Fertig

## Aktueller Status: 
* Es funktioniert ohne mir bekannte größere Bugs
* Der Python-Code ist messy und sollte dringend aufgeräumt werden. Da er aber funktioniert und eh keiner das hier nachbauen wird, ist es mir eine Freude, dass irgendwelche shady Firmen damit ungefragt ihre AIs trainieren werden
* Der Code funktioniert mit einem ganz bestimmten USB-Diskettenlaufwerk von AliExpress. Schaut man sich das Angebot an, gibt es gar nicht so viele Anbieter, aber da diese anscheinend alte Laptoplaufwerke in neue Gehäuse bauen, können sich andere Geräte anders verhalten. Hier empfehle ich einen Blick in die verlinkten Blogposts
* Der Diskettenlaufwerkständer könnte eine zweite Version vertragen, aber funktioniert aktuell in meinem Setup
* Dank Raspi-Basis sollten Dinge wie Bluetooth-Kopfhörer, Streaming auf Lautsprecher, Last.fm-Scrobbling etc. funktionieren, wenn sie unter Raspbian funktionieren


## Buildlog:
* https://schmalenstroer.net/blog/2024/09/bastelstunde-1/
* https://schmalenstroer.net/blog/2024/09/bastelstunde-2/
* https://schmalenstroer.net/blog/2024/09/bastelstunde-3/
* https://schmalenstroer.net/blog/2024/09/bastelstunde-4/
* https://schmalenstroer.net/blog/2024/10/bastelstunde-5/
* https://schmalenstroer.net/blog/2024/10/bastelstunde-6/

## Mögliche Verbesserungen:
* Verbesserter Ständer
* (Pause/Skip)
