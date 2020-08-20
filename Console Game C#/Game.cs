using System;

namespace ConsoleGame
{
    class Game : SuperGame
    {
        public new static void UpdatePosition(string keyPressed, out int x, out int y)
        {
            // Sets variables to avoid errors
            x = 0;
            y = 0;
            switch (keyPressed)
            {
                // Detects which key the user pressed, takes the key through the switch statement then updates the Y and X axis accordingly
                case "UpArrow":
                    y -= 1;
                    break;
                case "DownArrow":
                    y += 1;
                    break;
                case "LeftArrow":
                    x -= 1;
                    break;
                case "RightArrow":
                    x += 1;
                    break;
                default:
                    x += 0;
                    y += 0;
                    break;
            }
        }

        public new static char UpdateCursor(string KeyPressed)
        {
            switch (KeyPressed)
            {
                // Display of cursor
                case "LeftArrow":
                    return '<';
                case "RightArrow":
                    return '>';
                case "UpArrow":
                    return '^';
                case "DownArrow":
                    return 'v';
                default:
                    return '<';
            }
        }

        public new static int KeepInBounds(int CurrentCoord, int MaxCoord)
        {
            if (CurrentCoord < 0)
            {
                // When the player goes to far right or the bottom edge, moves them to the opposite side 
                return MaxCoord;
            }
            else if (CurrentCoord > MaxCoord)
            {
                // When the player goes to far left or the top edge, moves them to the opposite side
                return 0;
            }
            else
            {
                // When the player is'nt touching any of the edges , they can carry on
                return CurrentCoord;
            }
        }

        public new static bool DidScore(int CharX, int CharY, int FruitX, int FruitY)
        {
            // Checks if is on the same X and Y coordinate as the fruit 
            if (CharX == FruitX && CharY == FruitY)
            {
                return true;
            }
            else
            {
                // If they are'nt on the same coord, do not add score!
                return false;
            }
        }
    }
}