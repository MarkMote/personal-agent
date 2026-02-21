# pdfpc Cheatsheet

## Launch
```
pdfpc main.pdf          # normal (dual monitor: slides on external, presenter on laptop)
pdfpc -S main.pdf       # single screen (for practice, or Zoom sharing)
pdfpc -s main.pdf       # swap screens
pdfpc -d 35 main.pdf    # set timer duration to 35 minutes
```

## During Presentation
| Key | Action |
|-----|--------|
| Right / Space / Click | Next slide |
| Left / Backspace | Previous slide |
| g | Go to slide (type number, then Enter) |
| b | Blank screen (black) |
| w | Blank screen (white) |
| f | Freeze presentation (change slides on presenter only) |
| o | Toggle slide overview |
| n | Toggle notes view |
| e | Edit current slide notes live |
| p | Pause/resume timer |
| r | Reset timer |
| s | Start timer |
| Esc / q | Quit |

## Zoom Setup (Interview Day)
1. Run `pdfpc -S main.pdf` (single screen mode)
2. In Zoom, share the pdfpc window
3. Audience sees slides, you control from keyboard

## Notes in Beamer
Add after each frame:
```latex
\end{frame}
\note{Speaker notes for this slide.}
```
pdfpc reads these automatically and displays in presenter view.
