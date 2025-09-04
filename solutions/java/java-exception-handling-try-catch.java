import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            // Read inputs
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            
            // Compute the division
            System.out.println(a / b);
        } catch (java.util.InputMismatchException e) {
            System.out.println("java.util.InputMismatchException");
        } catch (java.lang.ArithmeticException e) {
            System.out.println("java.lang.ArithmeticException: / by zero");
        }
        
        scanner.close();
    }
}
