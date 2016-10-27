import javax.swing.JOptionPane;

public class MatrixOne {

    private static double[][] matrix;
    private static double[][] lower;
    private static double[][] upper;
    private static int n = 0;

    private int cols;
    private int rows;

    public MatrixOne(int rows, int col) // The constructor for the matrix which allows
    {
        matrix = new double[rows][col];

        cols = col;
        this.rows = rows;
    }

    /**
     * This is a method that will add values to the matrix based on user input.
     */
    public void populateMatrix()
    {
        for(int i = 0; i < matrix.length; i++)
        {
            for(int j = 0; j < cols; j++)
            {
                String ans = JOptionPane.showInputDialog(null, "Enter the value you wish to input for " + i + j);  //Takes in the values from the user.
                matrix[i][j] = Double.parseDouble(ans);     //Takes the value and converts it to a double and adds it to the matrix.
            }
        }
     }

    /**
     * This is a method that will convert the matrix to a string.
     */
    public static String toString(double[][] arr)
    {
        String returnString = "";
        for(int i = 0; i < arr.length; i++)  //Loop that will add all of the elements to a string to be printed.
        {
            for(int j = 0; j < arr[0].length; j++)
            {
                returnString += arr[i][j];  //The elements are added to the string.
                returnString += " ";
            }
            returnString += "\n";
        }
        return returnString;
    }
    /**
     * This is the method that does the actual LU Factorization.
     */
    public void luFactorize()
    {
        double[][] L = new double[rows][cols];  //Creates a new double array to serve as the lower matrix.

        for(int i = 0; i < rows; i++)           // This whole for loop is used to fill the
        {                                       // Lower matrix with the values of an identity matrix.
            for(int j = 0;j < cols; j++)
            {
                if(i ==j)
                {
                    L[i][j] = 1.0;
                }
                else
                {
                    L[i][j] = 0.0;
                }
            }
        }

        int n = 0;
        for(int i = 0; i < matrix[0].length - 1; i++)  // This loop takes each of the rows and row reduces them.
        {
            for(int j = 1 + n; j < matrix.length; j++)
            {
                if(!(matrix[i][i] == 0.0))
                {
                    double divide = matrix[j][i]/matrix[i][i];
                    subtract(i,j,divide);

                    L[j][i] = divide;
                }
            }
            n++;
        }
        MatrixOne.lower = L; // The lower matrix is set to equal the matrix L we created previously.
        MatrixOne.upper = matrix; // The upper matrix is set to what is left of the original matrix.
    }
    /**
     * This method subtracts the rows of the specified and is used for row reduction.
     *
     * @param i - The rows the is being subtracted.
     * @param j - The row that is being subtracted from.
     * @param divide The value that the first row is scaled by during subtraction.
     */
    private void subtract(int i, int j, double divide) {

        for(int k = 0 + n; k < matrix[0].length; k++)
        {
            matrix[j][k] -= (divide* matrix[i][k]);
        }
    }

    // private boolean isSingular(double[][] upper2) throws NoSquareException { // A method that checks if the given matrix is singular.
    //     MatrixOne matrixNew = new MatrixOne(matrix);

    //     if(MatrixMathematics.determinant(matrixNew) == 0)
    //     {
    //         return true;
    //     }
    //     return false;
    // }

    /**
     * This runs the actual code that prints the output to the screen.
     *
     * @param args Default argument that java needs.
     * @throws NoSquareException is thrown when the matrix is not square.
     */
    public static void main(String args[])
    // throws NoSquareException
    {
        String rows = JOptionPane.showInputDialog(null, "Enter the number of rows:");

        String col = JOptionPane.showInputDialog(null, "Enter the number of columns:");

        int intRows = Integer.parseInt(rows);  //Converts the input into integers.
        int intCol = Integer.parseInt(col);   //Converts the input into integers.

        MatrixOne mat = new MatrixOne(intRows, intCol);

        mat.populateMatrix();
        System.out.println("Original Matrix:");
        System.out.println(MatrixOne.toString(matrix));

        // if(mat.isSingular(matrix))
        // {
        //     System.out.println("The Matrix is Singular!");// Checks if the matrix is singular.
        // }
        // else
        //     System.out.println("The Matrix is not Singular!");


                                                            //
        mat.luFactorize();                                  // This part is
        System.out.println("Upper Matrix:");                // responsible for printing out
        System.out.println(MatrixOne.toString(upper));      // all of the matrices.
        System.out.println("Lower Matrix:");                //
        System.out.println(MatrixOne.toString(lower));      //
    }
}