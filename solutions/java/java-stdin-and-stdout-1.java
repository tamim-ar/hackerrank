import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read input from stdin, as per the given number of lines
        while (scanner.hasNext()) {
            int a = scanner.nextInt();  // Read the integer
            System.out.println(a);      // Print the integer
        }
        
        scanner.close();  // Close the scanner
    }
}
