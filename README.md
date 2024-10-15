# Tic-Tac-Toe Game

## Beskrivning
Detta är ett grafiskt användargränssnitt (GUI) för spelet Tic-Tac-Toe, utvecklat med Python och `tkinter`. Två spelare turas om att spela och försöker få tre av sina symboler i rad (horisontellt, vertikalt eller diagonalt) för att vinna spelet.

## Krav
För att kunna köra detta projekt behöver du:
- Python 3 installerat
- `tkinter` (ingår vanligtvis med Python-installationen)
- Mappen `utils` som innehåller filen `game.py` som implementerar Tic-Tac-Toe-logiken

## Installation
1. Klona eller ladda ner detta projekt till din dator.
2. Se till att du har `utils/game.py` med klassen `TicTacToe` som innehåller spelreglerna och logiken.

## Användning
För att köra spelet, öppna en terminal och navigera till mappen där `main.py` finns. Kör följande kommando:

```sh
python main.py
```

Ett fönster öppnas där två spelare kan spela Tic-Tac-Toe mot varandra.

## Spelregler
- Spelare `X` och spelare `O` turas om att göra sina drag.
- För att göra ett drag, klicka på en av rutorna i 3x3-spelbrädet.
- Spelet slutar när någon spelare får tre i rad, eller när alla rutor är fyllda utan att någon har vunnit (oavgjort).

## Återställning
När spelet är slut (antingen genom vinst eller oavgjort) visas ett meddelande och spelet återställs automatiskt så att en ny match kan börja.