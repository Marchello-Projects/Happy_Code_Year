<img width="2728" height="1395" alt="Group 6" src="https://github.com/user-attachments/assets/4e1986b4-7776-4540-9e5a-966ef22f59a6" />

> [!INFO]
>A simple program that displays a Christmas tree decorated with ornaments (on which programming languages are written), with a garland and a New Year greeting

---

## Technology Stack:

Used Python and the Pygame library to render the greeting card

> [!EXAMPLE]
>```python
>running = True
>while running:
>    # Handle events (e.g., closing the window)
>    for event in pygame.event.get():
>        if event.type == pygame.QUIT:
>            running = False
>
>    # Fill the screen with black
>    SCREEN.fill(BLACK)
>
>    # Draw the blinking star
>    draw_star(star_pulse)
>    # Draw falling snow
>    draw_snow()
>    # Draw the tree
>    draw_tree()
>    # Draw the garland
>    draw_lights()
>    # Draw ornaments with programming languages
>    draw_toys()
>
>    # Update the star pulse
>    star_pulse += 0.08
>
>    # Update text color (title) via hue
>    hue += 0.005
>    if hue > 1:
>        hue = 0
>    draw_title(hue)
>
>    # Refresh the screen and set FPS
>    pygame.display.flip()
>    clock.tick(60)
>
># Quit Pygame and exit the program
>pygame.quit()
>sys.exit()
>```  

---

## Year Summary:

Eight pet projects were created:

1. **Tic-Tac-Toe (Python):**
   [https://github.com/Marchello-Projects/Tic-tac-toe_by_Marchello](https://github.com/Marchello-Projects/Tic-tac-toe_by_Marchello)

2. **Simple CLI Wallet for managing money and crypto (Python):**
   [https://github.com/Marchello-Projects/M-Wallet](https://github.com/Marchello-Projects/M-Wallet)

3. **Telegram bot using the VirusTotal API to check files for viruses (Python):**
   [https://github.com/Marchello-Projects/Virus_Check_bot](https://github.com/Marchello-Projects/Virus_Check_bot)

4. **Cookie Clicker (HTML, CSS, JS):**
   [https://github.com/Marchello-Projects/Cookie_clicker_by_Marchello](https://github.com/Marchello-Projects/Cookie_clicker_by_Marchello)

5. **Telegram bot for analyzing prompts with Mistral AI (Python):**
   [https://github.com/Marchello-Projects/Prompt_training_by_Marchello](https://github.com/Marchello-Projects/Prompt_training_by_Marchello)

6. **Mini messenger using the WebSocket protocol (Python):**
   [https://github.com/Marchello-Projects/WebSockChat](https://github.com/Marchello-Projects/WebSockChat)

7. **Tamagotchi API:**
   [https://github.com/Marchello-Projects/TamagoAPI](https://github.com/Marchello-Projects/TamagoAPI)

8. **New Year greeting card:**
   I congratulate programmers on the New Year! May the next year be more ambitious and better than the previous one!
