In this exercise, you will create a function that controls the movement of a character in a gaming world.

Assume that the gaming world is two-dimensional, rectangular (with square being a special rectangle), and every possible place in the world has exact coordinates. Each coordinate can be either 'free' (e.g., grass land) or 'blocked' (e.g., a rock). The player can freely move around in this world, but cannot leave the world and can only walk on 'free' fields.

Consider the following example of a game world:

     --------
    |#####   |    
    |###    #|
    |#   o ##|
    |   #####|
     --------

The example shows a 8x4 sized world. Two large rock formations ("#") exist in the top left and the lower right of the world, the rest of the world is freely walkable (" "). The current player position is marked with an "o". Based on the rules defined before, the player could move `left`, `right`, and `up`, but not `down`, because this way is blocked by a rock.

This game state can be encoded in very basic Python data types, for example, by using tuples and strings:

    state = (
    	"#####   ",
    	"###    #",
    	"#   o ##",
    	"   #####"
    )

You task is to test and implement a function `move` that takes two arguments: 1) a game state and 2) a direction into which the player marker should be moved. The function should check whether this move is possible and, if yes, return the mutated game state, as well as all possible walking directions in the new state, ordered alphabetically (i.e., `down` < `left` < `right` < `up`).

For example, a call to `move(state, "right")` should return the following result:

    (
    	(
	    	"#####   ",
	    	"###    #",
	    	"#    o##",
	    	"   #####"
	    ),
	    ("left", "up")
	)

The function should check several assumptions on the input data to ensure a consistent game state.

* The provided game state is valid if:	
    * ... it only contains the defined characters (" ", "#", "o").
    * ... each line has same length.
    * ... it contains exactly one player.
    * ... it has a sensible size (both dimensions are greater than 0).
    * ... at least one move is possible.
* The provided move is valid.

Whenever any of these assumptions is violated, `raise` a `Warning` to indicate that the current move cannot be executed. A good implementation should also include an appropriate error message to elaborate the `Warning` (e.g., `raise Warning("invalid character: x")`), but the automated grading will not take this into consideration. Make sure that your test suite checks whether an exception is raised in these cases! Various ways exist to do so, make yourself familiar with `self.assertRaises` to learn about the most convenient one.

Your task is to develop this function in a test-driven way. Both the test suite (`public/tests.py`) and the corresponding function (`public/script.py`) will be considered for the grading. The test suite based on its ability to correctly identify correct and incorrect implementations and the function itself based on its correctness. As such, the test suite must only access the top function `move` though, even if you decide to factor out functionality into utility functions in your own implementation.

**Note:** You can assume that the current field of the player is always a `free` field.

**Note:** This is a complex programming task. Think about how the task could be split into multiple sub-tasks and solve the problem by combining these smaller functions.

**Note:** The provided files define the signatures of various classes and functions. Do not change these signatures or the automated grading will fail.

**Note:** Both the test suite (`public/tests.py`) and the function (`public/script.py`) should be submitted for grading. Don't forget either of them.

**Note:** One of the pre-defined tests in `public/tests.py` is wrong and needs to be fixed to perform a correct test.
