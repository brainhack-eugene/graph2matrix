# graph2matrix

**Summary:** Graphical interface to build a finite state machine and create its matrix representation

This project was launched at 
[Eugene Brainhack 2017](https://brainhack-eugene.github.io/).

The manual process of creating a state transition matrix, the structure that
controls progress through an experimental trial, is highly susceptible to 
to error.  The objective of this project is to standardize and automate the 
creation of state transition matrices.

The project was inspired by a need in the TASKontrol project 
([TASKontrol (source)](https://github.com/sjara/taskontrol), 
[TASKontrol (documentation)](https://taskontrol.readthedocs.io)) from
the [jaralab](http://jaralab.uoregon.edu/) at the [University of Oregon](uoregon.edu), 
but was implemented as a stand alone module that could generalize to 
other tasks creating and editing a finite state machine and state transition 
matrix.

## Organization
This project roughly follows a model-view-controller organization.  The model
provides a digital representation of a finite state machine.  
Multiple views render the values within the model with varying levels of 
interactivity: graphical display, matrix, automated code generation.  
The controller provides the logic that accepts input from the designer as 
they build the finite state machine and pushes updates to or between the views.

## Input
The prototype implementation accepts interactive input from the user through
keystrokes and mouse clicks in the graphical view.  
(Future features could include the ability to read in a state transition matrix
for display, editing, and automated code generation).

## Output
The primary output is a two dimensional array that represents the state
transition matrix.

## Dependencies

- [NetworkX](https://networkx.github.io/), under the BSD license