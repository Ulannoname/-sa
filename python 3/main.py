# """ pyttsx3"""
# """ veny ->"""
# """
# python -m venv venv
# venv\Script\activate
# """

# import pyttsx3

# engine = pyttsx3.init()


# voices = engine.getProperty('voices')
# for voice in voices:
#     if "english" in voice.name.lower():
#         engine.setProperty('voice', voice.id)
#         break


# engine.say("Aгай, you’re the best, you’re cool, THE very best and classy.")
# engine.runAndWait()

# """pyttsx3  kolorama"""
# import pyttsx3
# from colorama import Fore,Style

# while True:
#     enter_text = input(Fore.GREEN + "Please enter some text (or type'exit' to quit):"
#                        + Style.RESET_ALL)
#     if enter_text.lower() == 'exit':
#         print(Fore.RED + "Exiting the program.Goodbye!" + Style.RESET_ALL)
#         break
#     engine = pyttsx3.init()
#     engine.say(enter_text)
#     engine.runAndWait()
#     engine.stop()
#     print(Fore.YELLOW + "text has been spoken" + Style.RESET_ALL)
#     print(Fore.CYAN + "You can enter more text or type 'exit' to quit." + Style.RESET_ALL)




