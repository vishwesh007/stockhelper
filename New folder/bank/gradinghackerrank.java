package bank;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;






   

class Result {

    /*
     * Complete the 'gradingStudents' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts INTEGER_ARRAY grades as parameter.
     */

    public static List<Integer> gradingStudents(List<Integer> grades) {
    // Write your code here
int[] array = grades.stream().mapToInt(i->i).toArray();
for(int i=0;i<array.length;i++){
    
    if(array[i]<40){
        
    }
    if(array[i]>37){//37 is corner case
    System.out.println(array[i]+"  "+(array[i]%5));
        if(array[i]%5>2){//2 was the error and corner case greater than symbol was punched in wrong direction
            array[i]=(array[i]/5+1)*5;//divide was the error
        }
    }
    

}
grades.removeAll(grades);
for(int i=0;i<array.length;i++){
    
   grades.add(array[i]);

}
return grades;
    }

}

 public class gradinghackerrank {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
       // BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter());

        int gradesCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> grades = IntStream.range(0, gradesCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .map(String::trim)
            .map(Integer::parseInt)
            .collect(toList());

        List<Integer> result = Result.gradingStudents(grades);

      /*   bufferedWriter.write(
            result.stream()
                .map(Object::toString)
                .collect(joining("\n"))
            + "\n"
        );*/
        System.out.println(result.stream()
        .map(Object::toString)
        .collect(joining("\n")));

        bufferedReader.close();
       // bufferedWriter.close();
    }
}
