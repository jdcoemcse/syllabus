import java.util.Scanner; // Import the Scanner class

class SwitchCasestatement {

    public static void main(String[] args) {
System.out.println("\nUsing Switch Case to identify value of number from 1 to 5 \n");
        Scanner scanner = new Scanner(System.in); // Create a Scanner object for user input

        System.out.println("Enter a size number (1, 2, 3, 4, or 5): ");
        int sizeNumber = scanner.nextInt(); // Read the user input as an integer

        switch (sizeNumber) {
            case 1:
                System.out.println("Extra Small");
                break;
            case 2:
                System.out.println("Small");
                break;
            case 3:
                System.out.println("Medium");
                break;
            case 4:
                System.out.println("Large");
                break;
            case 5:
                System.out.println("Extra Large");
                break;
            default:
                System.out.println("Invalid size number");
        }

        scanner.close(); // Close the Scanner object
    }
}
