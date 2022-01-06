# spaceaholic
Prototype
Het prototype is gemaakt in visual studio community, een tool waarmee je met gemak applicaties kan maken door onderdelen van de applicatie op je beeldscherm te swipen.
We hebben de functionaliteiten van de app hierin geprogrammeerd, wat slechts basis programmeerervaring vereiste.
We gebruiken een timer, een object wat bijhoud hoeveel tijd er is vertreken, om van het beginscherm naar ons hoofdscherm te gaan,
vervolgens gebruiken we 7 knoppen en een 'terug' knop om van dit hoofdscherm naar schermen voor individuele parken te navigeren.
De knoppen laden allemaal hun eigen parkoverzicht en druktegrafiek in. 
De emulatie is geschreven in de programmeertaal C# en is dus object georienteerd, de code bevat 168 regels.

Data
De data hebben we met behulp van programmeertaal python gescraped vanuit verschillende api's, 
dit zorgt er voor dat het niet alleen makkelijk is om snel aan data te komen, maar dat het ook makkelijk is om ons prototype uit te breiden met bijna alle parken in de wereld. 
Dit omdat de api's die we gebruiken veel verder gaan dan de huidige 7 parken. 
Iets wat verzekerd dat ons project en idee makkelijk scalable is en indien nodig op grotere schaal toe te passen is, ook
geeft het ons de beschikking over extreem veel data voor verdere uitbreidingen in de nabije toekomst.

Api's
De api's die we gebruiken zijn api.openrouteservice.org, om het mogelijk te maken makkelijk tussen parken te navigeren en hier instructies over op te halen.
We gebruiken api besttime.app/api om drukte op te halen voor de verschillende parken. 
We gebruiken de amadeus api om veiligheid op te halen, 
we doen dit door de parken automatisch om te zetten naar een set coordinaten, waarop amadeus weer veiligheidsscores kan geven.
