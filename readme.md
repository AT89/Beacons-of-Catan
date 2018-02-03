# Beacons of Catan
WIP.
This is my 3d printed LED project for Settlers
## Design

-3d Printing a Settlers of Catan board using Ultimaker 2+ Extended
-3d Printed Chits (roll numbers) to have LED display, wire thise to the base of the tile
-3d Printed player set for Settlements, Cities, Roads (using Warcraft/Starcraft set)
-LED lights at the bases of the Tiles, printed in clear filament
-3x6mm diametric magnets in the Hex bases.
-Accelerometer digital dice
-Robber to de-activate the Digital Chit -> remove any LED lighting trigger
-Still use game paper cards, development cards
-Still would like users to pay attention, alike the real game, if the user does not pay attention and grab their own -resource, they don't get it (so no need to actively keep log)


Every tile will have either a beacon transmitter or a beacon receiver, depending how I want to design it..
A phone app can send the beacon signals to each individual tile to trigger it to light up, after the `dice_roll()` function and `dice_roll_value` is returned. The `Tile_id` with ```chit_value === dice_roll_value``` will trigger the LEDs to light up for a short amount of time.

Schema for tile would be:
```
dice {
  dice_roll_value = array
}
```
tile {
  id: integer,
  chit_value: integer
}
```
Example of a tile object:
```
Tile {
id: 14,
chit_value: 8,
}
```

From a beacon perspective it will look like this:

Tile UUID: a7585613-22e5-4203-bdc9-f954e2504083
{
minor: 14,
major: 8
}
```

### Game setup:
User story is:
Game setup:
1. - User uses app, generates boards, user will organize the board accordingly
2. - Once board is set, need to assign every tile the correct number of Chits (store in `chit_value`)
3. - Players use regular rules to set up the Game (player 1 goes first and last, player 4 goes 4th and 5th etc)
4. - Game will have an object/hashes to coordinate each tile with a `chit_value`

5. Once the board is arranged as per Tile ID,

Game starts:
1. Player shakes the dice, activates the Accelerometers,
2. Accelerometer `stops` after it has been `shaken` calls a `dice_roll()`
3. A `dice_roll()` will generate dice1 = rand(1..6) twice and add the sum to push a value for array `diceRoll`
4. Iterate through all tiles (or call the tiles directly from ID when matches)
  ```
    if (diceRoll[i] === chit_value) {
      LED on for tile.id
    }
  ```

### Components

-Individual Tiles of the Settlers game
-BLE Beacons in every land Tile
-Accelerometers in black dice
-Deactivator mechanism for the Robber

### Planning

Game: https://www.thingiverse.com/thing:2525047
Case :  https://www.thingiverse.com/make:349648
Number tiles: https://www.thingiverse.com/thing:112018

### Game Pieces:
Chinese: https://www.thingiverse.com/thing:1071048
Medieval: https://www.thingiverse.com/thing:1076785
Future: https://www.thingiverse.com/thing:2121534
WARCRAFT/STARCRAFT: https://www.thingiverse.com/thing:649313

Dice: just need to print some cubes and place an accelerometer and a lithium ion battery
(or have it chargable by USB-C). `USB-C Master Race`

References:
Gamepieces count: https://boardgamegeek.com/thread/324667/counts-components-settlers-catan-4th-edition

Use Radbeacons as game 1-12 chips
Microbit LED for the Chit or Resource Number display
Use a Catan-randomizer to order the map accordingly

Filament: Argos 2.75mm or 3mm pla

### Progress:
PAINTING - Four (4) Fields (Grain Resource) Hexes.
PAINTING - Four (4) Forest (Lumber Resource) Hexes.

PRINTED - Three (3) Mountains (Ore Resource) Hexes.

PRINTING - Three (3) Hills (Brick Resource) Hexes.

TODO:
- [] Four (4) Pasture (Wool Resource) Hexes.
- [] Nine (9) regular sea hexes
- [] # Harbor Sea hexes
- [] # 1 of each 2:1 port
- [] # 3:1 ports

- [x] - One (1) Desert (No Resource) Hex.
