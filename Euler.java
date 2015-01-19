
/*
 Project Euler Solutions
 Jacob Waters
 2014-07-27
 */

public class Euler{
  public static void main(String[] args){
    String resultStr;
    String expectedStr;
    int resultInt;
    int expectedInt;
    
    
    //Problem 1 Test & result
    resultInt = problem1(10);
    expectedInt = 23;
    System.out.println("Problem 1\n-------------");
    System.out.println("Expected: " + expectedInt);
    System.out.println("Result: " + resultInt);
    System.out.println("Test: " + (resultInt==expectedInt));
    resultInt = problem1(1000);
    System.out.println("Solution: " + resultInt);
    
    //Problem 2 Test & result
    resultInt = problem2(100);
    expectedInt = 44;
    System.out.println("Problem 2\n-------------");
    System.out.println("Expected: " + expectedInt);
    System.out.println("Result: " + resultInt);
    System.out.println("Test: " + (resultInt==expectedInt));
    resultInt = problem2(4000000);
    System.out.println("Solution: " + resultInt);
    
    //Problem 3 Test & result
    resultInt = problem3(13195);
    expectedInt = 29;
    System.out.println("Problem 3\n-------------");
    System.out.println("Expected: " + expectedInt);
    System.out.println("Result: " + resultInt);
    System.out.println("Test: " + (resultInt==expectedInt));
    resultInt = problem2(600851475143);
    System.out.println("Solution: " + resultInt);
    
  }
  
  public static int problem1(int hi){
    //If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    //Find the sum of all the multiples of 3 or 5 below 1000.
    
    int sum = 0;
    
    for(int i=0; i<hi; i++){
      if(i%3==0 || i%5==0){
        sum += i;
      }
    }
    return sum;
  }
  
  public static int problem2(int hi){
    //By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    
    int sum = 2;
    int nextTerm = 0;
    int term1 = 1;
    int term2 = 2;
    
    while(nextTerm<hi){
      if(nextTerm%2==0){sum += nextTerm;}
      nextTerm = term1 + term2;
      term1 = term2;
      term2 = nextTerm;
    }
  return sum;
  }
  
  public static int problem3(int primeNum){
    
    
    
  }
}
