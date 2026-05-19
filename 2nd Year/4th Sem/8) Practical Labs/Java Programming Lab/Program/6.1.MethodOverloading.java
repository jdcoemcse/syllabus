class MethodOverloading {
    // Method with two integer parameters
    int add(int a, int b) {
        return a + b;
    }

    // Overloaded method with three integer parameters
    int add(int a, int b, int c) {
        return a + b + c;
    }

    // Overloaded method with two double parameters
    double add(double a, double b) {
        return a + b;
    }

    // Overloaded method with two string parameters
    String add(String a, String b) {
        return a + b; // Concatenates the two strings
    }
}

class Main {
    public static void main(String[] args) {
        MethodOverloading obj = new MethodOverloading();

        // Clear output messages
        System.out.println("Integer Addition (5 + 10): " + obj.add(5, 10));
        System.out.println("Integer Addition (5 + 10 + 15): " + obj.add(5, 10, 15));
        System.out.println("Double Addition (5.5 + 2.5): " + obj.add(5.5, 2.5));
        System.out.println("String Concatenation ('Hello, ' + 'World!'): " + obj.add("Hello, ", "World!"));
    }
}
