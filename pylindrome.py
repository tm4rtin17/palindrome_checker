import typer
import string

app = typer.Typer()

#Check if word is a palindrome
@app.command()
def word(word: str):
    if not word.strip():
        typer.echo("Error: Please provide a non-empty word.")
        raise typer.Exit(code=1)
    word = word.lower() #Adjust to lowercase to remove case sensitivity errors

    word_reversed = word[::-1] #string slicing reverses word & compares it
    if word == word_reversed:
        typer.echo(f'\nThe word "{word}" is a palindrome!')
    else:
        typer.echo(f'\nThe word "{word}" is not a palindrome.')

@app.command()
def sentence(sentence: str):
    if not sentence.strip():
        typer.echo("Error: Please provide a non-empty sentence.")
        raise typer.Exit(code=1)
    sentence = sentence.lower() #Adjust to lowercase to remove case sensitivity
    sentence = sentence.strip(string.punctuation) #remove punctuation

    word_list = sentence.split()
    pdromes = []

    #Iterate over every word in the string to check for palindromes
    for word in word_list:
        word_reversed = word[::-1]
        #store palindromes in their own list
        if word == word_reversed:
            pdromes.append(word)

    #Get count of total palindromes and list them out    
    pdrome_count = len(pdromes)
    if pdrome_count == 1:
        typer.echo('\n1 palindrome was detected!')
        typer.echo(f'-{pdromes[0]}')
    elif pdrome_count > 1:
        typer.echo(f'\n{pdrome_count} palindromes detected!')
        for word in pdromes:
            typer.echo(f'-{word}')
    else:
        typer.echo('\nNo palindromes were detected.')

#Run main program
if __name__ == "__main__":
    app()
