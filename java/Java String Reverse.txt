import java.util.Scanner;

public class PalindromeCheck {
    public static void main(String[] args) {
        // Create a Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter a string
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();

        // Convert the string to lowercase to handle case insensitivity
        input = input.toLowerCase();

        int left = 0;
        int right = input.length() - 1;

        // Check for palindrome
        while (left < right) {
            if (input.charAt(left) != input.charAt(right)) {
                System.out.println("No");
                System.exit(0);
            } else {
                left++;
                right--;
            }
        }

        System.out.println("Yes");

        // Close the scanner
        scanner.close();
    }
}
