import java.text.NumberFormat;
import java.util.Locale;
import java.util.Scanner;

public class CurrencyFormatter {
    public static void main(String[] args) {
        // Create a Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Prompt the user to enter a double value
        double payment = scanner.nextDouble();

        // Locale for US
        NumberFormat usFormatter = NumberFormat.getCurrencyInstance(Locale.US);
        String us = usFormatter.format(payment);

        // Locale for India (custom)
        Locale indiaLocale = new Locale("en", "IN");
        NumberFormat indiaFormatter = NumberFormat.getCurrencyInstance(indiaLocale);
        String india = indiaFormatter.format(payment);

        // Locale for China
        NumberFormat chinaFormatter = NumberFormat.getCurrencyInstance(Locale.CHINA);
        String china = chinaFormatter.format(payment);

        // Locale for France
        NumberFormat franceFormatter = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        String france = franceFormatter.format(payment);

        // Output results
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);

        // Close the scanner
        scanner.close();
    }
}
