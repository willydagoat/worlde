
from pathlib import Path


word_file = Path ("words.txt")
def find_word_file():
 if word_file.exists():
  return word_file
 else:
  print("We ain't found nuttin")



def  load_word_bank(filename = "words.txt"):
 with open(filename, "r") as file:
     return [line.strip().lower() for line in file if len(line.strip()) ==5]

word_bank = load_word_bank()


def main():
    print("wordle test prod")
    words = load_word_bank(word_file)
    
if__name__== "__main__":
main()
  