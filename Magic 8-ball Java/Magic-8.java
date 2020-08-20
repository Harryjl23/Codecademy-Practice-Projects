import java.util.Random;
import java.util.Arrays;

// Magic 8-ball toy
public class Magic8 {
    Random rand = new Random();
    // Array of outcomes 
    String[] outcomes = {"Outlook not so good", "My sources say no",  "Definitely not", "Don't count on it", "Very doubtful", "Signs point to yes", "Most likely", "Outlook good",  "As I see it, yes", "It is decidedly so", "It is certain",  "Absolutely", "Without a doubt", "You may rely on it", "Yes definitely", "Yes", "Cannot predict now", "Concentrate and ask again", "Better not tell you now", "Reply hazy try again" };
  //  Generate a number between 0 - 19
  int randomNumber = rand.nextInt(20);
  // Generate a random answer
  String answer = outcomes[randomNumber];

 public static void main(String[] args){
  //  Create instance of Magic8 class
    Magic8 shake = new Magic8();
    System.out.println("Welcome to Magic 8-ball.");
    System.out.println("Savagely shaken Magic 8-ball!");
    System.out.println("The answer to your question is....\n");
    // Print out the random answer
    System.out.println(shake.answer);
  }
}