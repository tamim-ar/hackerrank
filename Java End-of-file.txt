import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        
        // String name1 = scan.nextLine();
        // String name2 = scan.nextLine();
        // String name3 = scan.nextLine();
        
        // System.out.println(1 + " " + name1);
        // System.out.println(2 + " " + name2);
        // System.out.println(3 + " " + name3);
        
        int no = 1;
        while(scan.hasNext()){
            System.out.println(no++ + " " + scan.nextLine());
        }
        scan.close();
    }
}
