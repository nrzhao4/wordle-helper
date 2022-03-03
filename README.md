<h1>Wordle Helper</h1>
Wordle Helper is a tool designed to help you solve your daily Wordle :) Starting with a full list of valid Wordle answers, you can input commands which will be applied as filters. The availble commands are based on the clues that Wordle gives you, such as wrong letter, right letter wrong place, and right letter right place. As the list gets narrowed down, you will be closer and closer to guessing the correct answer. 

<h2>How to Use Wordle Helper (macOS)</h2>
<ul>
  <li>Clone this repository</li>
  <li>Make sure you have python3 installed. This is easiest using homebrew <link>(https://brew.sh)</link> then run <code>brew install python3</code> from your terminal</li>
<li>From the project root, run <code>python3 wordlehelper.py</code></li>
</ul>

<h2>Commands</h2>
<h3>no &lt;letter(s)&gt;</h3>
Indicates the given letter(s) are not in the word. You can include several letters at once. Example: <code>no abc</code> will eliminate all words that have the letters a, b, and c.

<h3>contains &lt;letter(s)&gt;</h3>
Indicates the given letter(s) are anywhere in the word. You can include several letters at once. Example: <code>contains abc</code> will eliminate all words that don't contain the letters a, b, and c.

<h3>contains &lt;letter&gt; not &lt;first/second/third/fourth/fifth&gt;</h3>
Indicates the letter is in the word but NOT in the given position. You can only include one letter. Example: <code>contains s not fifth</code></li> will filter the word list to only include words with the letter s in the first, second, third, or fourth position.

<h3>&lt;first/second/third/fourth/fifth&gt; &lt;letter&gt;</h3>
Indicates the letter is in the word at the given position. You can only include one letter. Example: <code>second s</code> will eliminate all words that don't have the letter s in the second position.

<h3>back</h3>
Undo the last command

<h3>help</h3>
Show a list of available commands

<h3>restart</h3>
Undo all filters and start from the full word list
