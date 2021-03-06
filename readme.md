# Beacons of Catan
WIP.
This is my 3d printed LED project for Settlers
view the complete log here: [Website log](https://at89.github.io/Beacons-of-Catan/index.html)

updated schematic of Hex Tile guts:
![tile schematic](assets/img/tile-layout.jpg)

## Design

- 3d Printing a Settlers of Catan board using Ultimaker 2+ Extended
- 3d Printed Chits (roll numbers) to have LED display, wire thise to the base of the tile
- 3d Printed player set for Settlements, Cities, Roads (using Warcraft/Starcraft set)
- LED lights at the bases of the Tiles, printed in clear filament
- 3x6mm diametric magnets in the Hex bases.
- Accelerometer digital dice
- Robber to de-activate the Digital Chit -> remove any LED lighting trigger
- Still use game paper cards, development cards
- Still would like users to pay attention, alike the real game, if the user does not pay attention and grab their own - resource, they don't get it (so no need to actively keep log)
- Fair rolls option

Every tile will have either a beacon transmitter or a beacon receiver, depending how I want to design it..
A phone app can send the beacon signals to each individual tile to trigger it to light up, after the `dice_roll()` function and `dice_roll_value` is returned. The `Tile_id` with ```chit_value === dice_roll_value``` will trigger the LEDs to light up for a short amount of time.


`dice_roll_value` will be evaluated in another object/table on the app or a Pi. It will then know which ID to send the LED function to the beacon major to true

### Schemas
Dice:
```
dice {
  dice_roll_value = array
}
```
Tiles:
```
tile {
  id: integer, unique
  LED: boolean
}
```
Example of a tile object:
```
Tile {
id: 14,
LED: false,
}
```

From a beacon perspective it will look like this:
```
Tile UUID: a7585613-22e5-4203-bdc9-f954e2504083
{
minor: 14,
major: false,
}
```

### Game setup:
User story is:
Game setup:
- User uses app, generates boards, user will organize the board accordingly
- Once board is set, need to assign every tile the correct number of Chits (store in `chit_value`) and will display on the MicroLED device. The board will have to match the generated map and this is based on Human not being an idiot.
- Players use regular rules to set up the Game (player 1 goes first and last, player 4 goes 4th and 5th etc)
- Game will have an object/hashes to coordinate each tile with a `chit_value`
- MicroLED module will have to light up according to the `chit_value`

-Submodule interpreter for generating the map and transmitting/receiving signal can either live as an apk on the phone or on a Pi. It would be cool to use rn-s.net to generate and broadcast a nearby URL the generated map setup

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

### Thingiverse file links

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


## Progress:
#### To Paint:
- Four (4) Fields (Grain Resource) Hexes.
- Four (4) Forest (Lumber Resource) Hexes.
- Three (3) Mountains (Ore Resource) Hexes.
#### To Prime
- One (1) Desert (No Resource) Hex.
-
### Printing queue:
- Three (3) Hills (Brick Resource) Hexes.

#### To Print:
- [] Four (4) Pasture (Wool Resource) Hexes.
- [] Nine (9) regular sea hexes
- [] # Harbor Sea hexes
- [] # 1 of each 2:1 port
- [] # 3:1 ports
