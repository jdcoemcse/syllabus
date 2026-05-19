class MultiDimensionalArray { 
    public static void main(String[] args) { 
        // Declare and initialize a 2x2 two-dimensional array 
        int[][] matrix = { 
            {1, 2}, 
            {3, 4} 
        }; 
 
        // Print elements of the two-dimensional array 
        System.out.println("Elements in the two-dimensional array:"); 
        for (int i = 0; i < matrix.length; i++) { 
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.println("Element at [" + i + "][" + j + "]: " + matrix[i][j]); 
            } 
        } 
    } 
} 
Output: