# BOARDEDITOR
> Tool For Assisting The Creation of Boards for a game I am working on with a group

#
### Description

Codname Boardeditor is an application programmed in python using the pygame library that either reads/edits a map from an adjacency list that is stored from in a json file or can create a new json file to read/edit boards.

The original purpose of this application is to create board prototypes for future use in the upcoming game Project Orpheus and to display useful information of maps like most frequent spots of a map assuming a person can move an arbitrary amounts of steps each turn.

#
### How To SetUp

1. Download Boardeditor.app folder for mac or Boardeditor.exe folder for windows (*linux support will be added later*)
2. Open Application to create a blank map of size (*currently preset*) named *prototype.json* or drag a json file to the application to continue editing a previously made map.

#
### Current Functions

- Left-Click Empty Space -> Add Space
- Left-Click Space -> Highlight Space
- Left-Click Highlighted Space -> remove highlight
- Left-Click Another Space (with one already highlighted) -> Add Edge
- Right-Click -> Delete Space (and edges connected to Space)
- Left-Click Key Item -> Becomes New Space To be Added
- ArrowKey on Highlighted Space -> offsets the space in that direction
- ***[MORE TO COME]***

#
### Objective List
> ~~completed~~ / TODO

+ ~~Read json files~~
+ ~~Draw board spaces~~
+ ~~Draw board edges~~
+ Draw directional edges
+ ~~Add key of spaces~~
+ ~~Create OS Boardeditor.app~~
+ ~~Create Windows Boardeditor.exe~~
+ Create Special Spaces
+ ~~Add offset to space location for more unique boards~~
+ ~~Add delete space with right click function~~
+ ~~Add delete edge function~~
+ ~~Add function to clean json code (remove missing indexes)~~
+ Add Frequency MetaData
+ Come Up With More Objectives
