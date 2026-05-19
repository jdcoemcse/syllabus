class Bitwise {
    public static void main(String[] args) 
    {
                System.out.println("\nBitwise Operator\n");
                
                int a = 0b1010; 
                int b = 0b1100; 

                System.out.println( "Value of a = " + a); 
                System.out.println( "Value of b = " + b); 
                
                System.out.println("a & b : " + (a & b)); 
                System.out.println("a | b : " + (a | b)); 
                System.out.println("a ^ b : " + (a ^ b)); 
                System.out.println("~a : " + (~a)); 
                System.out.println("a << 2 : " + (a << 2)); 
                System.out.println("b >> 1 : " + (b >> 1)); 
                System.out.println("b >>> 1 : " + (b >>> 1)); 
    }
}
