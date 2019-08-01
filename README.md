# gtablackjackdoer
it solves blackjack for you, need I say more?

simply the many dependencies and you just may have a slow and impractical blackjack solver

#how does it work?
that's a good question
~~it doesn't~~
it uses mss to take a screenshot of the screen which is cropped by opencv then processed by Tesseract OCR
the result of the OCR is fed into a seperate script which uses moves.csv to play the move with the greatest chance of payout
it then pipes the result into gTTS which outputs an audio file which is played by playsound
the reason the script creates multiple mp3's is because playsound doesn't close the file handle on files it plays which causes an os error when you try and write to a file that was previously played
