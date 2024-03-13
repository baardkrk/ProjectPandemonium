# Pollenvarsel for magic mirror

Denne modulen er laget for å hente data fra [naaf's
pollenvarsling]("https://www.naaf.no/pollenvarsel/") for å vise dette i et
informasjonsvindu i magic mirror prosjektet.

NB! Modulen er avhengig av formateringen på scriptet som blir hentet fra naaf, og vil
derfor ikke virke dersom dette endres. Noen antakelser er gjort ang. hvilke navn som blir
gitt på de øvrige allergiene bortsett fra Or og Hassel, da disse ikke er gitt i scriptet
som blir lastet ned nå. (14.03.2019)


TODOs:
 - [ ] Refaktorere til oop
 - [ ] Integrere til MM
 - [ ] Måte å velge område (automatisk basert på IP?)
