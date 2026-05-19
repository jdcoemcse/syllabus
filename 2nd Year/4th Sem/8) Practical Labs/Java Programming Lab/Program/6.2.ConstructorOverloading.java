class Employee { 
    String name; 
    int id; 

    // Default constructor 
    Employee() { 
        name = "Unknown"; 
        id = 0; 
    } 

    // Parameterized constructor 
    Employee(String empName, int empId) { 
        name = empName; 
        id = empId; 
    } 

    void display() { 
        System.out.println("Employee Details -> Name: " + name + ", ID: " + id); 
    } 

    public static void main(String[] args) { 
        // Creating objects using both constructors
        Employee emp1 = new Employee(); // Calls default constructor 
        Employee emp2 = new Employee("John Doe", 101); // Calls parameterized constructor 

        // Displaying details
        System.out.println("Displaying Employee Information:");
        emp1.display(); 
        emp2.display();  
    } 
}
